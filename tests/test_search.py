from pages.main_page import MainPage

def test_positive_search(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.search_for("паспорт")
    
    heading_text = main_page.get_results_heading_text()
    assert "Результаты поиска" in heading_text
