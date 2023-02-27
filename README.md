# AutomationAize
 
**Introduction:**

A quick note on how to download and set up the necessary software to start using Selenium 4 with Python, PyCharm Code Editor with pytest framework dependencies and is intended for Windows operating system.

**Prerequisites:**

1. Python 3.6 or above
2. Pip (Python Package Manager)
3. Chrome/Firefox browser (depending on the browser you want to automate)
4. JDK (Java Development Kit) 8 or above
 
**Download and install Selenium 4:**

1. Open a command prompt/terminal window
2. Type the following command: pip install selenium==4.0.0
3. Press Enter to download and install Selenium 4

**Download and install PyCharm Code Editor:**

1. Go to https://www.jetbrains.com/pycharm/download/
2. Click on "Download" button for the "Community" version
3. Install the downloaded file by following the prompts

**Installing pytest Framework Dependencies:**

1. Open a command prompt/terminal window
2. Type the following command: pip install pytest
3. Press Enter to download and install pytest framework dependencies

**Download and install WebDriver modules:**

1. Go to the following URLs to download the appropriate driver for your browser:
for an instance,Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
2. Extract the downloaded file to a location on your computer
3. Add the location of the extracted file to your system's PATH environment variable.

**Pytest Framework:**

pytest framework has been used to write tests for the web application and the same can be viewed in test_automation.py module.

**Reports Generation:**

Simple html reports have been used to generate reports using commands -v --html=report.html

**Commands to run the tests:**

1. Open terminal/command prompt 
2. Execute:pytest test_automation.py or 
3. Execute with report: pytest -v --html=report.html.
