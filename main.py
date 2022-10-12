import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
while True:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    actions = ActionChains(driver)

    driver.get("https://www.surveymonkey.com/r/TLRLWFX")
    driver.find_element(By.ID, "73167207_587792648").send_keys("All future simulcast titles")
    driver.find_element(By.ID, "73167207-ok").click()
    time.sleep(1)
    driver.find_element(By.ID, "73167518_599500068_label").click()

    actions.send_keys(Keys.TAB)
    actions.perform()
    time.sleep(1)

    #driver.find_element(By.ID, "question-title-73167652").click()
    driver.find_element(By.ID, "73167652").send_keys("Germany, Austria, Switzerland")
    #driver.execute_script('document.querySelector("textarea.question-title-73167652").innerText = "wefwefwef"')
    driver.find_element(By.ID, "73167652-ok").click()
    time.sleep(1)
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    driver.quit()