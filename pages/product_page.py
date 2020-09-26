from .base_page import BasePage
from .locators_m import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_msg_added_to_basket(self):
        added_name = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_MESSAGE).text
        item_name = self.browser.find_element(*ProductPageLocators.SELECTED_ITEM).text
        assert added_name == item_name, "Name of item added to basket is wrong! " \
                                        f"EXPECTED: {item_name}, ACTUAL: {added_name}"

    def should_be_total_price_of_basket(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        total_basket = self.browser.find_element(*ProductPageLocators.TOTAL_AMOUNT_BASKET).text
        assert item_price in total_basket, "Total amount is not equal to Cost of added item! " \
                                           f"EXPECTED: {item_price}, ACTUAL: {total_basket}"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message hasn't disappeared, but should!"

    def should_not_be_success_message(self):
        assert self.is_element_not_presented(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be!"
