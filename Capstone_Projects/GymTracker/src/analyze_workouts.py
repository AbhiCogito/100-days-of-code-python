import os, json
import pandas as pd

os.system("clear")

base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(base_dir, os.pardir))
source_file = os.path.abspath(os.path.join(project_root, "data", "hevy_data_clean.json"))

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

        week_data = self.df[self.df['Week'] == week].copy()

        daily_totals = (
            week_data.groupby(['Date', 'Title'])['Total Vol']
            .sum()
            .reset_index()
    )

        sorted_data = daily_totals.sort_values(by='Total Vol', ascending=False).iloc[:3]
        data_row = sorted_data.head(1).copy()
        data_row['Month'] = data_row['Date'].dt.strftime('%b')
        data_row['Week'] = week

        duration_lookup = week_data[['Date', 'Title', 'Duration']].drop_duplicates()
        data_row = data_row.merge(duration_lookup, on=['Date', 'Title'], how='left')

        return data_row[['Month','Week', 'Date', 'Title', 'Duration', 'Total Vol']]
    
    def top_day_in_month(self, month):

        month_data = self.df[self.df['Month'] == month].copy()
        sorted_data = month_data.sort_values(by='Total Vol', ascending=False)
        data_row = sorted_data.head(1).copy()
        data_row['Month'] = data_row['Date'].dt.strftime('%b')

        return data_row[['Month','Week', 'Date', 'Title', 'Duration', 'Total Vol']]
    
    def top_week_in_month(self, month):
        month_data = self.df[self.df['Month'] == month].copy()
        sorted_data = month_data.sort_values(by='Total Vol', ascending=False)
        data_row = sorted_data.head(1).copy()
        data_row['Month'] = data_row['Date'].dt.strftime('%b')

        return data_row[['Month','Week', 'Date', 'Title', 'Duration', 'Total Vol']]
   
    # def top_month_in_year(self, year):

    # def top_5_days_in_month(self, month):

    # def top_5_days_in_year(self, year):



analyzer = WorkoutAnalyzer(source_file)
result = analyzer.top_day_in_week(42)
# result = analyzer.top_day_in_month(10)
print(result)
