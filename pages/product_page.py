from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_product_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add product button is not presented"

    def add_product_button_click(self):
        add_product_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_product_button.click()

    def should_be_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BEEN_ADDED_TO_BASKET),\
            "Add product message is not presented"

    def should_be_message_product_name_equals_product_name(self):
        message_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name == message_product_name, \
            "The name of the added product does not equal the product name"

    def should_be_message_with_the_cost_of_the_cart(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET), \
            "No message with the cost of the cart"

    def should_be_cost_of_basket_equals_price_of_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_cost = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_PRICE).text
        assert product_price == basket_cost, "The cost of the basket does not match the price of the product"
