import datetime

# from typing import Callable, Any, Optional
import functools

# from src.masks import get_mask_card_number
import os


def log(filename=None):
    def decorator_log(func):
        @functools.wraps(func)
        def wrapper_log(*args, **kwargs):
            log_message = ""

            # сообщение о начале выполнения функции
            start_msg = f"{datetime.datetime.now()} - Started execution of {func.__name__}\n"
            log_message += start_msg

            try:

                result = func(*args, **kwargs)

                # сообщение об успешном выполнении функции
                end_msg = f"{datetime.datetime.now()} - Finished execution of {func.__name__} with result: {result}\n"
                log_message += end_msg

                if filename:
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
                    with open(filename, "a") as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message)

                # ЕСЛИ ЕСТЬ ЕЩЕ ОШИБКА
                raise

        return wrapper_log

    return decorator_log


log_path = os.path.join("logs", "mylogs.txt")


@log(filename=log_path)
def my_function(x, y):
    return x + y


my_function(1, 2)


@log()
def my_function_console(x, y):
    return x + y


my_function(3, 2)

# @log(filename=log_path)
# def get_mask_card_number(card_number: str) -> str:
#   return
# get_mask_card_number('7000792289606361')
