from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_HAS_ITEMS), \
            "The basket should be empty, but it is not"

    def go_to_basket_page(self):
        assert False, "There is no link to the basket page on the basket page"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.NO_ITEMS_IN_BASKET_MESSAGE), \
            "There should be a message that the basket is empty, but it is not"
