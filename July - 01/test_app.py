from app import greet_user, add_numbers


def test_greet_user():
    result = greet_user("Abdullah")
    assert result == "Hello, Abdullah! Welcome to Azure DevOps CI/CD."


def test_add_numbers():
    result = add_numbers(10, 20)
    assert result == 30
