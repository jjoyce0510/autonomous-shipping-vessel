import enum

class TripState(enum.Enum):
    pending = 1
    active = 2
    complete = 3
    failed = 4
