
def assert_text_on_page(driver, text_to_find):
    base_qa_page = driver.find_element_by_tag_name("body")
    all_text_on_page = base_qa_page.text
    assert text_to_find in all_text_on_page

