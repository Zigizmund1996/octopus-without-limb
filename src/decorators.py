import datetime
import os
import functools

log_path = os.path.join("logs", "mylogs.txt")


def log(filename=None):
    def decorator_log(func):
        @functools.wraps(func)
        def wrapper_log(*args, **kwargs):
            log_message = ""

            # сообщение о начале выполнения функции
            start_msg = f"{datetime.datetime.now()} - Started execution of {func.__name__}\n"
            log_message += start_msg

            try:
                result = func(*args, *kwargs)

                # сообщение об успешном выполнении функции
                end_msg = f"{datetime.datetime.now()} - Finished execution of {func.__name__} with result: {result}\n"
                log_message += end_msg

                if filename:
                    os.makedirs(os.path.dirname(filename), exist_ok=True)
                    with open(filename, "a") as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message)

                return result
            except Exception as e:
                # сообщение о возникшей ошибке
                error_msg = (
                    f"{datetime.datetime.now()} - Error in {func.__name__}; "
                    f"Type: {type(e).__name__}; Args: {args}; Kwargs: {kwargs}\n"
                )
                log_message += error_msg

                if filename:
                    os.makedirs(os.path.dirname(filename), exist_ok=True)
                    with open(filename, "a") as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message)

                # пишем дальше
                raise

        return wrapper_log

    return decorator_log


@log(filename=log_path)
def my_function(x, y):
    return x + y


my_function(1, 2)


@log()
def my_function_console(x, y):
    return x + y


my_function_console(3, 2)


@log()
def my_function_error(x, y):
    return x + y


try:
    my_function_error("undefined_var", 2)
except Exception as e:
    print(f"Caught an exception: {e}")
