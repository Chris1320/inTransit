from datetime import datetime, timedelta, timezone
from typing import Annotated, Any

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlmodel import Session, select

from centralserver.internals.config_handler import app_config
from centralserver.internals.logger import LoggerFactory
from centralserver.internals.models import DecodedJWTToken, User

logger = LoggerFactory().get_logger(__name__)
crypt_ctx = CryptContext(schemes=["argon2"], deprecated="auto", argon2__type="ID")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/auth/token")


def get_hashed_password(plaintext_password: str, salt: str | None = None) -> str:
    """Hash the plaintext password using Argon2id algorithm.

    Args:
        password: The password to hash.
        salt: The salt to use for hashing.

    Returns:
        The hashed password in its encoded form.
    """

    if salt:
        logger.debug("Hashing using Argon2id with salt.")
        return crypt_ctx.hash(plaintext_password, salt=salt)

    logger.debug("Hashing using Argon2id without salt.")
    return crypt_ctx.hash(plaintext_password)


def authenticate_user(
    username: str, plaintext_password: str, session: Session
) -> User | None:
    """Find the user in the database and verify their password.

    Args:
        username: The username of the user to authenticate.
        plaintext_password: The plainext password to verify.
        session: The database session to use.

    Returns:
        A User object if the user is found and the password is
        correct, None otherwise.
    """

    logger.debug("Attempting to authenticate user `%s`", username)
    found_user: User | None = session.exec(
        select(User).where(User.username == username)
    ).first()

    if not found_user:
        logger.debug("Authentication failed: %s (user not found)", username)
        return None

    if crypt_ctx.verify(plaintext_password, found_user.password):
        logger.debug("Authentication successful: %s", username)
        logger.debug("Returning user information for user id: %s", found_user.id)
        return found_user

    else:
        logger.debug("Authentication failed: %s (invalid password)", username)
        return None


def create_access_token(username: str, user_id: str, expiration_td: timedelta):
    """Create a JWT access token for the user, valid for +<expiration_td>.

    Args:
        username: The username of the user.
        user_id: The ID of the user.
        expiration_td: The time delta for the token expiration.

    Returns:
        The JWT access token.
    """

    logger.debug("Creating access token for user `%s`...", username)
    token_data: dict[str, Any] = {
        "sub": username,
        "id": user_id,
        "exp": datetime.now(timezone.utc) + expiration_td,
    }

    return jwt.encode(
        token_data,
        app_config.authentication.secret_key,
        app_config.authentication.algorithm,
    )


async def verify_access_token(
    token: Annotated[str, Depends(oauth2_bearer)],
) -> DecodedJWTToken | None:
    """Get the current user from the JWT token.

    Args:
        token: The JWT token.

    Returns:
        The decoded JWT token payload containing the username and user ID.

    Raises:
        HTTPException: Raised when the token is invalid or expired.
    """

    try:
        payload = jwt.decode(
            token,
            app_config.authentication.secret_key,
            algorithms=[app_config.authentication.algorithm],
        )
        username: str | None = payload.get("sub")
        user_id: str | None = payload.get("id")
        if username is None or user_id is None:
            logger.warning("Failed to validate user JWT: %s", payload)
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed to validate user.",
            )

        return DecodedJWTToken(
            id=user_id,
            username=username,
        )

    except JWTError:
        logger.warning("Failed to decode JWT: %s", token)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Failed to validate user.",
        )
