import pytest
from fake_useragent import UserAgent
from selenium import webdriver
from selenium_stealth import stealth


@pytest.fixture
def browser():
    useragent = UserAgent()
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  браузер без интерфейса
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("start-maximized")
    options.add_argument(f"user-agent={useragent.random}")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')
    options.add_argument('--disable-blink-features=AutomationControlled')

    browser = webdriver.Chrome(options=options)
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
                      const newProto = navigator.__proto__
                      delete newProto.webdriver
                      navigator.__proto__ = newProto
                      """
    })
    stealth(browser,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    link = 'https://www.citilink.ru/'
    browser.get(link)
    return browser
