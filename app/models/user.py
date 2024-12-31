from datetime import datetime
from enum import StrEnum

from sqlalchemy import Boolean, Date, String, Table, Column, Text, TIMESTAMP, UUID, Enum

from app.database.client import metadata
from app.helper.generator import timezone


class UserRoleEnum(StrEnum):
    capster = "capster"
    administrator = "administrator"
    customer = "customer"


user = Table(
    "user",
    metadata,
    Column(name="uuid", type_=UUID(), primary_key=True),
    Column(name="email", type_=String(length=255), unique=True, nullable=False),
    Column(name="password", type_=String(length=255), nullable=False),
    Column(name="created_at", type_=TIMESTAMP(timezone=True), default=datetime.now(tz=timezone)),
    Column(name="updated_at", type_=TIMESTAMP(timezone=True), onupdate=datetime.now(tz=timezone)),
    Column(name="deleted_at", type_=TIMESTAMP(timezone=True), nullable=True),
    Column(name="created_by", type_=String(length=255)),
    Column(name="updated_by", type_=String(length=255)),
    Column(name="deleted_by", type_=String(length=255)),
)