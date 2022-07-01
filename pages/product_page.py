from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_button_click(self):
        add_product_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        self.scroll_to_element(add_product_button)
        add_product_button.click()
        if "?promo=" in self.url:
            self.solve_quiz_and_get_code()

    def should_be_add_product_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add product button is not presented"

    def should_be_cost_of_basket_equals_price_of_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        result = self.wait_for_value_in_element(ProductPageLocators.MESSAGE_BASKET_PRICE, product_price)
        assert result, "The cost of the basket does not match the price of the product"

    def should_be_message_product_name_equals_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        result = self.wait_for_value_in_element(ProductPageLocators.MESSAGE_PRODUCT_NAME, product_name)
        assert result, "The name of the added product does not equal the product name"

    def should_be_message_with_the_cost_of_the_cart(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET), \
            "No message with the cost of the cart"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Add product message is not presented"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "The success message should disappear, but it didn't"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
