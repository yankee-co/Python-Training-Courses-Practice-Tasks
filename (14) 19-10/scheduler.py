import datetime
from singleton_decorator import singleton

@singleton
class Scheduler:
    """Scheduler class for booking time slots"""

    _slot_length: int
    _booked_slots: list

    def __init__(self, slot_length: int):
        self._booked_slots = []

        if not isinstance(slot_length, int):
            raise TypeError(
                f"Slot length must be int, '{type(slot_length)}' received"
            )
        if slot_length % 15 != 0:
            raise ValueError(
                "Slot length must be multiplied by 15"
            )

        self._slot_length = slot_length

    def get_available_slots(self, d: datetime.datetime.date) -> list:
        """Returns list of available slots for specified date"""
        slots = []
        start = datetime.datetime(d.year, d.month, d.day)
        end = start + timedelta(days=1)

        while start < end:
            if start not in self._booked_slots:
                slots.append(start)
            start = start + timedelta(minutes = self._slot_length)

        return slots

    def book_slot(self, dt: datetime.datetime) -> bool:
        """Books slot if available"""
        if dt in self._booked_slots:
            return False
        self._booked_slots.append(dt)
        return True

    def cancel_booking(self, dt: datetime.datetime) -> bool:
        """Cancels booking for passed slot if possible"""
        if dt in self._booked_slots:
            self._booked_slots.remove(dt)
            return True
        return False

    @property
    def booked_slots(self) -> list:
        """Returns list of booked slots"""
        return self._booked_slots

    def get_unused_time(self, dt: datetime.datetime) -> int:
        """ Returns unused time for a date """
        minutes = 0
        start = datetime.datetime(dt.year, dt.month, dt.day)
        end = start + timedelta(days=1)
        while start < end:
            if start not in self._booked_slots:
                minutes += start.minute
            start = start + timedelta(minutes = self._slot_length)
        if minutes >= 60:
            return f'{minutes/60}, free hours'
        return f'{minutes} free minutes'

    def is_available(self, dt: datetime.datetime) -> bool:
        """ Returns True or False depends on book is available or not """
        if dt in self.booked_slots:
            return False
        return True

    def is_booked(self, dt: datetime.datetime) -> bool:
        """ Returns True or False depends on book is available or not """
        if dt in self.booked_slots:
            return True
        return False

class Slot():
    """ Book info """

    long: int = 15

    def __init__(self, length, year, month, day, hour, minute):
        self.dt = datetime.datetime(year, month, day, hour, minute)
        self.length = length

    @property
    def duration(self):
        return self.long

    @property
    def start_at(self):
        return self.dt.time()

    @property
    def end_at(self):
        return (self.dt + datetime.timedelta(minutes = self.length)).time()
#dt = datetime.datetime(2020, 12, 25, 16, 30)
ins = Slot(year = 2020, month = 12, day = 15, hour = 16, minute = 15, length = 15)
