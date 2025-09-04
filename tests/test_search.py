from pages.main_page import MainPage

def test_positive_search(browser):
    main_page = MainPage(browser)
    
    main_page.perform_search("паспорт")
    
    heading_text = main_page.wait_for_search_results()
    
    assert "РЕЗУЛЬТАТЫ ПОИСКА ПО ЗАПРОСУ" in heading_text
