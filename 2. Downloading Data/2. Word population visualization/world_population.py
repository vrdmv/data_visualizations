import json
from pygal_maps_world.maps import World
from country_codes import get_country_code
from pygal.style import RotateStyle, LightColorizedStyle

# Load the data into a list.
filename = 'population_data.json'
with open(filename) as file_object:
    population_data = json.load(file_object)

# Print the 2010 population for each country.
cc_populations = {}
for population_dict in population_data:
    if population_dict['Year'] == '2010':
        country_name = population_dict['Country Name']
        population = int(float(population_dict['Value']))
        code = get_country_code(country_name)
        if code: #not empty, thus True (i.e. it found the country code)
            cc_populations[code] = population

# Group the countries into 3 population levels.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop


wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')
            