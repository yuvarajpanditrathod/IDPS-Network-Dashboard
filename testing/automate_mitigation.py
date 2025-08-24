from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

# === CONFIGURATION ===
DASHBOARD_URL = "http://127.0.0.1:5000/"  # Change if hosted on a different address

# === SETUP SELENIUM DRIVER (NO PATH NEEDED) ===
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Remove this line to see the browser window
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

try:
    # Step 1: Open the dashboard
    driver.get(DASHBOARD_URL)

    # Wait for malicious IP table to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "table"))
    )

    # Step 2: Get all malicious IPs
    print("[*] Extracting malicious IPs...")
    malicious_rows = driver.find_elements(
        By.XPATH,
        "//div[contains(@class, 'border-danger')]//table//tbody//tr"
    )
    malicious_ips = []
    for row in malicious_rows:
        ip_cell = row.find_element(By.XPATH, ".//td[1]")
        ip = ip_cell.text.strip()
        malicious_ips.append(ip)

    print(f"[*] Found {len(malicious_ips)} malicious IPs: {malicious_ips}")

    # Step 3: Submit each IP to the mitigation form with 'block' action
    for ip in malicious_ips:
        print(f"[>] Mitigating IP: {ip}")

        # Fill in the form
        ip_input = driver.find_element(By.ID, "ip_address")
        ip_input.clear()
        ip_input.send_keys(ip)

        action_select = Select(driver.find_element(By.ID, "action"))
        action_select.select_by_value("block")

        # Submit form
        submit_btn = driver.find_element(
            By.XPATH, "//form[@id='mitigation-form']//button[@type='submit']"
        )
        submit_btn.click()

        # Wait for success alert
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))
        )

        print(f"[✔] Successfully mitigated {ip}")

        # Optional: reload page for updates
        driver.refresh()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "table"))
        )
        time.sleep(1)

    print("[✓] All malicious IPs have been mitigated.")

except Exception as e:
    print(f"[!] Error occurred: {e}")

finally:
    driver.quit()

print("[✓] Automation completed.")