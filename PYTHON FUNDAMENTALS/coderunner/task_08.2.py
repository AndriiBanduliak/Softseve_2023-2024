import module

# Setting freezing point and boiling point
module.FREEZING_POINT = 0
module.BOILING_POINT = 100

# Getting temperature input from the user
temperature = float(input())

# Using the module function to print the water state
module.print_water_state(temperature)
