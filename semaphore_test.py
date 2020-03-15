import threading
import unittest

from threading import Thread
from semaphore import Semaphore
class MyTestCase(unittest.TestCase):
    def test_semaphore(self):
        s = Semaphore()

        def run(sem, id):
            sem.acquire()
            print("thread={0} getting semaphore".format(id))
            sem.release()
        t1 = Thread(target=run, args=(s, "thread1",))
        t2 = Thread(target=run, args=(s, "thread2",))

        t2.start()
        t1.start()

if __name__ == '__main__':
    unittest.main()
