from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# Optional argument, if not specified will search path.
driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.99acres.com/')

# print(driver.title)
# print(driver.current_url)
print("----------Home Page----------")

driver.find_element_by_xpath("//*[@id='hmcontainer']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='login']/a").click()
time.sleep(2)


print("----------Login Page----------")

time.sleep(3)
username = driver.find_element_by_name('username')
username.send_keys("email_address")


driver.find_element_by_xpath("//*[@id='loginSubmit']").click()
time.sleep(2)
password = driver.find_element_by_name('password')
password.send_keys("Password")

driver.find_element_by_xpath("//*[@id='loginSubmit']").click()
time.sleep(5)


print("----------After Login----------")

n = input("1 for Commerical 0 for Residential: ")
if(n == '1'):
    print("----------Selecting Commercial----------")
    driver.find_element_by_xpath("//*[@id='ComTab']").click()
    time.sleep(5)
    keyword = driver.find_element_by_id('keyword')
    keyword.click()
    driver.find_element_by_xpath("//*[@id='area_lbl']").click()
    print("Do you want to Specify min and Max ")
    mini = int(input("Minimium Area in SqFt: "))
    maxi = int(input("Maximium Area in SqFt: "))
    minEle = driver.find_element_by_id('area_min')
    minEle.send_keys(mini)
    maxEle = driver.find_element_by_id('area_max')
    maxEle.send_keys(maxi)
else:
    print("----------Selecting Residential----------")
    keyword = driver.find_element_by_id('keyword')
    keyword.click()


print("----------Selecting Filters----------")

location = input("Enter the Location: ")
keyword.send_keys(location)

driver.find_element_by_id("submit_query").click()

time.sleep(5)
print("----------Query Search Started----------")
# data = str(driver.find_element_by_class_name("srpTop__tuplesWrap").text)


# print(len(data))
print("Page Number :", 1)
x = 1
time.sleep(7)
try:
    while(1):
        print("Page Number :", x)
        listEle = driver.find_elements_by_class_name("srpTuple__tupleDetails ")
        print("Getting list Data")
        for i in listEle:
            print("-------------Next------------------")
            print(i.text)

        listPhoneNumberEle = driver.find_elements_by_xpath(
            "//span[text()='View Phone Number']")
        for i in listPhoneNumberEle:
            i.click()
            time.sleep(10)
            try:
                print("___________________Try checking button____________-")
                driver.find_element_by_xpath(
                    "//*[@id='recaptcha-anchor']/div[1]").click()
                time.sleep(5)
            except:
                try:
                    driver.find_element_by_xpath("//*[@id='recaptcha-anchor']/div[4]").click()
                except:
                    try:
                        driver.find_element_by_xpath("//*[@id='recaptcha-anchor']/div[3]").click()
                    except:
                        pass
            data = str(driver.find_element_by_class_name(
                "component__details").text)
            print(data)
            time.sleep(3)
            # Closing the Page
            driver.find_element_by_xpath(
                "//i[@class='pageComponent component__eoiLayerCrossBtn']")
            driver.find_element_by_css_selector(
                ".pageComponent.component__eoiLayerCrossBtn").click()
            time.sleep(3)
        driver.find_element_by_link_text("Next Page >").click()
        time.sleep(3)
        x = x+1
        time.sleep(5)
except:
    print("----------Query Completed----------")
time.sleep(3)
driver.close()
driver.quit()
