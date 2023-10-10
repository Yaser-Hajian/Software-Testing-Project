from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from tqdm import tqdm
import numpy as np

url = "https://torob.com/browse/99/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D9%88-%D9%86%D9%88%D8%AA-%D8%A8%D9%88%DA%A9-laptop/"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
sleep(60)

products = []
stock_status = []
links = []
prices = []
brands = []

content = driver.page_source
bs = BeautifulSoup(content, 'html.parser')
for a in bs.findAll('a', href=True):
    if a.find('div', attrs={'class': 'filter-brand-item'}) is not None:
        brand = a.find_all('div', attrs={'class': 'filter-brand-item'})
        brands.append(brand[0].text.lower())
        brands.append(brand[1].text.lower())

    if a.find('h2', attrs={'class': 'product-name'}) is not None:
        product = a.find('h2', attrs={'class': 'product-name'})
        status = a.find('div', attrs={'class': 'badge'})
        price = a.find('div', attrs={'class': 'product-price-text'})
        link = 'https://torob.com' + a['href']
        products.append(product.text.lower())
        if status is not None:
            stock_status.append(1)
        else:
            stock_status.append(0)
        links.append(link)
        prices.append(price.text)
brands.extend(['مک بوک ایر',
               'macbook air',
               'مک بوک پرو',
               'macbook pro'])
brand = []
weight = []
cpu_series = []
cpu_model = []
cache = []
ram = []
memory = []
size = []
ram_title = ['حافظه رم (Ram)',
             'حافظه رم',
             'ظرفیت حافظه RAM',
             'مقدار حافظه رم',
             'ظرفیت حافظه RAM',
             'مقدار حافظه رم',
             'ظرفیت حافظه ی رم',
             'میزان حافظه رم'
             ]
memory_title = ['ظرفیت حافظه داخلی',
                'ظرفیت SSD',
                'ظرفیت حافظه HDD',
                'ظرفیت حافظه SSD',
                'حافظه خشک(SSD)',
                'حافظه مکانیکی(HDD)',
                'ظرفیت HDD',
                'هارد دیسک'
                ]

for pr in products:
    b = False
    for br in brands:
        if br in pr and not b:
            b = True
            brand.append(br)
            break
    if not b:
        brand.append(np.nan)

print('brand:', len(brand))
print('first 10 brand: ', brand[:10])
option = webdriver.ChromeOptions()
option.add_argument('--headless')
for link in tqdm(links):
    driver = webdriver.Chrome(options=option)
    driver.get(link)
    content = driver.page_source
    bs = BeautifulSoup(content, 'html.parser')
    specification = bs.find('div', attrs={'class': 'specs-content'})
    if specification.find('div', attrs={'class': 'no-specs'}) is None:
        titles = specification.find_all('div', attrs={'class': 'detail-title'})
        values = specification.find_all('div', attrs={'class': 'detail-value'})
        w = False
        c = False
        cp = False
        ca = False
        s = False
        r = False
        m = False
        for title, value in zip(titles, values):
            if title.text.find('وزن') != -1 and not w:
                w = True
                weight.append(value.text)
            elif title.text == 'سری پردازنده' and not c:
                c = True
                cpu_series.append(value.text)
            elif title.text == 'مدل پردازنده' and not cp:
                cp = True
                cpu_model.append(value.text)
            elif (title.text.find('حافظه کش') != -1 or title.text.find('Cache') != -1) and not ca:
                ca = True
                cache.append(value.text)
            elif (title.text.find('اینچ') != -1 or value.text.find('اینچ') != -1) and not s:
                s = True
                size.append(value.text)
            elif title.text in ram_title and not r:
                r = True
                ram.append(value.text)
            elif title.text in memory_title and not m:
                if value.text != 'ندارد':
                    m = True
                    memory.append(value.text)
        if not w:
            weight.append(np.nan)
        if not c:
            cpu_series.append(np.nan)
        if not cp:
            cpu_model.append(np.nan)
        if not ca:
            cache.append(np.nan)
        if not s:
            size.append(np.nan)
        if not r:
            ram.append(np.nan)
        if not m:
            memory.append(np.nan)
    else:
        weight.append(np.nan)
        cpu_series.append(np.nan)
        cpu_model.append(np.nan)
        cache.append(np.nan)
        size.append(np.nan)
        ram.append(np.nan)
        memory.append(np.nan)
print('weight:', len(weight))
print('cpu:', len(cpu_series))
print('cpu:', len(cpu_model))
print('cache:', len(cache))
print('ram:', len(ram))
print('memory:', len(memory))
print('size:', len(size))

df1 = pd.DataFrame({'product': products, 'stock_status': stock_status, 'prices': prices})
df1.to_csv('data.csv', index=False, encoding='utf-8')

df2 = pd.DataFrame({'product': products, 'Link': links})
df2.to_csv('links.csv', index=False, encoding='utf-8')

df3 = pd.DataFrame(
    {'Brand': brand, 'Weight': weight, 'CPU Series': cpu_series, 'CPU Model': cpu_model, 'Cache': cache, 'RAM': ram,
     'Memory': memory, 'Size': size, 'Stock_statu': stock_status, 'Price': prices})
df3.to_csv('specdata.csv', index=False, encoding='utf-8')