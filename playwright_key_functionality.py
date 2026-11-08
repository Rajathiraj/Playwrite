from playwright.sync_api import sync_playwright
'''
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://google.com", wait_until="domcontentloaded")
    page.screenshot(path="google.png")
    print(page.title())
    browser.close()
'''

    browser = sync_playwright().chromium.launch(headless=False)
    page=browser.new_page()
    #Navigation
    page.goto("https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671", wait_until="domcontentloaded")
    page.screenshot(path="accuweather.png")
    print(page.title())

    #Clicking
    page.click ("text=Hourly")
    page.screenshot(path="full_forecast.png")

    #Typing
    page.fill("input[name='query']", "Chennai")
    page.press("input[name='query']", "Enter")
    page.screenshot(path="search_results.png")

    #waiting for elements
    page.wait_for_selector("text=Chennai, Tamil Nadu")
    page.screenshot(path="chennai_weather.png")

    #Extracting the data
    title = page.title()
    print(f"Page title: {title}")
    browser.close()