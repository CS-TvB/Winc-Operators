# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
spain_language = 'spanish'
zwitzerland_language = 'swiss-german'
spain_religion = 'roman chatolic'
zwitzerland_religion = 'roman chatolic'
spain_capitol = 'madrid'
zwitzerland_capitol = 'bern'
spain_GPD = 1.95
zwitzerland_GPD = 1.11
pop_growth_spain = 0.13
pop_growth_zwitzerland = 0.65
pop_count_spain = 47163418
pop_count_zwitzerland = 8508698

print(spain_language == zwitzerland_language)
print(spain_religion == zwitzerland_religion)
print(len(spain_capitol) != len(zwitzerland_capitol))
print(zwitzerland_GPD >= spain_GPD)
print(pop_growth_spain <=1.0 and pop_growth_zwitzerland <= 1.0)
print(pop_count_spain > 10000000 or pop_count_zwitzerland > 10000000)
print(pop_count_spain > 10000000 and pop_count_zwitzerland < 10000000 or pop_count_spain < 10000000 and pop_count_zwitzerland > 10000000)
