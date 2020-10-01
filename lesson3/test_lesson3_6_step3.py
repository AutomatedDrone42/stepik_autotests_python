import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('ufo', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_ufo_messages_collector(browser, ufo):
    link = f'https://stepik.org/lesson/{ufo}/step/1'
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.find_element_by_class_name("textarea.string-quiz__textarea.ember-text-area.ember-view").send_keys(
        str(answer))
    browser.find_element_by_class_name("submit-submission").click()
    message = browser.find_element_by_class_name("smart-hints__hint")
    assert "Correct!" in message.text, message.text
