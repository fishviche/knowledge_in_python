def check_data(params: dict):
    response = {"error": False, "message": ""}
    try:
        full_name = params["fullname"]
        email = params["email"]
        phone = params["phone"]
        if (
            isinstance(full_name, str) is False
            or isinstance(email, str) is False
            or isinstance(phone, str) is False
        ):
            response["message"] = "Some data is not string"
            response["error"] = True
        elif len(full_name) > 100 or len(email) > 100 or len(phone) > 100:
            response["message"] = "Some data is too long"
            response["error"] = True
    except KeyError as e:
        response["message"] = "Incomplete data"
        response["error"] = True
    return response
