from time import perf_counter


def measure_execution_time(func):
    """A decorator that measures the execution time of a function."""

    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print(f"Executed {func.__name__} in {execution_time:.2f}s")
        return result

    return wrapper
