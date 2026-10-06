from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")
time.sleep(2)

driver.get("https://www.youtube.com")
time.sleep(2)
# driver.get("https://google.com") 

# driver.execute_script("window.open('https://youtube.com')") #execute script ethu javascript la use pannarathu ethu advance kuda so theva padum pothu tha us pannanum
# driver.close()   # closes google tab

# driver.switch_to.window(driver.window_handles[0])
# print(driver.title)

# driver.quit()

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(2)

driver.quit()
