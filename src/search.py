from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



## search train list for given condition
def searchTrain(driver: webdriver, departure, arrival, date, time, max_find):
    driver.get('https://etk.srail.kr/hpg/hra/01/selectScheduleList.do')
    driver.implicitly_wait(10)

    dep_stn = driver.find_element(By.ID, 'dptRsStnCdNm')
    dep_stn.clear()
    dep_stn.send_keys(departure)

    arr_stn = driver.find_element(By.ID, 'arvRsStnCdNm')
    arr_stn.clear()
    arr_stn.send_keys(arrival)

    Select(driver.find_element(By.ID, "dptDt")).select_by_value(date)
    Select(driver.find_element(By.ID, "dptTm")).select_by_visible_text(time)

    driver.find_element(By.XPATH, "//input[@value='조회하기']").click()
    driver.implicitly_wait(5)

    train_list = driver.find_elements(By.CSS_SELECTOR, "#result-form > fieldset > \
    div.tbl_wrap.th_thead > table > tbody > tr")

    return train_list
