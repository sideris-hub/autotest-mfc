def test_open_main_page_and_check_title(browser):
    browser.get("https://e-mfc.ru/" )
    assert "Единый портал" in browser.title
