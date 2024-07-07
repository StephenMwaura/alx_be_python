from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    print(current_date)
    return current_date

# display_current_datetime()

number_of_days = int(input("Enter the  number of days to add to the current date: "))
def calculate_future_date():
    current_date = display_current_datetime()
    future_date = current_date + timedelta(days=number_of_days)
    date = "%Y-%m-%d %H:%M:%S"
    format_date = future_date.strftime(date)
    return format_date

calculate_future_date()