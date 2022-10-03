import pytest
from schemas.users_schema import check_data


class TestUser:
    def test_no_params(self):
        response = check_data({})

        assert response["error"] is True
        assert response["message"] == "Incomplete data"

    def test_no_string(self):
        response = check_data({"fullname": "xxx", "email": "xx@xx", "phone": 98765})

        assert response["error"] is True
        assert response["message"] == "Some data is not string"

    def test_too_long(self):
        full_name = "a" * 105
        response = check_data({"fullname": full_name, "email": "xx@xx", "phone": '98765'})

        assert response["error"] is True
        assert response["message"] == "Some data is too long"
