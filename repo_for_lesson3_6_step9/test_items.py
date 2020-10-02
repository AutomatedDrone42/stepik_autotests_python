link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def btn_add_to_basket_is_present(browser):
    browser.get(link)
    is_btn_here = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    assert is_btn_here == "true", "Cannot find add to basket button"
