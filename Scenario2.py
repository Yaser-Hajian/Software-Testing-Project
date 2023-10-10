import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the driver
driver = webdriver.Chrome()
driver.get("http://vu.sbu.ac.ir/class/course.list.php")

# Find the lessons
student_id = driver.find_element(By.CSS_SELECTOR, '#username')
student_id.send_keys("98243084")
time.sleep(3)
input_1 = driver.find_element(By.CSS_SELECTOR, 'body > nav.navbar.navbar-light > form > div > button')
input_1.click()
time.sleep(5)

# select lesson
lesson = driver.find_element(By.CSS_SELECTOR, 'body > div > div.card.bg-light.mb-3 > ul > li:nth-child(4) > a')
lesson.click()
time.sleep(5)

# send username and password
username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
username.send_keys("98243084")
time.sleep(3)
password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys("0312344406")
time.sleep(5)
enter = driver.find_element(By.CSS_SELECTOR, '#loginbtn')
enter.click()
time.sleep(5)

# go to the class
class_link = driver.find_element(By.CSS_SELECTOR, '#module-43747 > div > div > div:nth-child(2) > div > a > span')
class_link.click()
time.sleep(5)

# exit from panel
exit_panel = driver.find_element(By.CSS_SELECTOR, '#action-menu-toggle-0')
exit_panel.click()
time.sleep(3)

# exit from lms
exit_lms = driver.find_element(By.CSS_SELECTOR, '#actionmenuaction-6')
exit_lms.click()
time.sleep(3)


driver.quit()
