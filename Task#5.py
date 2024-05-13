import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции '{func.__name__}': {execution_time:.4f} секунд")
        return result

    return wrapper

@timer
def sum_and_print(a, b):
    result = a + b
    print(f"Сумма {a} и {b} равна {result}")
    return result

@timer
def read_and_write():
    with open("input.txt", "r") as f:
        a, b = map(int, f.read().split())

    result = a + b

    with open("output.txt", "w") as f:
        f.write(str(result))

    print(f"Результат суммы {a} и {b} записан в файл output.txt")


sum_and_print(8, 24)
read_and_write()
