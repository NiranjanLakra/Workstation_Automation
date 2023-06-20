from selenium import webdriver
import time

# create an instance of the Edge driver
edge_options = webdriver.EdgeOptions()
edge_options.add_argument("--remote-allow-origins=*")
driver = webdriver.Edge(options=edge_options)

# navigate to the first page
driver.get("https://teams.microsoft.com")

# open a new tab and navigate to the second page
driver.execute_script("window.open('https://outlook.office.com/mail/');")
driver.switch_to.window(driver.window_handles[1])

# perform some actions on the second page
# ...

# switch back to the first page
driver.switch_to.window(driver.window_handles[0])

# navigate to the third page
driver.execute_script("window.open('https://google.com');")

# loop through all open tabs and perform some actions
while 1>0:
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        time.sleep(10)
        # perform some actions on the current tab
        # ...

# close the browser
driver.quit()
