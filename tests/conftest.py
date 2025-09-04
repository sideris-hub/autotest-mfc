import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    chrome_options = Options()
    
    # chrome_options.add_argument("--headless") 
    
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )
    
    driver.set_window_size(1920, 1080)
    print("Установили размер окна 1920x1080.")
    
    driver.execute_script("document.body.style.zoom='75%'")
    print("Уменьшили масштаб до 75%.")
    
    yield driver
    
    print("\nquit browser..")
    driver.quit()
