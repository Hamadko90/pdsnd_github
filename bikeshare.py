import time
import pandas as pd
import numpy as np
import statistics as st


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nWhich city do you want to see its data chicago, new york city, washington. \n").lower()
        if city in CITY_DATA:
            break
        else:
            print('Invalid input, try again!')


    # TO DO: get user input for month (all, january, february, ... , june)
    MONTHS = ["january", "february", "march", "april", "may", "june", "all"]
    while True:
        month = input("\nPlease enter a month to filtter the results by month or type all for all months. (e.g january, february, march, april, may, june). \n").lower()
        if month in MONTHS:
            break
        else:
            print('Invalid input, try again!')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
    while True:
        day = input("\nPlease enter a day to filtter the results by day or type all for all days. (e.g monday, tuesday, wednesday, thursday, friday, saturday, sunday). \n").lower()
        if day in DAYS:
            break
        else:
            print('Invalid input, try again!')



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
    #use pandas library to read the csv files
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

    if month != 'all':
        month = MONTHS.index(month)

        df = df.loc[df['month'] == month]

 # filter by day of week if applicable

    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if day != 'all':

        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    start_time = time.time()
    # TO DO: display the most common month
    MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

    common_month = df['month'].mode()[0]
    print("The most common month is: " + MONTHS[common_month].title())

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is: " + common_day_of_week)




    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is: " + str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most common used start station is: " + common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most common used end station is: " + common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station is: " + str(frequent_combination.split("||")))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is: " + str(total_travel_time))



    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time is: " + str(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""


    print('\nCalculating User Stats...\n')

    start_time = time.time()
    # TO DO: Display counts of user types
    users = df['User Type'].str.count('User').sum()
    customers = df['User Type'].str.count('Customer').sum()
    print('\nCount of users are {}\n'.format(users))
    print('\nCount of customers are {}\n'.format(customers))


    # TO DO: Display counts of gender
    if('Gender' in df):
     gender = df['Gender'].value_counts()
     print("The Count user gender is: \n" + str(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
        earliest_birth = df ['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print('Earliest year of birth is: {}\n'.format(earliest_birth))
        print('Recent year of birth is: {}\n'.format(recent_birth))
        print('Most common year of birth is {}\n'.format(common_birth))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nDo you want to view next 5 rows of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
