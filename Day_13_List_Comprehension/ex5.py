# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

new_list = [
            {'country' : item[0].upper(), 'city' : item[1].upper()}
            for country in countries
            for item in country
]

print(new_list)