def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает номер карты (card_number)
    и возвращает маску карты (mask_card_number)
    """

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
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает номер счета (account_number)
    и возвращает маску счета (mask_account_number)
    """

    user_account_number_list = list(account_number)
    del user_account_number_list[:-6]
    replace_elements = [0, 1]
    for index in replace_elements:
        user_account_number_list[index] = "*"
    mask_account_number = "".join(user_account_number_list)
    return mask_account_number
