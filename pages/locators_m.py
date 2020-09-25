from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SELECTED_ITEM = (By.CSS_SELECTOR, ".product_main h1")
    ADDED_ITEM_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".price_color")
    TOTAL_AMOUNT_BASKET = (By.CSS_SELECTOR, ".basket-mini")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
