from .base_page import BasePage
from .locators_m import BasketPageLocators


class BasketPage(BasePage):
    def should_see_basket_empty_msg(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert "Your basket is empty." in message, f"EXPECTED: 'Your basket is empty.' ACTUAL: {message}"

    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_ELEMENT), \
            "Basket is not empty!"
