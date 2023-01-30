# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output Required
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

new_list = [[item[0].upper(),item[0].upper()[:3],item[1].upper()]  for country in countries for item in country ]
print(new_list)

