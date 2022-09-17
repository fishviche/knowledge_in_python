from schemas.users_schema import check_data


def insert_user(user_info: dict, cur):
    """
    Function to insert users
    Input:
        user_info(dict): Dict with user data
        cur
        conn
    Output:
        response(dict): Dict with error(bool) and message(str)
    """
    response = check_data(user_info)
    if response["error"]:
        return response
    query_insert = """
        INSERT INTO users(fullname, email, phone)
        VALUES(%(fullname)s, %(email)s, %(phone)s)
    """
    cur.execute(query_insert, user_info)
    response = {"error": False, "message": "User created"}
    return response
