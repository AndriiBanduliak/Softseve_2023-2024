import re

data = ["id,name,population,is_capital",
        "3024,juba,284324",
        "3025,galya,23735",
        "3026,mexico city,23423555",
        "3027,santiago,1342381",
        "3028,lusaka,1742973",
        "4900,tel aviv,4324355",
        "6600,al fujayrah,97320"]

def max_population(data):
    max_pop = 0
    max_location = ""
    for entry in data[1:]:  # Skip the header
        match = re.search(r'(\d+),([^,]+),(\d+)', entry)
        if match:
            population = int(match.group(3))
            if population > max_pop:
                max_pop = population
                max_location = match.group(2)
    return max_location, max_pop

#print(max_population(data))
