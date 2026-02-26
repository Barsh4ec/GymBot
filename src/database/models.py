import enum

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .engine import Base


class WeightType(str, enum.Enum):
    SELECTORIZED = "стек"
    PLATE_LOADED = "вільна вага"


class MachineCategory(str, enum.Enum):
    CHEST = "груди"
    ARMS = "руки"
    BACK = "спина"
    LEGS = "ноги"


class User(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    chat_id: Mapped[int] = mapped_column(unique=True)

    machines: Mapped[list["Machine"]] = relationship(
        "Machine",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    sets: Mapped[list["Set"]] = relationship(
        "Set",
        back_populates="user",
        cascade="all, delete-orphan"
    )


class Machine(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str]
    category: Mapped[MachineCategory]
    weight_type: Mapped[WeightType]
    pic_path: Mapped[str | None]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(
        "User",
        back_populates="machines"
    )

    sets: Mapped[list["Set"]] = relationship(
        "Set",
        back_populates="machine",
        cascade="all, delete-orphan"
    )


class Set(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    machine_id: Mapped[int] = mapped_column(ForeignKey("machines.id"))

    user: Mapped["User"] = relationship(
        "User",
        back_populates="sets"
    )
    machine: Mapped["Machine"] = relationship(
        "Machine",
        back_populates="sets"
    )

    reps: Mapped[list["Rep"]] = relationship(
        "Rep",
        back_populates="set",
        cascade="all, delete-orphan"
    )


class Rep(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    set_id: Mapped[int] = mapped_column(ForeignKey("sets.id"))
    rep_number: Mapped[int]
    weight: Mapped[float]

    set: Mapped["Set"] = relationship(
        "Set",
        back_populates="reps"
    )