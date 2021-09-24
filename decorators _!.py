#if we want to take parameters in decorator function we want to import some function tools let's see
from functools import wraps
#defind a function with argments
def main_function(arg):
    def function1(func):
        @wraps(func)
        def function2(*a,**b):
            func(*a,**b)
            print(arg)
        return function2
    return function1
@main_function(50)
def cal(a,b):
    print(a*b)
cal(8,9)