
import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new York City': 'new_york_city.csv',
             'washington': 'washington.csv'}


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

    citys = ['chicago', 'new York City', 'washington']
    while True:
        city = input(" Please choose a city name from (Chicago, New York City or Washington ) : \n ").lower()
        if city in citys:
            break
        else:
            print(' your choice is not available, please try again ')

    # TO DO: get user input for month (all, january, february, ... , june)

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
    while True:
        month = input(
            " please choose a month to filter by (January, February, March, April, May, June or All ) : \n ").title()
        if month in months:
            break
        else:
            print('your month choice is not available, please try again ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All']
    while True:
        day = input(
            " please choose a day to filter the month by (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or All ) : \n ").title()
        if day in days:
            break
        else:
            print('your day choice is not available, please try again ')

    print('-' * 40)
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

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extracting month , day and hour of the week
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start hour'] = df['Start Time'].dt.hour

    # filtering by month
    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filtering by day
    if day != 'All':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('the most common month is :', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('the most common day of week is :', most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['start hour'].mode()[0]
    print('the most common start hour is : ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_usedStartStation = df['Start Station'].mode()[0]
    print('the most commonly used start station is :', most_common_usedStartStation)

    # TO DO: display most commonly used end station
    most_common_usedEndStation = df['End Station'].mode()[0]
    print('the most commonly used end station is :', most_common_usedEndStation)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = (df['Start Station'] + "," + ['End Station'])
    most_common_usedCombination = df['combination'].mode()[0]
    print('the most common frequent combination of start station and end station trip is :',
          most_common_usedCombination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totalTravelTime = df['Trip Duration'].sum().round()
    print('the Total travel time is :', totalTravelTime)

    # TO DO: display mean travel time
    meanTravelTime = df['Trip Duration'].mean().round()
    print('the Mean travel time is :', meanTravelTime)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usertypes = df['User Type'].value_counts().to_frame()
    print('Counts of user types :', usertypes)

    # TO DO: Display counts of gender
    try:
        userGender = df['Gender'].value_counts().to_frame()
        print('Counts of user gender :', userGender)

        # TO DO: Display earliest, most recent, and most common year of birth
        print('The earliest year of birth is :', (df['Birth Year']).min())
        print('The most recent year of birth is :', (df['Birth Year']).max())
        print('The most common year of birth is :', (df['Birth Year']).mode()[0])

    except KeyError:
        print('Sorry , no data available for this city ')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


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
