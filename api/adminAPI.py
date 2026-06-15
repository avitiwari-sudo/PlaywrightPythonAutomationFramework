import pytest

@pytest.mark.api
def get_adminUsers(api_context):

    response = api_context.get(
        "/web/index.php/api/v2/admin/users",
    )

    assert response.ok
    data = response.json()
    print(data)