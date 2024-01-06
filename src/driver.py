from selenium import webdriver

## Initialize Chrome Driver

def init_driver():
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    opt.add_argument('--no-sandbox')
    opt.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    return driver