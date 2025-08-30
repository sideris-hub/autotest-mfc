# pages/main_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    # Нам нужен только локатор поля ввода и заголовка результатов
    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_RESULTS_HEADING = (By.TAG_NAME, "h1")

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def open(self):
        """Открывает главную страницу."""
        self.browser.get("https://e-mfc.ru/" )

    def search_for(self, text):
        """
        Просто ждет, пока поле ввода станет видимым, и вводит текст.
        """
        # Ждем, пока поле ввода станет просто ВИДИМЫМ
        search_input = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        
        search_input.clear()
        search_input.send_keys(text)
        search_input.submit()

    def get_results_heading_text(self):
        """
        Ждет появления заголовка на странице результатов и возвращает его текст.
        """
        heading = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_RESULTS_HEADING)
        )
        return heading.text
