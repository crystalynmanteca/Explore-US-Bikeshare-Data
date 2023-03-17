import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june','all']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
CITIES = list(CITY_DATA.keys())

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
        city = input('Let us begin by choosing one of the following cities: Chicago, New York City, or Washington?').lower()
        if city in CITY_DATA:
            print('Excellent! Now choose a month.')
            break
        else:
            print('Sorry not an option! Try again!')
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Alrighty, now choose a month between January and June. ').lower()
        if month in MONTHS:
            print ('Nice choice! Next choose a day of the week.')
            break
        else:
            print('Sorry! How about we try that again?')
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Last step! What weekday would you like to pull data from?').lower()
        if day in DAYS:
            print('Great! Time to look up some data!')
            break
        else:
            print('Close, but no cigar! Try again')
            continue

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
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])


    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df ['Start Hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The Most Popular Start Month:', common_month)


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The Most Popular Start Day:', common_day)

    # TO DO: display the most common start hour
    common_hour = df['Start Hour'].mode()[0]
    print('The Most Popular Start Time:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print("The most popular starting station is:", common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print("The most popular end station is:", common_end)

    # TO DO: display most frequent combination of start station and end station trip
    common_station = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print("The most common used station is:", common_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel =  df['Trip Duration'].sum()
    print(total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print(mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The number of user types are: \n", user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print("Counts of each gender: \n", gender)


    if 'Birth Year' in df:
    # Display earliest, most recent, and most common year of birth
        the_birth_year = df['Birth Year']
    # the most common birth year
        the_most_common_year = the_birth_year.value_counts().idxmax()
        print("The most common birth year:", the_most_common_year)
    # the most recent birth year
        the_most_recent_year = the_birth_year.max()
        print("The most recent birth year:", the_most_recent_year)
    # the most earliest birth year
        the_most_earliest_year = the_birth_year.min()
        print("The most earliest birth year:", the_most_earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df

def raw_data(yz):
    i = 0

    while True:
        yes_or_no = input('Would you like to see 5 lines of Raw Data?')
        if yes_or_no == 'yes':
            print('You asked for it!')
            print(yz.iloc[i:i + 5])
            i = i + 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to start again? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main()
