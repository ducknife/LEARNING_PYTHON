from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Kết nối với Chrome đã mở sẵn
chrome_options = webdriver.ChromeOptions()
chrome_options.debugger_address = "localhost:9222"
driver = webdriver.Chrome(options=chrome_options)

""" #"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\selenium\chrome-profile" """

# Mở tab mới (Facebook)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[-1])
driver.get("https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0")

try:
    # Chờ trang Facebook load hoàn toàn
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print("🔹 Trang Facebook đã load xong!")

    # Nhập email vào ô tìm kiếm
    email = 'mika12@wolke7.net'

    input_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "email"))
    )
    input_box.click()
    input_box.send_keys(email)

    # Nhấn nút "Tìm kiếm"
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Tìm kiếm")] | //button[contains(text(), "Search")]'))
    )
    actions = ActionChains(driver)
    actions.move_to_element(search_button).click().perform()
    print("✅ Đã nhấn nút 'Tìm kiếm' trên Facebook!")

    # Nhấn nút "Tiếp tục" nếu có
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Tiếp tục")] | //button[contains(text(), "Continue")]'))
    )
    actions.move_to_element(continue_button).click().perform()
    print("✅ Đã nhấn nút 'Tiếp tục' trên Facebook!")

except Exception as e:
    print(f"❌ Lỗi trên Facebook: {e}")

# Mở tab mới (Mail.com)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[-1])
driver.get("https://www.mail.com/#.23140-header-navlogin2-1")

try:
    # Chờ trang Mail.com load hoàn toàn
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print("🔹 Trang Mail.com đã load xong!")

    # Nhập email vào ô "Email address"
    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="text" and @placeholder="Email address"]'))
    )
    email_input.click()
    email_input.send_keys(email)

    # Nhập mật khẩu vào ô "Password"
    password = "Meo12345@@"  # 🚨 CẬP NHẬT LẠI PASSWORD CỦA ANH Ở ĐÂY 🚨
    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@type="password" and @placeholder="Password"]'))
    )
    password_input.click()
    password_input.send_keys(password)

    # Nhấn phím Enter sau khi nhập mật khẩu
    password_input.send_keys(Keys.RETURN)
    print("✅ Đã nhấn phím 'Enter' trong ô Password!")

except Exception as e:
    print(f"❌ Lỗi trên Mail.com: {e}")

# Chờ người dùng kiểm tra kết quả
input("Nhấn Enter để thoát...")
driver.quit()
