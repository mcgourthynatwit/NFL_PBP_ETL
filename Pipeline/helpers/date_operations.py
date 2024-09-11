import pandas as pd 

# Determines the week of the games played by the row date. 
# Earliest game of a week is thursday and that week ends the following Monday
# Used by: split_games.py
def get_week(dates):
    week_numbers = {}
    week_num = 1

    # Initialize week_start to the Thursday before the first game
    week_start = dates[0] - pd.Timedelta(days=(dates[0].weekday() + 4) % 7)

    for date in dates:
        # Check if we need to start a new week
        if date - week_start >= pd.Timedelta(days=7):  
            week_num += 1
            week_start = date - pd.Timedelta(days=(date.weekday() + 4) % 7)  # Adjust to the new Thursday

        date_str = date.strftime('%Y-%m-%d')
        week_numbers[date_str] = week_num

    return week_numbers