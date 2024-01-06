from src.search import searchTrain
from selenium.webdriver.common.by import By
from selenium import webdriver
from src.notification import send_notification
from datetime import datetime, timedelta
import time
from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC


def reserve(driver: webdriver, departure, arrival, reserve_date, reserve_time, max_find):
    cnt = 0
    is_reserved = False

    while not is_reserved:
        start_time = time.time()
        cnt = cnt + 1
        print(f'@@{cnt}th cylcle@@')
        print(f'trying to reserve SRT train @{reserve_date} {reserve_time} | {departure} => {arrival}')
        searchTrain(driver, departure, arrival, reserve_date, reserve_time, max_find)
        driver.implicitly_wait(10)
        print("---(#1) %s seconds ---" % (time.time() - start_time))


        for i in range(1, int(max_find)):
            seat_status = driver.find_element(By.CSS_SELECTOR,
                                              f"#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child({i}) > td:nth-child(7)").text
            print("---(#2) %s seconds ---" % (time.time() - start_time))
            try:
                # click reserve button if exists
                driver.find_element(By.XPATH, f"/html/body/div[1]/div[4]/div/div[3]/div[1]/\
                                        form/fieldset/div[6]/table/tbody/tr[{i}]/td[7]/a").click()
                driver.implicitly_wait(10)
                print("---(#3) %s seconds ---" % (time.time() - start_time))
                if driver.find_element(By.ID, 'isFalseGotoMain'):
                    # send message(kakao talk message) to user and make them pay the bill
                    print("Got a ticket. Sending notification...")
                    send_notification("SRT",
                                      f'We got you a ticket. Please pay the bill before {(datetime.now() + timedelta(minutes=10)).strftime("%Y/%m/%d %H:%M:%S")}. '
                                      f'The link is https://etk.srail.kr/hpg/hra/02/selectReservationList.do'
                                      f'?pageId=TK0102010000')
                    is_reserved = True
                    print("---(#4) %s seconds ---" % (time.time() - start_time))
                    break
                else:
                    # somebody took the seat
                    print("---(#4) %s seconds ---" % (time.time() - start_time))
                    print("No seats available... trying to catch the next train")
                    continue
            except UnexpectedAlertPresentException as e:
                print("---(#5) %s seconds ---" % (time.time() - start_time))
                print("alert present...")
                print(e.msg)
                # search again
                searchTrain(driver, departure, arrival, reserve_date, reserve_time, max_find)
                print("Skipping this case...")
                driver.implicitly_wait(10)
                continue
            except NoSuchElementException as e:
                print("---(#5) %s seconds ---" % (time.time() - start_time))
                print("No such element error...")
                print(e.msg)
                # search again
                searchTrain(driver, departure, arrival, reserve_date, reserve_time, max_find)
                print("Skipping this case...")
                driver.implicitly_wait(10)
                continue
        print("---(#6) %s seconds ---" % (time.time() - start_time))
        if not is_reserved:
            print("No seats available. Searching again after 1 seconds")
        print("\n")
        time.sleep(1)

    print("Reservation Success.")
