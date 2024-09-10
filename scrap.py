from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chrome_service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(service=chrome_service(ChromeDriverManager().install()))

driver.get("https://bullsconnect.usf.edu/events?topic_tags=7276307")

time.sleep(5)


event_items = driver.find_elements(By.CLASS_NAME,"list-group-item")


with open("content.txt","w") as f:
    for item in event_items:
        f.write(item.next)


