import pytest

# These are the user stories of our user - let's call her Lauryn.


@pytest.mark.usefixtures("chrome_driver_init")
class TestFunctional:
    # Lauryn heard about this cool new app for showcasing a webdevelopers or
    # web designers portfolio.
    @pytest.mark.slow
    def test_open_url(self, live_server):
        # She types in the URL in her browser's address bar and presses 'enter'.
        self.driver.get((f"{live_server.url}"))

        # She notices the name of the app in the title bar.
        assert "devfolio" in self.driver.title
        # She notices a button with the text 'Portfolio'.
        assert "Portfolio" in [
            element.text for element in self.driver.find_elements_by_tag_name("a")
        ]
        # She notices a section with the header text 'My portfolio'.
        assert "My portfolio" in [
            element.text for element in self.driver.find_elements_by_tag_name("h2")
        ]
