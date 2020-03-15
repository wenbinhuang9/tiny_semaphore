from threading import Condition

class Semaphore():
    def __init__(self, value = 1):
        if value < 0:
            raise ValueError("semaphore value must be greater than 0")
        self._value = value
        self._cond = Condition()

    def acquire(self):
        with self._cond:
            while self._value <= 0:
                self._cond.wait()
            else:
                self._value -= 1

    def release(self):
        with self._cond:
            self._value += 1
            self._cond.notify()

    __enter__ = acquire
    __exit__ = release