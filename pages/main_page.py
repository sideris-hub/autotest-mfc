from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    HTML_TAG = (By.TAG_NAME, "html")
    SEARCH_ICON_AREA = (By.CSS_SELECTOR, "div.search__trigger")
    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_RESULTS_HEADING = (By.CSS_SELECTOR, "h2.page-header__title")

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 15)


    def perform_search(self, text):
        self.browser.get("https://e-mfc.ru/" )
        print("Шаг 1: Сайт открыт.")
    
        try:
            self.browser.implicitly_wait(1)
            root_element = self.wait.until(EC.element_to_be_clickable(self.HTML_TAG))
            root_element.click()
            print("Шаг 2: Кликнули по фону.")
        except Exception:
            print("Шаг 2: Всплывающее окно не появилось.")

        search_area = self.wait.until(EC.element_to_be_clickable(self.SEARCH_ICON_AREA))
        search_area.click()
        print("Шаг 3: Кликнули на иконку лупы.")

        search_input = self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT))
        search_input.clear()
        search_input.send_keys(text)
        print(f"Шаг 4: Ввели текст '{text}'.")

        search_input.submit()
        print("Шаг 5: Нажали Enter.")

    def wait_for_search_results(self):
        heading = self.wait.until(EC.visibility_of_element_located(self.SEARCH_RESULTS_HEADING))
        print("Шаг 6: Результаты поиска загрузились.")
        return heading.text
