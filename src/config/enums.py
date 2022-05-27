from .constants import STATUSES, UNITS, ROLES
from enum import Enum


class OrderStatus(str, Enum):
    pending = STATUSES.PENDING.value
    completed = STATUSES.COMPLETED.value
    in_progress = STATUSES.IN_PROGRESS.value
    packed = STATUSES.PACKED.value


class Units(str, Enum):
    kg = UNITS.KG.value
    gram = UNITS.GRAM.value
    piece = UNITS.PIECE.value
    ml = UNITS.ML.value
    litre = UNITS.LITRE.value


class Roles(str, Enum):
    owner = ROLES.OWNER.value
    customer = ROLES.OWNER.value
