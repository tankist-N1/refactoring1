from datetime import datetime
from typing import List, Optional

from sqlalchemy import String, TIMESTAMP, ForeignKey, Boolean, Integer, ARRAY, func
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy.orm import Mapped, mapped_column, relationship
from passlib.context import CryptContext

from models.base import Base

# Хеширование паролей — вынесено в отдельную переменную
_pwd_context = CryptContext(schemes=["sha256_crypt"])


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    _password: Mapped[str] = mapped_column("password", String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    telegram_id: Mapped[Optional[str]] = mapped_column(String(16), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, server_default="True", nullable=False)

    user_info: Mapped["UserInfo"] = relationship(
        back_populates="user", uselist=False, cascade="all, delete-orphan"
    )
    sessions: Mapped[List["UserSession"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    @hybrid_property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, raw_password: str) -> None:
        self._password = _pwd_context.hash(raw_password)

    @hybrid_method
    def verify_password(self, raw_password: str) -> bool:
        return _pwd_context.verify(raw_password, self._password)


class UnverifiedUser(Base):
    __tablename__ = "unverified_user"

    email: Mapped[str] = mapped_column(String(255), primary_key=True)
    project_ids: Mapped[List[int]] = mapped_column(
        ARRAY(Integer, dimensions=1), nullable=False, server_default="{}"
    )


class UserSession(Base):
    __tablename__ = "user_session"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), nullable=False, index=True
    )
    fingerprint: Mapped[str] = mapped_column(String(255), nullable=False)
    invalid_after: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False
    )
    identity: Mapped[str] = mapped_column(String(255), nullable=False)

    user: Mapped["User"] = relationship(back_populates="sessions")


class UserInfo(Base):
    __tablename__ = "user_info"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), primary_key=True
    )
    surname: Mapped[str] = mapped_column(String(64), nullable=False)
    name: Mapped[str] = mapped_column(String(64), nullable=False)
    patronymic: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String(16), nullable=True)
    position: Mapped[Optional[str]] = mapped_column(String(128), nullable=True)
    joined_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.current_timestamp()
    )

    user: Mapped["User"] = relationship(back_populates="user_info", uselist=False)
