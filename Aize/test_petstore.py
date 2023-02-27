import requests
import pytest
import json

# API endpoint
url = "https://petstore.swagger.io/v2"

# Test case to create a new user
def test_create_user():
    # Request body
    payload = {
        "id": 1,
        "username": "testuser",
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": "password",
        "phone": "1234567890",
        "userStatus": 1
    }

    # Make POST request to create user
    response = requests.post(f"{url}/user", json=payload)

    # Check response status code
    assert response.status_code == 200


# Test case to get details of the new user
def test_get_user_details():
    # User ID of the newly created user
    user_name = "testuser"

    # Make GET request to get user details
    response = requests.get(f"{url}/user/{user_name}")

    # Check response status code
    assert response.status_code == 200
    json_data = json.loads(response.content)
    assert json_data["lastName"] == "User"

# Test case to delete the new user
def test_delete_user():
    # User ID of the newly created user
    user_name = "testuser"

    # Make DELETE request to delete user
    response = requests.delete(f"{url}/user/{user_name}")

    # Check response status code
    assert response.status_code == 200


if __name__ == "__main__":
    pytest.main(["-v", '--html=report.html'])
