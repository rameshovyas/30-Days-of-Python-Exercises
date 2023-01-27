# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. 
# December, January or February,#  the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

month = int(input("Enter month number (1- Jan, .. 12 - Dec : "))
season=""
if(month == 12 or month ==1 or month ==2):
    season ="Winter"
elif (month ==3 or month ==4 or month ==5):
    season ="Spring"    
elif (month ==6 or month ==7 or month ==8):
    season ="Summer"
else : season ="Autum"

print("Welcome %s" % season)
