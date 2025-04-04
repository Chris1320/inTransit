from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlmodel import Session

from centralserver.internals.auth_handler import (
    authenticate_user,
    create_access_token,
)
from centralserver.internals.config_handler import app_config
from centralserver.internals.db_handler import get_db_session
from centralserver.internals.logger import LoggerFactory
from centralserver.internals.models import (
    JWTToken,
    User,
    UserLoginRequest,
    UserPublic,
)
from centralserver.internals.user_handler import create_user

logger = LoggerFactory().get_logger(__name__)

router = APIRouter(
    prefix="/auth",
    tags=["authentication"],
    # dependencies=[Depends(get_db_session)],
)


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=UserPublic)
async def create_new_user(
    new_user: UserLoginRequest, session: Annotated[Session, Depends(get_db_session)]
) -> UserPublic:
    """Create a new user in the database.

    Args:
        new_user: The new user's information.
        session: The database session.

    Returns:
        A newly created user object.
    """

    logger.info("Creating new user: %s", new_user.username)
    user = UserPublic.model_validate(create_user(new_user, session))
    logger.debug("Returning new user information: %s", user)
    return user


@router.post("/token", response_model=JWTToken)
async def request_access_token(
    data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[Session, Depends(get_db_session)],
) -> JWTToken:
    """Get an access token for a user.

    Args:
        data: The data from the OAuth2 password request form.
        session: The database session.

    Returns:
        A JWT token object containing the access token and token type.

    Raises:
        HTTPException: If the user cannot be authenticated.
    """

    logger.info("Requesting access token for user: %s", data.username)
    user: User | None = authenticate_user(data.username, data.password, session)

    if not user:
        logger.warning(
            "Failed to authenticate user: %s (Invalid credentials)", data.username
        )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    return JWTToken(
        access_token=create_access_token(
            user.username,
            user.id,
            timedelta(minutes=app_config.authentication.access_token_expire_minutes),
        ),
        token_type="bearer",
    )
