import math
import threading
from sys import stderr
from typing import Union, Any, List, Callable, Tuple
from queue import Queue
from collections import defaultdict


def clamp(val: Union[int, float], min_val: Union[int, float], max_val: Union[int, float]) -> Union[int, float]:
    """
    Clamps value

    :param val: value to be clamped
    :type val: Union[int, float]
    :param min_val: minimum value
    :type min_val: Union[int, float]
    :param max_val: value to be clamped
    :type vmax_al: Union[int, float]
    :returns: clamped value
    :rtype: Union[int, float]
    """

    if min_val > max_val:
        raise ValueError("Minimum value is bigger than maximum value")

    return max(min_val, min(val, max_val))


class XList(list):
    """
    Extended list
    """

    def rotate(self, n: int) -> None:
        """Rotate list by n

        Keyword arguments:
        n -- Ammount to shift (left to right if n > 0)
        """
        step = int(abs(n)/n)
        for i in range(0, n, step):
            self[:] = self[1*step:] + self[:1*step]

    def unique(self) -> List:
        """
        Returns all unique values
        """
        return [el for el in self if self.count(el) == 1]


class EVM:
    def __init__(self, show_warnings=True, panic=True, threaded_mode=True):
        self.show_warnings = show_warnings
        self.panic = panic
        self.threaded_mode = threaded_mode
        self.work = True

        self.subs = defaultdict(lambda: [])
        self.events = Queue()
        self.worker_thread = threading.Thread(target=self._worker, daemon=True)
        self.worker_thread.start()

    def subscribe(self, event: str, callback: Callable):
        """subscribe to an event

        event -- event name

        callback -- function to be called on emit

        """
        self.subs[event].append(callback)

    def emit(self, event: str, args: Tuple = None):
        """emit an event

        event -- event name

        args -- arguments to pass to callbacks
        """
        if event not in self.subs:  # if event has no subs ignore emit
            if self.show_warnings:
                print(
                    f"[WARNING] event `{event}` has no subscriptions", file=stderr)
            if self.panic:
                exit(1)
            return
        if args is None:
            args = ()
        self.events.put((event, args))

    def wait(self, event_complete=False):
        """run until closed or no events to do"""
        if event_complete:
            self.events.join()
        else:
            self.worker_thread.join()

    def end_worker(self):
        self.work = False

    def _runner(self, func, *args):
        """internal runner for callbacks

        this is to allow calling `task_done()` to be called

        """
        t = threading.Thread(target=func, args=args, daemon=True)
        t.start()
        t.join()
        self.events.task_done()

    def _worker(self):
        """worker responsible for handling events"""
        if self.threaded_mode:
            while self.work:
                event, args = self.events.get()
                for func in self.subs[event]:
                    threading.Thread(target=self._runner,
                                     args=(func, *args), daemon=True).start()
        else:
            while self.work:
                event, args = self.events.get()
                for func in self.subs[event]:
                    func(*args)
                    self.events.task_done()


# OUTSOURCED
def addVectors(angle1, length1, angle2, length2):
    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2
    length = math.hypot(x, y)
    angle = 0.5 * math.pi - math.atan2(y, x)
    return (angle, length)


class COLORS:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    SOME_GREY = (123, 123, 123)
