from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success:first-child strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child")
    MESSAGE_BASKET = (By.CSS_SELECTOR, ".alert-info")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")


class BasketPageLocators:
    BASKET_HAS_ITEMS = (By.CSS_SELECTOR, ".basket_summary")
    NO_ITEMS_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
