from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)
    return current_date

# display_current_datetime()
    


number_of_days = int(input("Enter the number of days to be add to the current date: "))

def calculate_future_date():
    current_date = display_current_datetime()
    future_date = current_date + timedelta(days=number_of_days)
    formatted_future_date= future_date.strftime("%Y-%m-%d")
    
    print("Future date", formatted_future_date)
    return formatted_future_date
calculate_future_date()

def main():
    display_current_datetime()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date()

if __name__ =="__main__":
    main()
      