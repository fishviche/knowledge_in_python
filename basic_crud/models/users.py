from schemas.users_schema import check_data, check_id


def get_user(cur, id=0):
    """
    Function to get all users by default or one user
    Input:
        Id(int): User ID, by default is 0
        cur:
    Output:
        response(dict): Dict with all users or one user
    """
    response = check_id(id)
    if response["error"]:
        return response
    get_users = """
        WITH one_user AS (SELECT * FROM users WHERE id = %s)
        SELECT
            *
        FROM
            one_user
        UNION 
        SELECT
            *
        FROM
            users
        WHERE NOT EXISTS (SELECT * FROM one_user LIMIT 1) 
        """
    cur.execute(get_users, (id,))
    users = cur.fetchall()
    if id != 0 and len(users) > 1:
        response["error"] = True
        response["message"] = "User ID not exists"
        return response
    response["error"] = False
    response["message"] = "Sucess"
    response["data"] = users
    return response


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


def update_user(user_info: dict, cur):
    """
    Function to update users
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
    response = check_id(user_info['id'])
    if response["error"]:
        return response
    update_user = """
        UPDATE
            users
        SET
            fullname = %(fullname)s, 
            email = %(email)s, 
            phone = %(phone)s
        WHERE
            id = %(id)s
    """
    cur.execute(update_user, user_info)
    response = {"error": False, "message": "User updated"}
    return response