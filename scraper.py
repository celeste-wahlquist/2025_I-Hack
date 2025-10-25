# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
import openpyxl
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

TARGET_WEBSITES = ["https://www.allrecipes.com/recipe/270750/simple-baked-potato/", "https://www.allrecipes.com/scarborough-fair-roasted-vegetables-recipe-11763940", "https://www.allrecipes.com/cheesy-cauliflower-cakes-recipe-11803145"] # "https://www.recipes.com"
XPATH_INDEX = {"total-time": '//*[@id="mm-recipes-details_1-0"]/div[1]/div[3]/div[2]', "ingredients": '//*[@id="mm-recipes-structured-ingredients_1-0"]/ul/li', "servings": '//*[@id="mm-recipes-details_1-0"]/div[1]/div[4]/div[2]'}
COLUMNS = ["link", "meal-category", "ingredients", "total-time", "servings"]
# TODO: Get all needed data {url, name, category, rating, ingredients, prep_time, cook_time, ready_in_time, calories}

# Create the driver for the selenium browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# TODO: Make dynamic webpage crawling within target websites base url.
# //*[@id="mntl-taxonomy-nodes__list_1-0"]
# The above is the xml path to the list of different dinner genres
# blank_data = {"link": None, "meal_category": None, "ingredients": None}
df = pd.DataFrame(columns=COLUMNS)
# Category: Things like breakfast, dinner, side dish, and dessert


# Make the get into a reusable function
def get_url(url):
    driver.get(url)
"""# Get an element by Xpath, specifically the list of meal types
# food_types = driver.find_elements(By.XPATH, '//*[@id="mntl-taxonomy-nodes__list_1-0"]')
# print(food_types)
# food_types_list = []

# for food_type in range(len(food_types)):
#    food_types_list.append(food_types[food_type].text)

# print(food_types_list)
"""

def get_element_by_xpath(xpath):
    """This returns a dictionary containing a list."""
    element = list(driver.find_elements(By.XPATH, xpath))
    # if (function != None):
        # Add a function application 
    element_dict = {"element":[]}
    for element in element:
        print(element.text)
        element_dict["element"].append(element.text)
    return element_dict
# print(ingredients)

# print(ingredients[0].tag_name)

# print(ingredients_list)

df = pd.DataFrame(columns=COLUMNS)

# get_url(TARGET_WEBSITES[0])
# element = get_element_by_xpath(XPATH_INDEX["ingredients"]) # Returns a dictionary containing a list of data.
# print(element)




for url in TARGET_WEBSITES:
    # for key in XPATH_INDEX:
    sleep(2)
    get_url(url)
    ingredients_dict = get_element_by_xpath(XPATH_INDEX["ingredients"])
    total_time_dict = get_element_by_xpath(XPATH_INDEX["total-time"])
    serving_dict = get_element_by_xpath(XPATH_INDEX["servings"])
    temp_df = pd.DataFrame({"link":url, "meal-category":"side-dish", "ingredients":ingredients_dict, "total-time": total_time_dict, "servings": serving_dict}) #TODO: Clean up the ingredients list.
    df = pd.concat([df, temp_df])

# d94427
# print(df)
df.to_csv("./output.csv")



# temp_df = pd.DataFrame([{"link":TARGET_WEBSITES[0], "meal_category":"side-dish", "ingredients": "test string"}])
# df["ingredients"] = zip(ingredients_list)
# df.loc[(len(df))] = [temp_df]
# pd.concat([df, temp_df])
# print(df)
# This input keeps the page alive
# input()
driver.quit()
