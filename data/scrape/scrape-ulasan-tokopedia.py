import time
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

'''
TODO
- add rating
- add actual date
- click selengkapnya and get the complete text
'''
url = 'https://www.tokopedia.com/jeteofficialsby/jete-speaker-bluetooth-sm3-surround-sound-with-led-light/review'

name_file = f'data_scrape_{datetime.now().strftime("%Y-%m-%d")}.csv'
try: 
    current_dir = os.getcwd()
    target_dir = os.path.join(current_dir, 'data', 'raw')
    final_path = os.path.normpath(target_dir)
    if not os.path.exists(final_path):
        os.makedirs(final_path)
    csv_path = os.path.join(final_path, name_file)
except Exception as e:
    print(e)
    exit(1)

driver = webdriver.Chrome()
driver.get(url)

for i in range(19) :
    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#zeus-root')))
    
    time.sleep(5)
    
    for j in range(12):
        driver.execute_script('window.scrollBy(0, 250)')
        time.sleep(1)
    driver.execute_script('window.scrollTo(50, 0)')

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    for item in soup.find_all('article', class_='css-15m2bcr'):
        # selengkapnya = driver.find_elements(By.CSS_SELECTOR, 'button.css-89c2tx')
        # print(selengkapnya)
        # for btn in selengkapnya:
        #     try:
        #         driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        #         driver.execute_script("arguments[0].click();", btn)
        #     except Exception as e:
        #         print(e)
        ulasan = item.find('p', class_='css-34x6j7-unf-heading e1qvo2ff8')
        if ulasan is not None:
            ulasan = ulasan.get_text()
        lama = item.find('p',class_='css-1rpz5os-unf-heading e1qvo2ff8')
        if lama is not None:
            lama = lama.get_text()
        nama = item.find('span', class_='name')
        if nama is not None:
            nama = nama.get_text()
        varian = item.find('p', class_='css-5amcmn-unf-heading e1qvo2ff8')
        if varian is not None:
            varian = varian.get_text()
        with open(csv_path, 'a', encoding='utf-8') as f:
            f.write(f'{nama};{lama};{varian};{ulasan}\n')
    next_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Laman berikutnya"]')
    if next_btn.get_attribute('disabled') == 'true':
        break
    next_btn.click()

driver.close()