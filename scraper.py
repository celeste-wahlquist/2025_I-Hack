# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

TARGET_WEBSITES = ["https://www.allrecipes.com/recipe/270750/simple-baked-potato/"] # "https://www.recipes.com"

# Create the driver for the selenium browser
driver = webdriver.Chrome()

# //*[@id="mntl-taxonomy-nodes__list_1-0"]
# The above is the xml path to the list of different dinner genres



driver.get(TARGET_WEBSITES[0])
"""# Get an element by Xpath, specifically the list of meal types
# food_types = driver.find_elements(By.XPATH, '//*[@id="mntl-taxonomy-nodes__list_1-0"]')
# print(food_types)
# food_types_list = []

# for food_type in range(len(food_types)):
#    food_types_list.append(food_types[food_type].text)

# print(food_types_list)
"""


# This input keeps the page alive
input()
driver.quit()