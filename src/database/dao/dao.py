from .base import BaseDAO
from ..models import User, Machine, Set, Rep


class UserDAO(BaseDAO):
    model = User
    


class MachineDAO(BaseDAO):
    model = Machine


class SetDAO(BaseDAO):
    model = Set


class RepDAO(BaseDAO):
    model = Rep
