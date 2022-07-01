import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default="chrome",
                     help="Choose browser: chrome or firefox (default: chrome)")
    parser.addoption('--language',
                     action='store',
                     default="en",
                     help="Choose language: en, ru, fr, de, es, etc (default: en)")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(options=options)
        browser.implicitly_wait(5)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
