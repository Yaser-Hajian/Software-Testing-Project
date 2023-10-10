import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep


# Set up the driver
driver = webdriver.Chrome()
driver.get("https://www.alibaba.ir/")
sleep(2)

# select foreign flight
foreign_flight = driver.find_element(By.CSS_SELECTOR, '#app > div.wrapper.bg-white > main > div > div.a-container.px-0.pb-8 > div.a-card.products-box > div.products-box__tabs > ul > li:nth-child(2) > a')
foreign_flight.click()
time.sleep(2)

# select source and destination
source = driver.find_element(By.CSS_SELECTOR, '#app > div.bg-white.wrapper > main > div > div.a-container.px-0.pb-8 > div.a-card.products-box > div.tab-view.z-10 > div > form > div.flex.w-full.justify-center > div:nth-child(1) > div > div > div.a-input.is-first.is-lg > label')
source.click()
time.sleep(2)
source_city = driver.find_element(By.CSS_SELECTOR, '#app > div.bg-white.wrapper > main > div > div.a-container.px-0.pb-8 > div.a-card.products-box > div.tab-view.z-10 > div > form > div.flex.w-full.justify-center > div:nth-child(1) > div > div.v-dropdown.pretty-scroll.is-open > div > ul > li:nth-child(2) > a')
source_city.click()
time.sleep(2)

destination = driver.find_element(By.CSS_SELECTOR, '#app > div.bg-white.wrapper > main > div > div.a-container.px-0.pb-8 > div.a-card.products-box > div.tab-view.z-10 > div > form > div.flex.w-full.justify-center > div:nth-child(1) > div > div.a-input-group.is-horizontal.relative.mb-0 > div.a-input.is-last.is-lg > label')
destination.click()
time.sleep(2)
destination_city = driver.find_element(By.CSS_SELECTOR, '#app > div.bg-white.wrapper > main > div > div.a-container.px-0.pb-8 > div.a-card.products-box > div.tab-view.z-10 > div > form > div.flex.w-full.justify-center > div:nth-child(1) > div > div.v-dropdown.pretty-scroll.is-open > div > ul > li:nth-child(3) > a')
destination_city.click()
time.sleep(2)

# choose date
date = driver.find_element(By.CSS_SELECTOR, '#app > div.bg-white.wrapper > main > div > div.a-container.px-0.pb-8 > div.a-card.products-box > div.tab-view.z-10 > div > form > div.flex.w-full.justify-center > div.relative > div > div > div.a-input.is-first.is-lg > label')
date.click()
time.sleep(2)
date_day = driver.find_element(By.CSS_SELECTOR, '#app > div.bg-white.wrapper > main > div > div.a-container.px-0.pb-8 > div.a-card.products-box > div.tab-view.z-10 > div > form > div.flex.w-full.justify-center > div.relative > div > div.v-dropdown.pretty-scroll.is-open > div > div.a-card__body.relative > div > div > div.datepicker-slide.lg\:-mx-2 > div:nth-child(2) > div > span:nth-child(25) > span')
date_day.click()
time.sleep(2)

# select one trip
one_trip = driver.find_element(By.CSS_SELECTOR, '#app > div.bg-white.wrapper > main > div > div.a-container.px-0.pb-8 > div.a-card.products-box > div.tab-view.z-10 > div > form > div.flex.w-full.items-stretch.justify-start.mb-5 > span:nth-child(1) > button')
one_trip.click()
time.sleep(2)
one_trip_confirm = driver.find_element(By.CSS_SELECTOR, '#app > div.bg-white.wrapper > main > div > div.a-container.px-0.pb-8 > div.a-card.products-box > div.tab-view.z-10 > div > form > div.flex.w-full.items-stretch.justify-start.mb-5 > span:nth-child(1) > div > div > ul > li:nth-child(1) > a')
one_trip_confirm.click()
time.sleep(2)

# search flight
search = driver.find_element(By.CSS_SELECTOR, '#app > div.bg-white.wrapper > main > div > div.a-container.px-0.pb-8 > div.a-card.products-box > div.tab-view.z-10 > div > form > div.flex.w-full.justify-center > div:nth-child(4) > button')
search.click()
time.sleep(15)

# non-stop flight
nonstop = driver.find_element(By.CSS_SELECTOR, '#app > div.wrapper > main > div > div.layout-sidebar__main > aside > div > div > div:nth-child(3) > div > details > div > div > label:nth-child(2)')
nonstop.click()
time.sleep(5)

# flight detail
detail = driver.find_element(By.CSS_SELECTOR, '#app > div.wrapper > main > div > div.layout-sidebar__main > section > div:nth-child(4) > div:nth-child(1) > div > div.available-card__action.flex.justify-center.items-center > div > div:nth-child(3) > div > button')
detail.click()
time.sleep(5)

# costs = []
# flight_no = []
# content = driver.page_source
# bs = BeautifulSoup(content, 'html.parser')
# cost = bs.find('div', attrs={'class': 'available-card__action flex flex-col'})
# flight_number = bs.find('div', attrs={'class': 'tab-view mt-px pretty-scroll'})
# if cost.find('div', attrs={'class': 'flex items-center justify-between w-full'}) is None:
#     lcost = cost.find_all('strong', attrs={'class': 'text-secondary-400 font-bold text-4'})
#     costs.append(lcost)
#
# if flight_number.find('span', attrs={'class': 'a-label is-sm mr-2'}) is None:
#     lflight_number = flight_number.find_all('span', attrs={'class': 'class="font-en-number mr-1"'})
#     flight_no.append(lflight_number)
#
# print(len(costs))
# print("------------------")
# print(len(flight_no))
