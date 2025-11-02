import os, json
import pandas as pd

os.system("clear")

base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(base_dir, os.pardir))
source_file = os.path.abspath(os.path.join(project_root, "data", "hevy_data_clean.json"))

#Defines how many results per query is needed. Say 5 days per month.
RESULTS_SIZE = 3

class WorkoutAnalyzer:
    def __init__(self, source_file):
        with open(source_file, 'r') as f:
            data = json.load(f)
        self.df = pd.DataFrame(data)
        self.df['Total Vol'] = self.df['Weights (kg)'] * self.df['Reps']
        self.df['Weight per rep'] = self.df['Weights (kg)'] / self.df['Reps']
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df['Week'] = self.df['Date'].dt.isocalendar().week
        self.df['Month'] = self.df['Date'].dt.month
        self.df['Year'] = self.df['Date'].dt.year

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
        #Find sum of Total Vol by Week & Title
        monthly_totals = (
            month_data.groupby('Week')['Total Vol']
            .sum()
            .reset_index()
        )

        #Find sum of total duration per week
        duration = (
            month_data.groupby('Week')['Duration']
            .sum()
            .reset_index()
        )

        #Merge values by week
        merged = monthly_totals.merge(duration, on='Week')
        data_row = merged.sort_values(by='Total Vol', ascending=False).iloc[:RESULTS_SIZE] #.copy()

        #Strftime needs date in YYYY-MM-DD format
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

        #Merge values by week
        merged = monthly_totals.merge(duration, on='Month')
        data_row = merged.sort_values(by='Total Vol', ascending=False).iloc[:RESULTS_SIZE] #.copy()

        #Strftime needs date in YYYY-MM-DD format
        data_row['Month'] = pd.to_datetime(data_row['Month'], format='%m').dt.strftime('%b')
        data_row['Year'] = year

        return data_row[['Year', 'Month', 'Duration', 'Total Vol']]

    # def top_5_days_in_month(self, month):

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


analyzer = WorkoutAnalyzer(source_file)
result = analyzer.top_month_in_year(2025)
# result = analyzer.top_day_in_month(10)
print(result)
