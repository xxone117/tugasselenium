from selenium import webdriver
from time import sleep

url = [
    "https://www.tiket.com/",
    "https://www.tokopedia.com/",
    "https://www.orangsiber.com/",
    "https://idejongkok.com/",
    "https://kelasotomesyen.com/"
]

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)

for urls in url:
    driver.get(urls)
    sleep(3)
    title = driver.title
    print(f"Link : {urls} - {title}")
driver.close()
