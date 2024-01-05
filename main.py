import time

from src.driver import init_driver
from src.login import login
from src.search import searchTrain
from selenium.webdriver.common.by import By
from config import srt_member_number, srt_password, departure, arrival, reserve_date, reserve_time, max_find
from src.notification import send_notification
from datetime import datetime, timedelta

driver = init_driver()

login(driver, srt_member_number, srt_password)

isReserved = False

while not isReserved:
    train_list = searchTrain(driver, departure, arrival, reserve_date, reserve_time, max_find)

    for i in range(1, int(max_find)):
        seat_status = driver.find_element(By.CSS_SELECTOR,
                                          f"#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child({i}) > td:nth-child(7)").text

        if "예약하기" in seat_status:
            driver.find_element(By.XPATH, f"/html/body/div[1]/div[4]/div/div[3]/div[1]/\
                        form/fieldset/div[6]/table/tbody/tr[{i}]/td[7]/a/span").click()
            driver.implicitly_wait(3)

            if driver.find_elements(By.ID, 'isFalseGotoMain'):
                isReserved = True
                # send message(kakao talk message) to user and make them pay the bill
                send_notification("SRT", f'We got you a ticket. Please pay the bill before {(datetime.now() + timedelta(minutes = 10)).strftime("%Y/%m/%d %H:%M:%S")}. '
                                         f'The link is https://etk.srail.kr/hpg/hra/02/selectReservationList.do'
                                         f'?pageId=TK0102010000')
                print("Reservation Success.")
                break
            else:
                # somebody took the seat
                print("Somebody took the seat... trying to catch the next train")
                continue

    if not isReserved:
        print("No seats available. Searching again after 1 seconds")
    time.sleep(1)
