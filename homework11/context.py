from contextlib import contextmanager
from datetime import datetime


#
# class ContextMen(object):
#     def __init__(self, a):
#         a.lock = False
#
#     def __enter__(self):
#         a.lock = True
#         return a.lock
#
#
#     def __exit__(self, *args):
#         a.lock = False
#         return a.lock
#
# class Lock(object):
#     def __init__(self):
#         self.lock = False
#
# a = Lock()
# print(a.lock)
# with ContextMen(a):
#     print(a.lock)
#
# print(a.lock)
# @contextmanager
# def no_exceptions():
#     try:
#         yield
#     except Exception as e:
#         print(e)
# with no_exceptions():
#     a = 1/0
#     print(a)

class Contextmen():
    def __init__(self):
        pass
    def __enter__(self):
        self.start = datetime.now()
    def __exit__(self, *args):
        self.stop = datetime.now()
        print("Time for execution {}".format(self.stop - self.start))

with Contextmen():
    a = 1000000
    while a > 0:
        a -=1

