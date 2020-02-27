import pygal
from die import Die


# Create two dies with 6 sides (i.e. a D6)
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_number in range(10000):
    result = die_1.roll_the_dice() + die_2.roll_the_dice()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.sides + die_2.sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
histogram = pygal.Bar()

histogram.title = "Results of rolling two D6 dice 10000 times."
histogram.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
histogram._x_title = "Results"
histogram._y_title = "Frequency of result"

histogram.add('D6 + D6', frequencies)
histogram.render_to_file('die_visual.svg')