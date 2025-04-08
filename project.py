from bs4 import BeautifulSoup

with open('amazon_project/data.html') as file:
    data = file.read()

soup = BeautifulSoup(data, 'lxml')

laptops = soup.find_all('div','puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v2kc40w2su09y2pn1beieejnkj s-latency-cf-section puis-card-border')
d = {}
i = 0
for laptop in laptops:
    price = 'Rs ' + laptop.find('span','a-price-whole').text
    name = laptop.find('h2','a-size-medium a-spacing-none a-color-base a-text-normal').span.text
    orig_price = laptop.find('span','a-offscreen').text.replace('â‚¹','Rs ')
    try:
        rating = laptop.find('span','a-icon-alt').text.split()[0]
    except:
        rating = ' - '
    try:
        num_review = laptop.find('span','a-size-base s-underline-text').text
    except:
        num_review = '0'

    d[i] = [name,orig_price,price,rating,num_review]
    i += 1

with open('amazon_project/output.csv','w',encoding = 'utf-8',newline = '') as file:
    import csv
    writer = csv.writer(file)
    writer.writerow(['product','original price','current price','rating','number of reviews'])
    for i in range(len(d)):
        writer.writerow(d[i])
    

    