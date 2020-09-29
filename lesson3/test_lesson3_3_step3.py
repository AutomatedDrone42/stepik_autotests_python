import pytest
from selenium import webdriver
import time


def link_t(link):
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_xpath("//input[@class='form-control first' and @required]").send_keys("Ivan")
    browser.find_element_by_xpath("//input[@class='form-control second' and @required]").send_keys("Иванов")
    browser.find_element_by_xpath("//input[@class='form-control third' and @required]").send_keys("ivan@mail.ru")
    browser.find_element_by_css_selector("button.btn").click()

    time.sleep(1)
    return browser.find_element_by_tag_name("h1").text


class TestReg:
    def test_reg1(self):
        assert (link_t("http://suninjuly.github.io/registration1.html"),
                "Поздравляем! Вы успешно зарегистировались!", "registration is failed")

    def test_reg2(self):
        assert (link_t("http://suninjuly.github.io/registration2.html"),
                "Поздравляем! Вы успешно зарегистировались!", "registration is failed")

    if __name__ == "__main__":
        pytest.main()
