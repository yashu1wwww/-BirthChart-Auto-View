from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.astrosage.com/freekphorary/instantchart.asp")

input=driver.find_element_by_xpath('//*[@id="Name"]')
input.send_keys('darshan')

input=driver.find_element_by_xpath('//*[@id="roundborder"]/div[3]/div[1]/form/fieldset/div[1]/div[2]/div/label[1]')
input.click()

input=driver.find_element_by_xpath('//*[@id="Day"]')
input.send_keys('16')

input=driver.find_element_by_xpath('//*[@id="Month"]')
input.send_keys('04')

input=driver.find_element_by_xpath('//*[@id="Year"]')
input.send_keys('1977')

input=driver.find_element_by_xpath('//*[@id="Hrs"]')
input.send_keys('07')

input=driver.find_element_by_xpath('//*[@id="Min"]')
input.send_keys('30')

input=driver.find_element_by_xpath('//*[@id="Sec"]')
input.send_keys('00')

input=driver.find_element_by_xpath('//*[@id="place"]')
input.send_keys('mysore')

input=driver.find_element_by_xpath('//*[@id="submit"]')
input.click()























