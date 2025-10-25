# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
import openpyxl
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

TARGET_WEBSITES = ["https://www.allrecipes.com/recipe/270750/simple-baked-potato/", "https://www.allrecipes.com/scarborough-fair-roasted-vegetables-recipe-11763940"] # "https://www.recipes.com"

# Create the driver for the selenium browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# //*[@id="mntl-taxonomy-nodes__list_1-0"]
# The above is the xml path to the list of different dinner genres
# blank_data = {"link": None, "meal_category": None, "ingredients": None}
df = pd.DataFrame(columns=["link", "meal-category", "ingredients"])
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

def get_ingredients(xpath):
    ingredients = list(driver.find_elements(By.XPATH, xpath))
    ingredients_dict = {"ingredient":[]}
    for ingredient in ingredients:
        print(ingredient.text)
        ingredients_dict["ingredient"].append(ingredient.text)
    return ingredients_dict
# print(ingredients)

# print(ingredients[0].tag_name)

# print(ingredients_list)

df = pd.DataFrame(columns=["link", "meal-category", "ingredients"])

for url in TARGET_WEBSITES:
    sleep(2)
    get_url(url)
    ingredients_dict = get_ingredients('//*[@id="mm-recipes-structured-ingredients_1-0"]/ul/li')
    temp_df = pd.DataFrame({"link":url, "meal-category":"side-dish", "ingredients":ingredients_dict}) #TODO: Clean up the ingredients list.
    df = pd.concat([df, temp_df])

print(df)
df.to_csv("./output.csv")

# temp_df = pd.DataFrame([{"link":TARGET_WEBSITES[0], "meal_category":"side-dish", "ingredients": "test string"}])
# df["ingredients"] = zip(ingredients_list)
# df.loc[(len(df))] = [temp_df]
# pd.concat([df, temp_df])
# print(df)
# This input keeps the page alive
input()
driver.quit()
