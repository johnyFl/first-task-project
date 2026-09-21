import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"{func.__name__} took {end - start:.4f} seconds")

        return result

    return wrapper


@timer
def add(a, b):
    time.sleep(1)
    return a + b


@timer
def multiply(a, b):
    time.sleep(2)
    return a * b


@timer
def divide(a, b):
    time.sleep(0.5)
    return a / b


result1 = add(10, 20)
print("Result:", result1)

result2 = multiply(10, 20)
print("Result:", result2)

result3 = divide(20, 5)
print("Result:", result3)

