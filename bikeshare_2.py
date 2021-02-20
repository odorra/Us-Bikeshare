import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city_list = ['Chicago','NY City','Washington']
month_list = ['All','January','February','March','April','May','June']
day_list = ['All','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_input, month_input, day_input = False, False, False
    while True:
        if not city_input:
            city = input("Please choose a city from Chicago, NY City or Washington: ")
            city = city.title()
            if city not in city_list:
                print("This city is not included in this query. Please choose Chicago, NY City or Washington:")
                continue
            else:
                city_input = True

    # get user input for month (all, january, february, ... , june)
        if not month_input:
            month = input("Please choose a month from January, February, March, April, May or June or All: ")
            month = month.title()
            if month not in month_list:
                print("This month is not included in this query. Please choose January, February, March, April, May or June or All:")
                continue
            else:
                month_input = True
    # get user input for day of week (all, monday, tuesday, ... sunday)
        if not day_input:
            day = input("Please choose a day of the week  (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday): ")
            day = day.title()
            if day not in day_list:
                print("This day is not included in this query. Please choose All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday:")
                continue
            else:
                break
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    start_time = time.time()
    print ("Please wait while data is being loaded")
    df = pd.read_csv(CITY_DATA.get(city), parse_dates = ["Start Time", "End Time"])
    df["Start Month"] = df["Start Time"].dt.month_name()
    df["Start Day"] = df["Start Time"].dt.day_name()
    df["Start Hour"] = df["Start Time"].dt.hour()
    if month != "All":
        df = df[df["Start Month"] == month]
    if day != "All":
        df = df[df["Start Day"] == day]
    print("Here We Go!")
    print("The code takes {} seconds.".format(round((time.time() - start_time),2)))
    return df
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == "All":
        most_common_month = df["Start Month"].dropna()
        if most_common_month.empty:
            print("No common months. Please reenter data")
        else:
            most_common_month = most_common_month.mode()[0]
            print("Most common month is: {}".format(most_common_month))

    else:
        print("Select All to get the most common month instead of{}".format(month))

    # display the most common day of week
    if day == "All":
        most_common_day = df["Start Day"].dropna()
        if most_common_day.empty:
            print("No common days. Please reenter data")
        else:
            most_common_day = most_common_day.mode()[0]
            print("Most common day is: {}".format(most_common_day))

    else:
            print("Select All to get the most common day instead of{}".format(day))

    # display the most common start hour
    most_common_hour = df["Start Hour"].dropna()
    if most_common_hour.empty:
        print("No common hour. Please reenter data")
    else:
        most_common_hour = most_common_hour.mode()[0]
        print("Most common hour is: {}".format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df["Start Station"]
    if most_common_start_station.empty:
        print("Data has no start station, so please refilter it.")
    else:
        most_common_start_station = most_common_start_station.mode()[0]
        print("Most common start station is{}".format(most_common_start_station))

    # display most commonly used end station
    most_common_end_station = df["End Station"]
    if most_common_end_station.empty:
        print("Data has no end station, so please refilter it.")
    else:
        most_common_end_station = most_common_end_station.mode()[0]
        print("Most common end station is{}".format(most_common_end_station))

    # display most frequent combination of start station and end station trip
    most_common_start_and_end_station = df["Start Station", "End Station"]
    if most_common_start_and_end_station.empty:
        print("Data has no start station, so please refilter it.")
    else:
        most_common_start_and_end_station = (most_common_start_and_end_station.groupby(["Start Station", "End Station"]).size().sort_values(ascending = False))
        trips = most_common_start_and_end_station.iloc[0]
        stations = most_common_start_and_end_station[most_common_start_and_end_station == trips].index[0]
        start_station, end_station = stations
        print("Most common start station is {} and end station is {} and part of the trips {}".format(start_station, end_station, trips))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time = df["Trip Duration"].dropna()
    if travel_time.empty:
        print("No entry")
    else:
        total_travel_time = valid.time.sum()
        print("Total travel time is {}".format(total_travel_time))

    # display mean travel time
    mean_travel_time = travel_time.mean()
    print("Mean travel time is {}".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df["User Type"].dropna()
    if user_type.empty:
        print("Please revisit your data!")
    else:
        user_type = user_type.value_counts()
        print("User type count is {}".format(user_type))

    # Display counts of gender
    user_gender = df["Gender"].dropna()
    if user_gender.empty:
        print("Please revisit your data!")
    else:
        user_gender = user_gender.value_counts()
        print("User gender count is {}".format(user_gender))

    # Display earliest, most recent, and most common year of birth
    user_births = df["User Birth Year"].dropna()
    if user_births.empty:
        print("Please revisit your data!")
    else:
        user_birth = df["User Birth Year"].dropna()
        if user_birth.empty:
            print("Please revisit your data!")
        else:
            earliest_birth = user_birth.min()
            print("Earliest birth year is {}".format(earliest_birth)) 
            latest_birth = user_birth.min()
            print("Most Recent birth year is {}".format(latest_birth))  
            most_common_birth_year = user_birth.mode()[0]
            print("Most common birth year is {}".format(most_common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()