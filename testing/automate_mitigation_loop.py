from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

# === CONFIGURATION ===
DASHBOARD_URL = "http://127.0.0.1:5000/"
CHECK_INTERVAL_SECONDS = 30

# === SETUP CHROME DRIVER (VISIBLE BROWSER) ===
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")  # Big enough for everything visible
# options.add_argument("--headless")  # Uncomment if you want headless mode

driver = webdriver.Chrome(options=options)

# Track already mitigated IPs
mitigated_ips = set()

try:
    while True:
        print("[*] Loading dashboard...")
        driver.get(DASHBOARD_URL)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "table"))
        )

        # Grab malicious IPs
        malicious_rows = driver.find_elements(
            By.XPATH,
            "//div[contains(@class, 'border-danger')]//table//tbody//tr"
        )

        new_ips = []
        for row in malicious_rows:
            ip_cell = row.find_element(By.XPATH, ".//td[1]")
            ip = ip_cell.text.strip()
            if ip not in mitigated_ips:
                new_ips.append(ip)

        print(f"[*] Found {len(new_ips)} new IP(s): {new_ips}")

        for ip in new_ips:
            try:
                print(f"[>] Blocking IP: {ip}")
                ip_input = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.ID, "ip_address"))
                )
                ip_input.clear()
                ip_input.send_keys(ip)

                action_select = Select(driver.find_element(By.ID, "action"))
                action_select.select_by_value("block")

                submit_btn = driver.find_element(
                    By.XPATH, "//form[@id='mitigation-form']//button[@type='submit']"
                )
                submit_btn.click()

                # Wait for success alert
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))
                )

                mitigated_ips.add(ip)
                print(f"[✔] Blocked: {ip}")
                time.sleep(1)

            except Exception as ip_error:
                print(f"[!] Failed to mitigate {ip}: {ip_error}")

        print(f"[✓] Waiting {CHECK_INTERVAL_SECONDS} seconds...\n")
        time.sleep(CHECK_INTERVAL_SECONDS)

except KeyboardInterrupt:
    print("\n[!] Stopped by user.")
except Exception as e:
    print(f"[!] Unhandled Error: {e}")
finally:
    driver.quit()

print("[✓] Automation completed.")
