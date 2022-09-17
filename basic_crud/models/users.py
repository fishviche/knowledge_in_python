def insert_user(user_info: dict, cur, conn):
    query_insert = """
        INSERT INTO users(fullname, email, phone)
        VALUES(%(fullname)s, %(email)s, %(phone)s)
    """
    cur.execute(query_insert, user_info)
    