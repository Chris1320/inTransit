from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlmodel import Session, select

from centralserver.internals.auth_handler import verify_access_token
from centralserver.internals.db_handler import get_db_session
from centralserver.internals.logger import LoggerFactory
from centralserver.internals.models import DecodedJWTToken, User, UserPublic

logger = LoggerFactory().get_logger(__name__)

router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_db_session)],
)

logged_in_dep = Annotated[DecodedJWTToken, Depends(verify_access_token)]


@router.get("/get", status_code=status.HTTP_200_OK, response_model=list[UserPublic])
async def get_all_users(
    token: logged_in_dep,
    session: Annotated[Session, Depends(get_db_session)],
) -> list[UserPublic]:
    logger.debug("user %s fetching all user info", token.username)
    return [
        UserPublic.model_validate(user) for user in session.exec(select(User)).all()
    ]


@router.get("/me")
async def get_user_profile(
    token: logged_in_dep,
    session: Annotated[Session, Depends(get_db_session)],
) -> UserPublic:
    logger.debug("Fetching user profile for user ID: %s", token.id)
    return UserPublic.model_validate(
        session.exec(select(User).where(User.id == token.id)).one()
    )
