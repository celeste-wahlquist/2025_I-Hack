# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
import openpyxl

TARGET_WEBSITES = ["https://www.allrecipes.com/recipe/270750/simple-baked-potato/"] # "https://www.recipes.com"

# Create the driver for the selenium browser
driver = webdriver.Chrome()

# //*[@id="mntl-taxonomy-nodes__list_1-0"]
# The above is the xml path to the list of different dinner genres
# blank_data = {"link": None, "meal_category": None, "ingredients": None}
df = pd.DataFrame(columns=["link", "meal_category", "ingredients"])
# Category: Things like breakfast, dinner, side dish, and dessert



driver.get(TARGET_WEBSITES[0])
"""# Get an element by Xpath, specifically the list of meal types
# food_types = driver.find_elements(By.XPATH, '//*[@id="mntl-taxonomy-nodes__list_1-0"]')
# print(food_types)
# food_types_list = []

# for food_type in range(len(food_types)):
#    food_types_list.append(food_types[food_type].text)

# print(food_types_list)
"""

sleep(2)
ingredients = list(driver.find_elements(By.XPATH, '//*[@id="mm-recipes-structured-ingredients_1-0"]/ul/li'))
# print(ingredients)

# print(ingredients[0].tag_name)
ingredients_dict = {"ingredient":[]}
for ingredient in ingredients:
    print(ingredient.text)
    ingredients_dict["ingredient"].append(ingredient.text)
# print(ingredients_list)
temp_df = pd.DataFrame({"link":TARGET_WEBSITES[0], "meal_category":"side-dish", "ingredients":ingredients_dict}) #TODO: Clean up the ingredients list.

print("Here")
print(temp_df)
with pd.ExcelWriter("./output.xlsx") as writer:
    temp_df.to_excel(writer)

# temp_df = pd.DataFrame([{"link":TARGET_WEBSITES[0], "meal_category":"side-dish", "ingredients": "test string"}])
# df["ingredients"] = zip(ingredients_list)
# df.loc[(len(df))] = [temp_df]
# pd.concat([df, temp_df])
print(df)
# This input keeps the page alive
input()
driver.quit()
