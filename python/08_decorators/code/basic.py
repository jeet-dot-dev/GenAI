# from functools import wraps

# def my_decorator(func):
#     @wraps(func)
#     def warpper():
#         print("before")
#         func()
#         print("after")
#     return warpper    

# @my_decorator
# def greet():
#     print("hello")

# greet()    

#project 1

# from functools import wraps

# def log_activity(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         print(f"Calling : {func.__name__}")
#         result = func(*args,**kwargs)
#         print(f"Finshed")
#         return result
#     return wrapper

# @log_activity
# def greet(name):
#     print(f"Hello{name}")

# greet("jeet")