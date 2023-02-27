from selenium import webdriver

def pytest_html_report_title(report):
    report.title = "Automation Aize"

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)