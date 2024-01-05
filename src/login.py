from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By


## login using driver
def login(driver: webdriver, member_number, password):
    # goto login page
    driver.get('https://etk.srail.co.kr/cmc/01/selectLoginForm.do')
    driver.implicitly_wait(15)

    # 회원번호 매핑
    driver.find_element(By.ID, 'srchDvNm01').send_keys(member_number)

    # 비밀번호 매핑
    driver.find_element(By.ID, 'hmpgPwdCphd01').send_keys(password)

    driver.find_element(By.XPATH, '/html/body/div/div[4]/div/div[2]/form/\
        fieldset/div[1]/div[1]/div[2]/div/div[2]/input').click()
    driver.implicitly_wait(5)
