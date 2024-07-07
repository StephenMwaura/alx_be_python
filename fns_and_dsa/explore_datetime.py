from datetime import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    print(current_date)
    return current_date

# display_current_datetime()

number_of_days = int(input("Enter a number of days: "))
def calculate_future_date():
    current_date = display_current_datetime()
    future_date = current_date + datetime.timedelta(days=number_of_days)
    print(future_date)

calculate_future_date()