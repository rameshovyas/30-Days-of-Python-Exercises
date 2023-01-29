# Write a function called check-season, it takes a month parameter and returns the season:
# Autumn, Winter, Spring or Summer.

def check_season(month):
    season=""
    if(month == 12 or month ==1 or month ==2):
        season ="Winter"
    elif (month ==3 or month ==4 or month ==5):
        season ="Spring"    
    elif (month ==6 or month ==7 or month ==8):
        season ="Summer"
    else : season ="Autum"

    return season

print(check_season(12))

