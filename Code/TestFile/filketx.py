from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 设置Edge WebDriver路径
driver_path = 'C:\\WebDriver\\bin\\msedgedriver.exe'

# 初始化Edge WebDriver
driver = webdriver.Edge(executable_path=driver_path)

# 目标网站的URL
url = 'https://www.todaybing.com/'

# 打开网页
driver.get(url)

# 等待覆盖元素出现并点击它
try:
    overlay = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'overlay'))
    )
    overlay.click()
except Exception as e:
    print(f"An error occurred while clicking the overlay: {e}")
    driver.quit()
    exit()

# 等待按钮元素出现并点击它
try:
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'btn.btn-blue.text-left.mb-2.btn-dl'))
    )
    button.click()
except Exception as e:
    print(f"An error occurred while clicking the download button: {e}")
    driver.quit()
    exit()

# 等待下载完成（这里需要根据实际情况调整等待时间）
time.sleep(5)

# 关闭浏览器
driver.quit()