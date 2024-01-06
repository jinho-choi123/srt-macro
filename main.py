import time

from src.driver import init_driver
from src.login import login
from config import srt_member_number, srt_password
from src.input import get_input
from src.reserve import reserve


driver = init_driver()

# make user choose the departure, arrival, date, time, max_find
departure, arrival, reserve_date, reserve_time, max_find = get_input()

driver = login(driver, srt_member_number, srt_password)

reserve(driver, departure, arrival, reserve_date, reserve_time, max_find)
