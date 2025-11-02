import os, json
import pandas as pd
import numpy as np

os.system("clear")

base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(base_dir, os.pardir))
source_file = os.path.abspath(os.path.join(project_root, "data", "hevy_data_clean.json"))

#Defines how many results per query is needed. Say 3 or 5 days per month.
RESULTS_SIZE = 3

def load_workout_data(source_file):

    with open(source_file, 'r') as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    df['Total Vol'] = df['Weights (kg)'] * df['Reps']
    df['Weight per rep'] = df['Weights (kg)'] / df['Reps']
    df['Date'] = pd.to_datetime(df['Date'])
    df['Week'] = df['Date'].dt.isocalendar().week
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year

    return df

class WorkoutAnalyzer:
    def __init__(self, source_file):
        self.df = load_workout_data(source_file)

    def vol_per_title(self):
        return (
            self.df.groupby('Title')['Total Vol']
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )
    
    def vol_per_exercise(self):
        return(
            self.df.groupby('Exercise')['Total Vol']
            .sum()
            .reset_index()
        )
    
    def daily_exercise(self):
        return(
            self.df.groupby(['Date', 'Exercise'])['Total Vol']
            .sum()
            .reset_index()
        )
    
    def avg_wt_per_rep_per_exercise(self):
        return(
            self.df.groupby('Exercise')['Weight per rep']
            .mean()
            .reset_index()
        )
    
    def avg_weight_per_workout(self):
        return(
            self.df.groupby('id')['Total Vol']
            .sum() #To sum weight per day using id
            .mean() #To find mean of weight lifted per day
        )
    
    def total_weight_reps_per_day(self):
        return(
            self.df.groupby('id')[['Total Vol', 'Reps']]
            .sum()
            .reset_index()
        )
    
    def total_weight_reps_per_week(self):
        return(
            self.df.groupby('Week')[['Total Vol', 'Reps']]
            .sum()
            .reset_index()
        )
    
    def total_weight_reps_per_month(self):
        return (
            self.df.groupby('Month')[['Total Vol', 'Reps']]
            .sum()
            .reset_index()
        )
    
    def workout_duration_for_a_date(self, date):

        date = pd.to_datetime(date)
        return self.df[self.df['Date'] == date]['Duration'].iloc[0]

    def avg_workout_duration(self):
        return(
            self.df.groupby('id')['Duration']
            .mean()
            .reset_index()
            .rename(columns={'Duration': 'Duration (min)'})
        )
    
    def top_day_in_week(self, week):
        #Copy the data for the relevant week
        week_data = self.df[self.df['Week'] == week].copy()
        #Find sum of Total Vol grouped by Date & Title
        daily_totals = (
            week_data.groupby(['Date', 'Title'])['Total Vol']
            .sum()
            .reset_index()
        ) #Groupby output will only contain Date, Title, and Total Vol. Other cols will be dropped

        #Arrange top three summed values in descending order
        data_row = daily_totals.sort_values(by='Total Vol', ascending=False).iloc[:RESULTS_SIZE]

        #Convert month display format from 09 to Sep
        data_row['Month'] = data_row['Date'].dt.strftime('%b')
        data_row['Week'] = week

        #Find duration value in the original copy as data is lost after groupby
        duration_lookup = week_data[['Date', 'Title', 'Duration']].drop_duplicates()
        #Merge duration back to the data set arranged in descending order
        data_row = data_row.merge(duration_lookup, on=['Date', 'Title'], how='left')

        return data_row[['Month','Week', 'Date', 'Title', 'Duration', 'Total Vol']]
    
    def top_day_in_month(self, month):
        #Copy the data for the relevant month
        month_data = self.df[self.df['Month'] == month].copy()
        #Find sum of Total Vol by Date & Title
        monthly_totals = (
            month_data.groupby(['Date', 'Title'])['Total Vol']
            .sum()
            .reset_index()
        )

        data_row = monthly_totals.sort_values(by='Total Vol', ascending=False).iloc[:RESULTS_SIZE]
        data_row['Month'] = data_row['Date'].dt.strftime('%b')
        data_row['Week'] = data_row['Date'].dt.isocalendar().week

        #Find duration value in the original copy as data is lost after groupby
        duration_lookup = month_data[['Date', 'Title', 'Duration']].drop_duplicates()
        #Merge duration back to the data set arranged in descending order
        data_row = data_row.merge(duration_lookup, on=['Date', 'Title'], how='left')

        return data_row[['Month','Week', 'Date', 'Title', 'Duration', 'Total Vol']]
    
    def top_week_in_month(self, month):
        #Copy the data for the relevant month
        month_data = self.df[self.df['Month'] == month].copy()
        #Find sum of Total Vol & Duration by Week & Title
        weekly_totals = (
            month_data.groupby('Week', as_index=False) #Not make Week as the new index for the grouped data
            .agg({'Total Vol': 'sum', 'Duration': 'sum'})
        )

        data_row = weekly_totals.sort_values(by='Total Vol', ascending=False).iloc[:RESULTS_SIZE] #.copy()

        #Strftime needs date in YYYY-MM-DD format. Only month is needed, rest data is ignored, hence hardcoded.
        data_row['Month'] = pd.to_datetime(f'2025-{month}-01').strftime('%b')

        return data_row[['Month','Week', 'Duration', 'Total Vol']]
   
    def top_month_in_year(self, year):
        #Copy the data for the relevant month
        year_data = self.df[self.df['Year'] == year].copy()
        #Find sum of Total Vol by Week & Title
        monthly_totals = (
            year_data.groupby('Month')['Total Vol']
            .sum()
            .reset_index()
        )

        #Find sum of total duration per week
        duration = (
            year_data.groupby('Month')['Duration']
            .sum()
            .reset_index()
        )

        #Merge values by week (alternative is to use aggregator on groupby)
        merged = monthly_totals.merge(duration, on='Month')
        data_row = merged.sort_values(by='Total Vol', ascending=False).iloc[:RESULTS_SIZE] #.copy()

        #Strftime needs date in YYYY-MM-DD format
        data_row['Month'] = pd.to_datetime(data_row['Month'], format='%m').dt.strftime('%b')
        data_row['Year'] = year

        return data_row[['Year', 'Month', 'Duration', 'Total Vol']]

    def top_day_in_year(self, year):
        # Copy the data for the relevant year
        year_data = self.df[self.df['Year'] == year].copy()

        # Find sum of Total Vol by Date & Title
        yearly_totals = (
            year_data.groupby(['Date', 'Title'])['Total Vol']
            .sum()
            .reset_index()
        )

        # Arrange top three summed values in descending order
        data_row = yearly_totals.sort_values(by='Total Vol', ascending=False).iloc[:RESULTS_SIZE]

        # Add Month and Week info from Date
        data_row['Month'] = data_row['Date'].dt.strftime('%b')
        data_row['Week'] = data_row['Date'].dt.isocalendar().week

        # Find duration value in the original copy as data is lost after groupby
        duration_lookup = year_data[['Date', 'Title', 'Duration']].drop_duplicates()

        # Merge duration back to the data set arranged in descending order
        data_row = data_row.merge(duration_lookup, on=['Date', 'Title'], how='left')

        return data_row[['Month', 'Week', 'Date', 'Title', 'Duration', 'Total Vol']]

class ProgressAnalyzer:

    def __init__(self, source_file):
        self.df = load_workout_data(source_file)

    def exercise_weekly_progress(self):
        #Find names of all the exercises
        self.exercises_list = self.df['Exercise'].unique()

        while True:
            print("Enter the number for the exercise for which weekly progress is required:")
            for i, exercise in enumerate(self.exercises_list, start=1):
                print(f"{i}: {exercise}")

            try: 
                choice = int(input("Enter 0 for exit. \nEnter the number for the corresponding exercise: "))
                if choice == 0: break
                if 1 <= choice <= len(self.exercises_list):
                    selected_exercise = self.exercises_list[choice - 1] #Coz Python index starts from 0
                    ex_data = self.df[self.df['Exercise']== selected_exercise].copy()
                    exercise_data = ex_data.groupby('Week').agg({
                        'Total Vol': 'sum', 
                        'Reps': 'sum', 
                        'Exercise': 'count'
                        }).rename(columns={'Exercise': 'Frequency'})

                    min_week = exercise_data.index.min()
                    max_week = exercise_data.index.max()
                    week_index = range(min_week, max_week, +1)
                    #Fill the missing weeks with 0
                    fill_index = exercise_data.reindex(week_index, fill_value = 0)
                    #Adding a custom weight-per-rep col and replacing NaN with 0
                    fill_index['Avg Weight per rep'] = (fill_index['Total Vol'] / fill_index['Reps']).fillna(0)
                    return selected_exercise, fill_index
                
            except (ValueError, IndexError):
                print(f"Exercise number should be between 1 and {len(self.exercises_list)}")
                continue
        
    def exercise_monthly_progress(self):
        #Find names of all the exercises
        self.exercises_list = self.df['Exercise'].unique()

        while True:
            print("Enter the number for the exercise for which weekly progress is required:")
            for i, exercise in enumerate(self.exercises_list, start=1):
                print(f"{i}: {exercise}")

            try: 
                choice = int(input("Enter 0 for exit. \nEnter the number for the corresponding exercise: "))
                if choice == 0: break
                if 1 <= choice <= len(self.exercises_list):
                    selected_exercise = self.exercises_list[choice - 1] #Coz Python index starts from 0
                    ex_data = self.df[self.df['Exercise']== selected_exercise].copy()
                    exercise_data = ex_data.groupby('Month').agg({
                        'Total Vol': 'sum', 
                        'Reps': 'sum', 
                        'Exercise': 'count'
                        }).rename(columns={'Exercise': 'Frequency'})

                    min_month = exercise_data.index.min()
                    max_month = exercise_data.index.max()
                    month_index = range(min_month, max_month, +1)
                    #Fill the missing weeks with 0
                    fill_index = exercise_data.reindex(month_index, fill_value = 0)
                    #Adding a custom weight-per-rep col and replacing NaN with 0
                    fill_index['Avg Weight per rep'] = (fill_index['Total Vol'] / fill_index['Reps']).fillna(0)
                    return selected_exercise, fill_index
                
            except (ValueError, IndexError):
                print(f"Exercise number should be between 1 and {len(self.exercises_list)}")
                continue
    
    def exercise_monthly_variety(self):
            
        monthly_exercises = {}
        exercises_count = {}
        exercises_summary = []

        # Getting data for the month
        months = self.df['Month'].unique().tolist()

        for m in months:
            # Creating a dictionary of month and all the unique exercises in that month
            monthly_exercises[m] = (
                self.df[self.df['Month'] == m]['Exercise']
                .dropna()
                .pipe(lambda x: sorted(set(x)))
            )

        for month, exercise in monthly_exercises.items():
            exercises_count[month] = len(exercise)

        for i in range(1, len(months)):

            # Extracting year for the current month
            year = self.df[self.df['Month'] == months[i]]['Year'].iloc[0]

            # Current and previous month's exercise sets
            curr_set = set(monthly_exercises[months[i]])
            prev_set = set(monthly_exercises[months[i-1]])

            # Exercises that are new this month and those that were dropped
            new_exer = curr_set - prev_set
            drop_exer = prev_set - curr_set

            # Count total exercises (including duplicates) in the current month
            total_exercises = self.df[self.df['Month'] == months[i]]['Exercise'].dropna().shape[0]

            # Count of unique exercises in the current month
            unique_exercises = len(monthly_exercises[months[i]])

            # Calculating variety score: proportion of unique exercises to total performed
            variety_score = unique_exercises / total_exercises if total_exercises > 0 else 0

            exercises_summary.append({
                'Year': year,
                'Month': months[i],
                'New Exercises': new_exer,
                'Dropped Exercises': drop_exer,
                'New Exercises count': len(new_exer),
                'Old Exercises count': len(drop_exer),
                'Unique Exercises': unique_exercises,
                'Total Exercises': total_exercises,
                'Variety Score': round(variety_score, 3)  # Rounded for readability
            })

        df_summary = pd.DataFrame(exercises_summary)
        df_sorted = df_summary.sort_values(by='Month', ascending=False)

        return df_sorted
    
    def streaks_and_rests(self):


analyzer = ProgressAnalyzer(source_file)
result = analyzer.exercise_monthly_variety()
# result = analyzer.top_day_in_month(10)
print(result)
