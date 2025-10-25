import csv

def main():
    with open('output.csv', mode='r') as file:
        for line in file:
            scuttle_hartest_data = []
            recipes = csv.reader(file)
            recipe_id = 0
            for line in recipes:
                    recipe_id += 1
                    non_ingredient_data = []
                    non_ingredient_data.append(recipe_id)
                    line_count = 0
                    for i in line:
                        line_count += 1
                        if line_count == 4:
                            pass
                        else:
                            non_ingredient_data.append(i)
                    scuttle_hartest_data.append(non_ingredient_data)
            print(scuttle_hartest_data)
            

if __name__=="__main__":
    main()


