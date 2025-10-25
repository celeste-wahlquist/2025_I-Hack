from fractions import Fraction
import re
import csv

def main():
    #takes 'output.csv' and turns it into a 2D Array
    #adapted from code taken by 'geeksforgeeks.org'
    with open('output.csv', mode='r') as file:
        scuttle_harvest_ingredients = []
        recipes = csv.reader(file)
        recipe_id = 0
        for line in recipes:
            if recipe_id == 0:
                recipe_id += 1
            else:
                list_fr_this_time = str_list_to_list_list(line[3])
                for i in list_fr_this_time:
                    #print(recipe_id)
                    scuttle_harvest_ingredients.append(seperate_variables(i, recipe_id))
                recipe_id += 1
    write_to_ingredients(scuttle_harvest_ingredients)
    
#--------------------------------------- Everything that's not MAIN -------------------------------------#

def str_list_to_list_list(str_list):
    str_to_list = []
    new_str = ""
    apostraphy_check = 0
    for i in str_list:
        if i == "[" or i == "]":
            pass
        elif i == "'":
            apostraphy_check += 1
            if apostraphy_check == 2:
                apostraphy_check = 0
                str_to_list.append(new_str)
                new_str = ""
        elif apostraphy_check == 0:
            pass
        else:
            new_str += i
    return(str_to_list)

def seperate_variables(list, recipe_id):
    #all of the variables
    measurement_values = ['tsp','tbsp','cup','pound','pounds','teaspoon','teaspoons','tablespoon','tablespoons']
    split_string = list.split()
    shopping_list = []
    rest_of_list = ""
    the_int_bit = 0
    #crunching the code
    for i in range(len(split_string)):
        if split_string[i].isdigit():
            num = int(split_string[i])
            the_int_bit += num
        elif split_string[i] in measurement_values:
            shopping_list.append(split_string[i])
        elif "/" in split_string[i]:
            the_int_bit += fraction_to_float(split_string[i])
        else:
            rest_of_list += (split_string[i] + " ")
    shopping_list.insert(0, the_int_bit)
    shopping_list.append(rest_of_list)
    return(convert_all_to_cups(shopping_list, recipe_id))

#start section given by ChatGBT
def fraction_to_float(fraction):
    match = re.search(r"\b\d+\s*/\s*\d+\b", fraction)
    fraction_str = match.group()
    decimal_value = float(Fraction(fraction_str))
#end section given by ChatGBT
    return decimal_value

def convert_all_to_cups(shopping_list, recipe_id):
    for i in range(len(shopping_list)):
        unit = shopping_list[0]
        if shopping_list[1] == "teaspoon" or shopping_list[1] == "teaspoons":
            unit = unit * .021
            shopping_list[0] = unit
            shopping_list[1] = "cups"
        elif shopping_list[1] == "tablespoon" or shopping_list[1] == "tablespoons":
            unit = unit * .0625
            shopping_list[0] = unit
            shopping_list[1] = "cups"
        elif shopping_list[1] == "ounce" or shopping_list[1] == "ounces":
            unit = unit * .125
            shopping_list[0] = unit
            shopping_list[1] = "cups"
        #elif shopping_list[1] == "salt":
        #    im_tired = shopping_list[1]

    shopping_list.insert(0, recipe_id)
    return shopping_list

def write_to_ingredients(ingredients_list):
    with open("scuttler_ingredients.csv", "a") as ingredients_file:
        first_line = "'recipe_id', 'measurement', 'unit', 'ingredient'"
        ingredients_file.write(f"{str(first_line)}\n")
        for line in ingredients_list:
            print(f"{line}")

if __name__=="__main__":
    main()
