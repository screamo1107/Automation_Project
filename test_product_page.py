from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket_1(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_msg_added_to_basket()
    page.should_be_total_price_of_basket()


# Same test with another item to ensure the implementation is independent
def test_guest_can_add_product_to_basket_2(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_msg_added_to_basket()
    page.should_be_total_price_of_basket()
