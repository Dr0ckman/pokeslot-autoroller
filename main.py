from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import getpass


print("This data is used automatically passed to Discord. Nothing is stored. \n"
      "Actually, check the source code, lol\n")

print("I'm not validating your dumb credentials because it's too much work. "
      "\nSo type them correctly the first time or this whole thing will break c:\n")

USERNAME = input("Discord E-mail: ")
PASSWORD = input("Discord Password: ")
SERVER = "" # Copy and paste the discord channel URL where you want to roll here

sched = BlockingScheduler()
@sched.scheduled_job('interval', minutes=120, next_run_time=datetime.now())
def timed_job():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--silent")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")
    options.add_argument("--mute-audio")
    driver = webdriver.Chrome(options=options)
    driver.get(SERVER)

    print("\nLogging to Discord with your dumb credentials...")

    email_box = driver.find_element_by_name('email')
    email_box.send_keys(USERNAME)
    email_box.send_keys(Keys.TAB)

    password_box = driver.find_element_by_name('password')
    password_box.send_keys(PASSWORD)
    password_box.send_keys(Keys.RETURN)

    print("Waiting for stuff to load. Meanwhile, did you know that potatoes are a bulb?")

    time.sleep(10)

    try:
        actions = ActionChains(driver)
        actions.send_keys('$p')
        actions.send_keys(Keys.RETURN)
        actions.perform()
        print("\nThere. Check Discord to see if it worked.\nLeave this thing open, it will do $p every 2 hours.")
        driver.quit()
    except:
        driver.quit()


sched.start()



