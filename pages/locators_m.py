from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_SUMMARY = (By.CSS_SELECTOR, ".btn-group a")
    VIEW_BASKET_SUMMARY_INV = (By.CSS_SELECTOR, ".btn-group-gr")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # duplicated in Base


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


class BasketPageLocators:
    BASKET_ITEMS_ELEMENT = (By.CSS_SELECTOR, ".basket_summary")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
