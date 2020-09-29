# Импортировать unittest в файл:
import time
import unittest

# Создать класс, который должен наследоваться от класса TestCase: class TestAbs(unittest.TestCase):
from selenium import webdriver


class TestAbs(unittest.TestCase):
    # Превратить тестовые функции в методы, добавив ссылку на экземпляр класса self
    # в качестве первого аргумента функции: def test_abs1(self):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        input3.send_keys("bebebe@mail.ru")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(str("Congratulations! You have successfully registered!", welcome_text, "Try again"))

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_xpath("//input[@class='form-control first' and @required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//input[@class='form-control third' and @required]")
        input3.send_keys("bebebe@mail.ru")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(str("Congratulations! You have successfully registered!", welcome_text, "Try again"))

    if __name__ == "__main__":
        # Заменить строку запуска программы на unittest.main()
        unittest.main()
