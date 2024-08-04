import logging
import os

project_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
log_directory = os.path.join(project_root, "logs")
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
log_file = os.path.join(log_directory, "masks.log")

file_handler = logging.FileHandler(log_file, mode="w")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает номер карты (card_number)
    и возвращает маску карты (mask_card_number)
    """
    try:
        logger.info(f"Получен номер карты для маскирования: {card_number}")
        cleaned_user_cart_input = card_number.replace(" ", "")
        # если пользователь вводит номер карты с пробелами мы их убираем
        cleaned_user_cart_input_list = list(cleaned_user_cart_input)
        elements_to_insert = [(4, " "), (9, " "), (14, " ")]
        # для добавления пробелов по индексу
        replace_elements = [7, 8, 10, 11, 12, 13]
        # для замены элементов на '*'
        for index, element in elements_to_insert:
            cleaned_user_cart_input_list.insert(index, element)

        for index in replace_elements:
            cleaned_user_cart_input_list[index] = "*"

        mask_card_number = "".join(cleaned_user_cart_input_list)
        logger.info(f"Маска карты успешно создана: {mask_card_number}")
        return mask_card_number
    except Exception as e:
        logger.error(f"Ошибка при маскировании номера карты: {e}")
        raise


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает номер счета (account_number)
    и возвращает маску счета (mask_account_number)
    """
    try:
        logger.info(f"Получен номер счета для маскирования: {account_number}")
        user_account_number_list = list(account_number)
        del user_account_number_list[:-6]
        replace_elements = [0, 1]
        for index in replace_elements:
            user_account_number_list[index] = "*"
        mask_account_number = "".join(user_account_number_list)
        logger.info(f"Маска счета успешно создана: {mask_account_number}")
        return mask_account_number
    except Exception as e:
        logger.error(f"Ошибка при маскировании номера счета: {e}")
        raise


card_number_example = "1234567890123456"
account_number_example = "123456789012345567"
masked_card = get_mask_card_number(card_number_example)
masked_account = get_mask_account(account_number_example)
print(f"Маскированный номер карты: {masked_card}")
print(f"Маскированный номер счета: {masked_account}")
