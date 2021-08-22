import time
import pandas as pd
import numpy as np

CITY_DATA = { "chicago": "chicago.csv",
              "new york city": "new_york_city.csv",
              "washington": "washington.csv" }

months = ["january", "february", "march", "april", "may", "june" , "all"]
days=["monday", "tuesday" , "wednesday" , "thursday" , "friday" , "saturday" , "sunday" , "all"]




def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    city=input("which city you want to analyze : ").lower()
    while city not in CITY_DATA.keys():
        if city !=  city.upper():
            print("Error.Please enter one of three cities : chicago , new york city or washington  ")
            break
        
    month=input("which month you want to analyze : ").lower()
    while month not in months:
        if month !=  month.upper():
            print("Error.Please enter one of six months : january , fabruary , march , april , may , june or all of them")
            break

    day=input("which day you want to analyze : ").lower()
    while day not in days:
        if day !=  day.upper():
            print("Error.Please enter one of seven days : Monday , Tuesday , Wednesday , Thursday , Friday , Saturday , Sunday or all of them")
            break
    print('-'*40)
    return city,month,day

#city,month,day=get_filters()

def load_data(city, month, day):
    xx=CITY_DATA.get(city)
    df=pd.read_csv(xx)
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    df['weekday'] = pd.to_datetime(df['Start Time']).dt.weekday_name
    

    if month != 'all':
        m = months.index(month) + 1
        df = df[df.month == m]
    
    if day != 'all':
        df = df[df.weekday == day.title()]
        
    return df


#df=load_data(city, month, day)



def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()   
    most_common_month=df["month"].value_counts().idxmax()
    print("The most common month is {}".format(most_common_month))
    most_day_of_week=df["weekday"].value_counts().idxmax()
    print("The most common day of week is {}".format(most_day_of_week))
    df["hour"] = pd.to_datetime(df["Start Time"]).dt.hour
    most_start_hour=df["hour"].value_counts().idxmax()
    print("The most common start hour is {}".format(most_start_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    most_start_station=df['Start Station'].value_counts().idxmax()
    print("The most common start station is {}".format(most_start_station))
    most_end_station=df['End Station'].value_counts().idxmax()
    print("The most common end station is {}".format(most_end_station))    
    most_start_end_station=df.groupby(['Start Station','End Station']).size().idxmax()
    print("The most common start-end station is {}".format(most_start_end_station))    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    total_trip_duration = np.sum(df['Trip Duration'])
    total_trip_duration_minutes = total_trip_duration // 60
    total_trip_duration_seconds = total_trip_duration % 60

    if total_trip_duration_minutes > 60:
        total_trip_duration_hours = total_trip_duration_minutes // 60
        total_trip_duration_minutes_wihout_hour = total_trip_duration_minutes % 60
        print("The total trip duration in hour is {} , minutes is {} and second is {}".format(total_trip_duration_hours,total_trip_duration_minutes_wihout_hour,total_trip_duration_seconds) )
    
    else:
        print("The total trip duration in minutes is {} and second is {}".format(total_trip_duration_minutes,total_trip_duration_seconds ))

    average_trip_duration =int(np.mean(df['Trip Duration']))
    average_trip_duration_minutes = average_trip_duration //60
    average_trip_duration_seconds = average_trip_duration % 60

    if average_trip_duration_minutes > 60:
        average_trip_duration_hours = average_trip_duration_minutes // 60
        average_trip_duration_minutes_wihout_hour = average_trip_duration_minutes % 60
        print("The average trip duration in hour is {} , minutes is {} and second is {}".format(average_trip_duration_hours,average_trip_duration_minutes_wihout_hour,average_trip_duration_seconds) )
    
    else:
        print("The average trip duration in minutes is {} and second is {}".format(average_trip_duration_minutes,average_trip_duration_seconds ))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    counts_of_user_types = df.groupby("User Type").size()
    print("Frequency values of user types is {}".format(counts_of_user_types))
    #ttt=df["User Type"].value_counts()
    try:
        
        
        counts_of_Gender = df.groupby("Gender").size()
        print("Frequency values of gender is {}".format(counts_of_Gender))

        earliest_common_year_of_birth = int(pd.DataFrame.min(df["Birth Year"]))
        print("Earliest common year of birth year is {}".format(earliest_common_year_of_birth))
        
        recent_common_year_of_birth = int(pd.DataFrame.max(df["Birth Year"]))
        print("Recent common year of birth year is {}".format(recent_common_year_of_birth))

        most_common_year_of_birth = int(df['Birth Year'].value_counts().idxmax())
        print("Most common year of birth year is {}".format(most_common_year_of_birth))
    
    
    except:
        
        print("There is no Gender or Birth Year features in such dataset to analyze")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    r=["yes","no"]
    n=input("Do you want to view the data ? ").lower()
    while n not in r:
        if n !=  n.upper():
            print("Error.Please enter one of two options : yes or no  ")
            break
        
    while n == "yes":
        if n == "yes":
            print(df.iloc[:, :].values)
            break
            
        elif n != "no":
            break

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
