from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import options, driver, tiktok_email, tiktok_pass
import pickle
import time

def tiktok_auth(url):
    driver.get(url=url)
    time.sleep(10)
    #driver.find_element_by_class_name("login-button").click
    driver.find_element_by_xpath("//button[text()='Войти']").click()
    time.sleep(5)
    iframe = driver.find_element_by_xpath("//iframe[@class='jsx-2041920090']")
    time.sleep(5)
    driver.switch_to.frame(iframe)
    time.sleep(5)
    driver.find_element_by_xpath("//div[text()='Введите телефон / почту / имя пользователя']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//a[@class='link-2j8GS']").click()
    time.sleep(5)

    email_input = driver.find_element_by_name("email")
    email_input.clear()
    email_input.send_keys(tiktok_email)
    time.sleep(5)

    password_input = driver.find_element_by_name("password")
    password_input.clear()
    password_input.send_keys(tiktok_pass)
    time.sleep(3)
    password_input.send_keys(Keys.ENTER)
    time.sleep(10)

    pickle.dump(driver.get_cookies(), open(f"{tiktok_email}_cookies", "wb"))


def main():
    tiktok_auth("https://tiktok.com")

if __name__ == '__main__':
    main()