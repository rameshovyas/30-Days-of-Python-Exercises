# Today is 5 December, 2019. Change this time string to time.
from datetime import datetime

date_string = "5 December, 2019"

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("time_object =", date_object)

