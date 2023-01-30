# Calculate the time difference between now and new year.
from datetime import datetime

today = datetime.today()
new_year = datetime(2024, 1, 1)
time_left_for_newyear = new_year - today


print('Time left for new year: ', time_left_for_newyear)