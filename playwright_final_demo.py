from datetime import datetime
from playwright.sync_api import sync_playwright

print("Starting the Playwright script...")
print(f"Script started at: {datetime.now()}")

with sync_playwright() as p:
  # Launch with extra args to bypass bot detection / timeouts on weather sites
  browser = p.chromium.launch(
      headless=False,
      args=[
          "--disable-blink-features=AutomationControlled",
          "--start-maximized",
      ],
  )

  # Create a context without passing a fixed viewport so it matches maximized window
  context = browser.new_context(
      no_viewport=True,
      user_agent=(
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
          " like Gecko) Chrome/120.0.0.0 Safari/537.36"
      ),
  )

  page = context.new_page()

  # Navigation with a more relaxed wait condition
  print("Navigating to AccuWeather...")
  page.goto(
      "https://www.accuweather.com/en/in/chennai/206671/hourly-weather-forecast/206671",
      wait_until="commit",
      timeout=60000,
  )

  # Wait for page to be usable
  page.wait_for_load_state("domcontentloaded")
  print(page.title())

  # Handle Cookie Consent if it appears
  try:
    page.click("text=Accept", timeout=5000)
    print("Cookie banner accepted.")
  except:
    print("No cookie banner found or already accepted.")

  page.screenshot(path="full_forecast.png")

  # Typing / Search interaction (if needed)
  try:
    page.fill("input[name='query']", "Chennai")
    page.press("input[name='query']", "Enter")
    page.screenshot(path="search_results.png")
  except Exception as e:
    print(f"Search interaction skipped or handled: {e}")

  # Waiting for elements
  try:
    page.wait_for_selector("text=Chennai, Tamil Nadu", timeout=5000)
    page.screenshot(path="chennai_weather.png")
  except:
    pass

  # Extracting the data
  title = page.title()
  print(f"Page title: {title}")
  browser.close()