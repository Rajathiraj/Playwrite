from datetime import datetime
from playwright.sync_api import sync_playwright

print("Starting the Playwright script...")
print(f"Script started at: {datetime.now()}")

with sync_playwright() as p:
  # Launch browser in headed mode so you can watch it work
  browser = p.chromium.launch(headless=False)
  page = browser.new_page()

  # Navigate to Cricbuzz
  page.goto("https://www.cricbuzz.com/")

  # Wait for the score element dynamically (replace selector with your inspected selector)
  # Example: page.wait_for_selector("your_inspected_selector_here")
  # For demonstration based on your task structure:
  print("Waiting for live score element...")
  # page.wait_for_selector(".cb-min-hdcb") # Example selector pattern

  # Extracting the live score text
  # score = page.inner_text(".cb-min-hdcb")
  # print(score)

  # Save screenshot
  page.screenshot(path="score.png")
  print("Saved score.png")

  browser.close()