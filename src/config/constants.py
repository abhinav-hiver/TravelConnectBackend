import enum


class BaseEnum(enum.Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class STATUSES(BaseEnum):
    PENDING = "pending"
    COMPLETED = "completed"
    IN_PROGRESS = "in_progress"
    PACKED = "packed"


class UNITS(BaseEnum):
    KG = "kg"
    GRAM = "gram"
    PIECE = "piece"
    ML = "ml"
    LITRE = "litre"


class TOKEN:
    expire_time_in_days = 30


class ROLES(BaseEnum):
    OWNER = "owner"
    CUSTOMER = "customer"
