# def redo_decor(func):
#     def ret_print():
#         print(func.__name__, "is cancelled")
#         return print
#     return ret_print()
#
# @redo_decor
# def second_print(f_str):
#     print(f_str)
#     return f_str
#
# second_print("ping")




# import time
# def func_timer(func):
#     def mesuare():
#         start = time.time()
#         func()
#         a = time.time() - start
#         print("Time for function {} is {}".format(func.__name__, a))
#     return mesuare
# @func_timer
# def print_s():
#     n= 100000
#     while n > 0:
#         n -= 1
#     return 2
#
# print_s()



# def dec(func):
#     def second(m):
#         second.n = second.n + 1
#         res = func(m)
#         print(second.n)
#         return  res
#     second.n = 0
#     return second
#
# @dec
# def fun_3_times(m):
#     if m > 0:
#         return fun_3_times(m - 1)
#     else:
#         return 0
#
# fun_3_times(6)
#
# def dec(func):
#     def second(*args, **kwargs):
#         print("Start {} ".format(func.__name__))
#         res = func(*args, **kwargs)
#         print("Stop {}".format(func.__name__))
#         return res
#     return second
# @dec
# def test(m):
#     print("2m = {}".format(2 * m))
#     return 2 * m
#
# test(2)


def dec(func):
    def second(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as e:
            print("Error!", e)
            return "Error! Function {} with {}".format(func.__name__, e)
    return second
@dec
def test(lst):
    for i in lst:
        print(1 / i)
lst = [1,0,1,1
       ]
test(lst)