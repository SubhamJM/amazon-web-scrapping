from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
text = 'laptop'
data = ''

for page in range(1,51):
    driver.get(f'https://www.amazon.in/s?k={text}&page=3&crid=3D4SMYD9MXB1B&qid=1744084925&sprefix=laptop%2Caps%2C296&xpid=JHjOOchaurm-0&ref=sr_pg_{page}')
    elems = driver.find_elements(By.CLASS_NAME, 'puis-card-container')
    for elem in elems:
        data += elem.get_attribute('outerHTML')

with open('amazon_project/data.html','w',encoding='utf-8') as file:
    file.write(data)

driver.close()