
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 

tiktok_email = ''
tiktok_pass = ''

#options Chrom
options = webdriver.ChromeOptions()
try:
    #user-agent
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51")
    #Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/23.0 Mobile/15E148 Safari/605.1.15

#for ChromeDriver version 79.0.3945.16 or over
    options.add_argument("--disable-blink-features=AutomationControlled")
    print("User-agent success")

except Exception as e:
    print(f"Error!\n{e}")

#headless mode
#options.headless = True

driver = webdriver.Chrome(
    executable_path="/chromdriver/chromedriver", 
    options=options)

