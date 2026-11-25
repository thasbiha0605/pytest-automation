import pytest
@pytest.mark.testbox
def test_box():
    import time
    from selenium import webdriver
    th = webdriver.Chrome()
    th.get("https://www.techlistic.com/p/selenium-practice-form.html")
    ri = th.find_element("name", "firstname")
    ri.send_keys("thas")
    ri = th.find_element("name", "lastname")
    ri.send_keys("biha")
    ri = th.find_element("xpath", "//*[@id='datepicker']")
    ri.send_keys("12/12/2025")
    time.sleep(3)
import pytest
@pytest.mark.radiobutton
def test_radiobuttton():
    import time
    from selenium import webdriver
    th = webdriver.Chrome()
    th.get("https://www.techlistic.com/p/selenium-practice-form.html")
    ri = th.find_element("xpath", "//*[@id='sex-1']")
    ri.click()
    ri = th.find_element("xpath", "//input[@value='1']")
    ri.click()
    time.sleep(3)
import pytest
@pytest.mark.checkbox
def test_checkbox():
    import time
    from selenium import webdriver
    th = webdriver.Chrome()
    th.get("https://www.techlistic.com/p/selenium-practice-form.html")
    ri = th.find_element("xpath", "//*[@id='profession-1']")
    ri.click()
    ri = th.find_element("xpath", "//*[@id='tool-2']")
    ri.click()
import pytest
@pytest.mark.dropdownbox
def test_dropdownbox():
    import time
    from selenium import webdriver
    th = webdriver.Chrome()
    th.get("https://www.techlistic.com/p/selenium-practice-form.html")
    ri = th.find_element("xpath", "//*[@id='continents']")
    ri.click()
    ri = th.find_element("xpath", "//*[@id='selenium_commands']/option[1]")
    ri.click()
import pytest
@pytest.mark.fileupload
def test_fileupload():
    import time
    from selenium import webdriver
    th = webdriver.Chrome()
    th.get("https://www.techlistic.com/p/selenium-practice-form.html")
    ri = th.find_element("xpath", "//*[@id='photo']")
    ri.send_keys("C:/img1.JPG")
    time.sleep(3)
