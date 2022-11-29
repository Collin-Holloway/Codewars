#Create a template string that will insert the country name and population 
pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

template = "The population of {} is {:,.2f} million"

for country in pop_millions:
    name = country[0]
    pop = country[1]
    output = template.format(name, pop)
    print(output)