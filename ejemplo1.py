
# def debug(f):
#     def new_function(a, b):
#         print("Function add() called!")
#         return f(a, b)
#     return new_function

def debug(f):
    def new_function(*args, **kwargs):
        print("Function %s() called!" % (f.__name__))
        return f(*args, **kwargs)
    return new_function

@debug
def add(a, b):
    return a + b

@debug
def add2(a):
    return a + 1 

print(add(10, 8))
print(add2(10))
