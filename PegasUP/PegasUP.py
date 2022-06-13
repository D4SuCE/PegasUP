from selenium import webdriver
from datetime import datetime
from creds import login, password
import time

def connect():
    url = f"https://pegas.bsu.edu.ru/login/index.php"
    options = webdriver.ChromeOptions()

    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36")
    options.add_argument("--start-maximized");

    driver = webdriver.Chrome(
        executable_path="chromedriver.exe",
        options=options
    )
    driver.get(url=url)
    time.sleep(2)
    try:
        username = driver.find_element_by_id("username")
        username.clear()
        username.send_keys(login)
        passwd = driver.find_element_by_id("password")
        passwd.clear()
        passwd.send_keys(password)
        driver.find_element_by_id("loginbtn").click()
        time.sleep(2)
        url = f"https://pegas.bsu.edu.ru/mod/bigbluebuttonbn/view.php?id=1174432"
        driver.get(url=url)
        driver.find_element_by_id("join_button_input").click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
        driver.find_element_by_xpath("//button[@aria-label='Listen only']").click()
        time.sleep(2)
        message = driver.find_element_by_id("message-input")
        message.clear()
        message.send_keys("Доброе утро")
        driver.find_element_by_xpath("//button[@aria-label='Send message']").click()
        while (True):
            if (getTime() == (13, 45)):
                driver.close()
                driver.quit()
                break

    except Exception as ex:
        print("-----------------------------------------")
        print(f"Exception: {ex}")
        print("-----------------------------------------")
        driver.close()
        driver.quit()
        exit()  

def getTime():
    now = datetime.now()
    hours = now.hour
    minutes = now.minute
    return hours, minutes

def main():
    while (True):
        if (getTime() == (22, 53)):
            connect()
            break

if __name__ == "__main__":
    main()