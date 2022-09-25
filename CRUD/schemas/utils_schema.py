def is_too_long(len_max: int, key: str, value: str):
    """
    Function to test is a variable is too long (with a max len)
    Input:
        len_max(int): Lenght max of a variable
        key(str): Name of variable
        value(str): Variable
    Output
        response(dict): Response with error_message(str) and error(bool)
    """
    response = {
        "error": False,
        "error_message": ""
    }
    if len(value) > len_max:
        response['error'] = True
        response['error_message'] = f'{value} is too long'
    return response