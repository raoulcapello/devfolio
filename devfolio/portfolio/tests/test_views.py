import pytest
from django import urls
from pytest_django.asserts import assertTemplateUsed


# These are the user stories of our user - let's call her Lauryn.
@pytest.mark.skip
@pytest.mark.django_db
def test_profile_page(client):
    # Lauryn checks out the portfolio page.
    url = urls.reverse("portfolio:list")

    response = client.get(url)

    assert response.status_code == 200
    assertTemplateUsed(response, "portfolio/list.html")
