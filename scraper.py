# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
import openpyxl
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import urllib.parse

TARGET_WEBSITES = ["https://www.allrecipes.com/recipe/270750/simple-baked-potato/", "https://www.allrecipes.com/scarborough-fair-roasted-vegetables-recipe-11763940", "https://www.allrecipes.com/cheesy-cauliflower-cakes-recipe-11803145", "https://www.allrecipes.com/4-ingredient-egg-avocado-toast-recipe-11763246"] # "https://www.recipes.com"
target_websites = """https://www.allrecipes.com/recipe/222399/smoked-salmon-dill-eggs-benedict
https://www.allrecipes.com/recipe/214713/potato-salad-deviled-eggs
https://www.allrecipes.com/recipe/81473/garlic-asparagus-with-lime
https://www.allrecipes.com/recipe/242379/lemon-pepper-rubbed-back-ribs
https://www.allrecipes.com/recipe/286162/cheesy-lemon-chicken-pasta
https://www.allrecipes.com/recipe/55151/ravioli-soup
https://www.allrecipes.com/recipe/165527/black-beans-and-pork-chops
https://www.allrecipes.com/recipe/186699/buffalo-chicken-chili
https://www.allrecipes.com/recipe/268320/hoisin-ginger-sesame-pork-chops
https://www.allrecipes.com/recipe/66326/great-grandma-johns-pasties
https://www.allrecipes.com/recipe/220538/ham-and-potato-casserole
https://www.allrecipes.com/recipe/39374/easy-grilled-tri-tip
https://www.allrecipes.com/recipe/8400743/air-fryer-calzones
https://www.allrecipes.com/recipe/268768/meyer-lemon-cream-sauce-for-salmon
https://www.allrecipes.com/recipe/276644/jack-frost-cocktails
https://www.allrecipes.com/recipe/286303/bacon-and-leek-quiche
https://www.allrecipes.com/recipe/222540/thirty-minute-baked-tuna-burgers
https://www.allrecipes.com/recipe/233254/grilled-sea-bass-with-chili-lime-dressing
https://www.allrecipes.com/recipe/76187/spiced-balsamic-vinaigrette
https://www.allrecipes.com/recipe/256678/caribbean-sorrel-tea
https://www.allrecipes.com/recipe/72114/chicken-souvlaki-gyro-style
https://www.allrecipes.com/recipe/230324/moist-turkey-burgers
https://www.allrecipes.com/recipe/221980/liberian-style-collard-greens
https://www.allrecipes.com/recipe/241035/gerrys-margarita
https://www.allrecipes.com/recipe/11782/smoked-salmon-alfredo-sauce
https://www.allrecipes.com/recipe/237251/malaguena-lemon-and-dill-vinaigrette
https://www.allrecipes.com/recipe/259609/apple-crisp-topping
https://www.allrecipes.com/recipe/240639/struffoli
https://www.allrecipes.com/recipe/12101/grandmas-butterscotch-pie
https://www.allrecipes.com/recipe/239753/nutella-stuffed-french-toast
https://www.allrecipes.com/recipe/278437/instant-pot-shrimp-risotto-with-peas
https://www.allrecipes.com/recipe/229965/october-oatmeal-pumpkin-muffins
https://www.allrecipes.com/recipe/265322/coxinhas-brazilian-chicken-croquettes
https://www.allrecipes.com/recipe/274344/feta-brined-chicken-breasts
https://www.allrecipes.com/recipe/232526/bobs-little-known-less-cared-about-chili
https://www.allrecipes.com/recipe/239704/potato-leek-and-spinach-soup
https://www.allrecipes.com/recipe/8531314/three-cheese-ham-involtini
https://www.allrecipes.com/recipe/220340/kellys-slow-cooker-beef-mushroom-and-barley-soup
https://www.allrecipes.com/recipe/89710/creamy-tomato-basil-soup
https://www.allrecipes.com/recipe/218928/easy-egg-white-omelet
https://www.allrecipes.com/recipe/206817/delicious-stuffed-potato-pancakes
https://www.allrecipes.com/recipe/95736/vegetarian-refried-beans
https://www.allrecipes.com/recipe/270234/purple-carrot-soup
https://www.allrecipes.com/recipe/165470/asparagus-with-garlic-and-onions
https://www.allrecipes.com/recipe/76791/creole-black-eyed-peas-and-rice
https://www.allrecipes.com/recipe/282179/jamaican-oxtail-stew
https://www.allrecipes.com/recipe/158794/roberts-homemade-italian-sausage
https://www.allrecipes.com/recipe/228233/spicy-white-chili-with-chicken
https://www.allrecipes.com/recipe/174713/graham-crusted-pork-chops
https://www.allrecipes.com/recipe/246646/kalbi-ribs
https://www.allrecipes.com/recipe/265681/vegan-udon-noodles-soup-with-tofu-and-vegetables
https://www.allrecipes.com/recipe/216436/low-fat-banana-bread
https://www.allrecipes.com/recipe/174559/sourdough-scones
https://www.allrecipes.com/recipe/246288/the-best-panna-cotta-you-will-ever-have
https://www.allrecipes.com/recipe/280661/homemade-strawberry-vinegar
https://www.allrecipes.com/recipe/83716/veggie-vegetarian-chili
https://www.allrecipes.com/recipe/223203/orzo-and-chicken-stuffed-peppers
https://www.allrecipes.com/recipe/231256/homemade-pickling-spice
https://www.allrecipes.com/recipe/246885/chocolate-cherry-peanut-butter-smoothie
https://www.allrecipes.com/recipe/277479/microwave-cashew-brittle
https://www.allrecipes.com/recipe/143466/hot-chicken-wing-dip
https://www.allrecipes.com/recipe/270858/roasted-butternut-and-black-bean-enchiladas
https://www.allrecipes.com/recipe/6811/panettone-i
https://www.allrecipes.com/recipe/15821/aunt-teens-creamy-chocolate-fudge
https://www.allrecipes.com/recipe/246066/salmon-en-croute
https://www.allrecipes.com/recipe/237764/lemon-basil-quinoa-salad
https://www.allrecipes.com/recipe/260803/blueberry-pierogi
https://www.allrecipes.com/recipe/274047/homemade-marshmallow-bald-eagles
https://www.allrecipes.com/recipe/221158/grad-cap-cookies
https://www.allrecipes.com/recipe/240380/chili-nachos
https://www.allrecipes.com/recipe/71146/garlic-corn-on-the-cob
https://www.allrecipes.com/recipe/49266/cathys-amazing-fish-chowder
https://www.allrecipes.com/recipe/269471/mini-buffalo-chicken-egg-rolls
https://www.allrecipes.com/recipe/267967/low-carb-stuffed-peppers
https://www.allrecipes.com/recipe/166417/filipino-spaghetti
https://www.allrecipes.com/recipe/247311/texan-chicken-and-rice-casserole
https://www.allrecipes.com/recipe/22786/lemon-pepper-dill-fish
https://www.allrecipes.com/recipe/261773/cheesy-bacon-slider-bake
https://www.allrecipes.com/recipe/218328/easy-turkey-chili
https://www.allrecipes.com/recipe/255688/elsies-baked-mac-and-cheese
https://www.allrecipes.com/recipe/214718/mushroom-and-spinach-ravioli-with-chive-butter-sauce
https://www.allrecipes.com/recipe/239898/no-yolks-chicken-noodle-soup
https://www.allrecipes.com/recipe/270269/ms-angelas-smothered-cabbage
https://www.allrecipes.com/recipe/236577/tortellini-in-chicken-broth
https://www.allrecipes.com/recipe/282410/baked-fish-with-frozen-vegetables
https://www.allrecipes.com/recipe/112095/roasted-beet-peach-and-goat-cheese-salad
https://www.allrecipes.com/recipe/25467/ham-and-pineapple-kabobs
https://www.allrecipes.com/recipe/189935/frizzled-onions
https://www.allrecipes.com/recipe/231942/southern-butter-beans
https://www.allrecipes.com/recipe/286043/cheesy-chicken-florentine-casserole
https://www.allrecipes.com/recipe/263059/easter-chocolate-eggs-made-with-a-mold
https://www.allrecipes.com/recipe/221181/fiesta-corn-tortilla-pizzas
https://www.allrecipes.com/recipe/89549/best-apple-salad
https://www.allrecipes.com/recipe/261309/quick-and-easy-parmesan-zucchini-fries
https://www.allrecipes.com/recipe/241626/cha-cha-chicken
https://www.allrecipes.com/recipe/104975/easy-german-bierocks-runza
https://www.allrecipes.com/recipe/230463/white-chocolate-thumbprint-cookies
https://www.allrecipes.com/recipe/15370/cauliflower-cheese-pie
https://www.allrecipes.com/recipe/221074/black-bean-and-cucumber-salad
https://www.allrecipes.com/recipe/13840/creamed-peas-and-onions
https://www.allrecipes.com/recipe/238919/stacked-tomato-and-burrata-salad
https://www.allrecipes.com/recipe/23420/spicy-crispy-beef
https://www.allrecipes.com/recipe/20019/swordfish-a-la-siciliana
https://www.allrecipes.com/recipe/8455770/sous-vide-prime-rib
https://www.allrecipes.com/recipe/268087/pressure-cooker-paella-with-chicken-thighs-and-smoked-sausage
https://www.allrecipes.com/recipe/279214/instant-pot-lebanese-lentil-soup-shorbat-adas
https://www.allrecipes.com/recipe/230548/vickis-tangerine-martini
https://www.allrecipes.com/recipe/256165/boeuf-bourguignon
https://www.allrecipes.com/recipe/279525/sourdough-rosemary-crackers
https://www.allrecipes.com/recipe/283791/crispy-rolled-breakfast-burrito
https://www.allrecipes.com/recipe/266996/brazilian-chicken-salad-salpicao-de-frango
https://www.allrecipes.com/recipe/278322/celery-soup
https://www.allrecipes.com/recipe/172445/lengua-beef-tongue-stew
https://www.allrecipes.com/recipe/283472/grilled-lobster-tails-with-garlic-butter""".split("\n")



XPATH_INDEX = {"total-time": '//*[@id="mm-recipes-details_1-0"]/div[1]/div[3]/div[2]', "ingredients": '//*[@id="mm-recipes-structured-ingredients_1-0"]/ul/li', "servings": '//*[@id="mm-recipes-details_1-0"]/div[1]/div[4]/div[2]', "meal-category":'//*[@id="mntl-breadcrumbs__item_2-0"]', "cook-time": '//*[@id="mm-recipes-details_1-0"]/div[1]/div[2]/div[2]', "prep-time": '//*[@id="mm-recipes-details_1-0"]/div[1]/div[1]/div[2]'}
COLUMNS = ["link", "meal-category", "ingredients", "total-time", "servings", "cook-time", "prep-time"]
SITEMAPS = ["https://www.allrecipes.com/sitemap_1.xml", "https://www.allrecipes.com/sitemap_2.xml", "https://www.allrecipes.com/sitemap_3.xml", "https://www.allrecipes.com/sitemap_4.xml"]


ROW_IDENTIFIER = "row"

# Create the driver for the selenium browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

df = pd.DataFrame(columns=COLUMNS)


# Make the get into a reusable function
def get_url(url):
    driver.get(url)

def get_elements_by_xpath(xpath):
    """This returns a dictionary containing a list with the captured data in that list."""
    elements = list(driver.find_elements(By.XPATH, xpath))
    element_dict = {ROW_IDENTIFIER: []}
    for element in elements:
        element_dict[ROW_IDENTIFIER].append(element.text)
    return element_dict

df = pd.DataFrame(columns=COLUMNS)

def get_target_urls(sitemap_url):
    driver.get(sitemap_url)

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, "xml")

    urls = soup.find_all("loc")

    urls_list = []
    for url in urls:
        clean_url = str(url.contents)[2:-3] # 2:-3 removes brackets and single quotes.
        parsed = urllib.parse.urlparse(str(clean_url))
        # special_url =f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        if (parsed.path[0:8] == "/recipe/"):
            print(clean_url)
            urls_list.append(clean_url)
    return urls_list

def fill_blank_df_fields(df):
    """Run this function on a newly created df to fill empty columns"""
    print(df)
    for column in COLUMNS:
        # print(df[column][ROW_IDENTIFIER])
        if(len(df[column][ROW_IDENTIFIER]) == 0):
            print(f"{column} has an empty entry")
            df.loc[ROW_IDENTIFIER, column] = [None]
    return df

for sitemap in SITEMAPS:
    target_websites = get_target_urls(sitemap)
# driver.close()
# if (len(target_websites) > 20):
    # target_websites = target_websites[0:20]
for url in target_websites:
    # sleep(2)  # This rate limits the calls to the server.
    get_url(url)
    ingredients_dict = get_elements_by_xpath(XPATH_INDEX["ingredients"])
    total_time_dict = get_elements_by_xpath(XPATH_INDEX["total-time"])
    cook_time_dict = get_elements_by_xpath(XPATH_INDEX["cook-time"])
    prep_time_dict = get_elements_by_xpath(XPATH_INDEX["prep-time"])
    serving_dict = get_elements_by_xpath(XPATH_INDEX["servings"])
    meal_category = get_elements_by_xpath(XPATH_INDEX["meal-category"]) 
    temp_df = pd.DataFrame({"link":url, "meal-category":meal_category, "ingredients":ingredients_dict, "total-time": total_time_dict, "servings":serving_dict, "cook-time": cook_time_dict, "prep-time": prep_time_dict}) #TODO: Clean up the ingredients list. There is currently a mismatch in columns filled here and the expected columns.
    # for each of the element dictionaries, I need to check if it is empty and fill it with None if empty
    temp_df = fill_blank_df_fields(temp_df)
    df = pd.concat([df, temp_df], ignore_index=True)

df.to_csv("./output.csv")

driver.close()
driver.quit()
