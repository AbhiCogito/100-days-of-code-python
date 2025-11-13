import sys, os
from pathlib import Path

os.system("clear")
# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# from analysis.summary import progress_data
from analysis.workouts import WorkoutAnalyzer
from analysis.progress import ProgressAnalyzer
import matplotlib.pyplot as plt # Same as <from matplotlib import pyplot as plt>
import numpy as np

# Now use the analyzers
wa = WorkoutAnalyzer(None)
pa = ProgressAnalyzer(None)

class workouts_charts:

    def __init__(self, workouts=None, progress=None):

        self.wa = workouts if workouts else WorkoutAnalyzer(None)
        self.pa = progress if progress else ProgressAnalyzer(None)

    def vol_per_exercise_chart(self, items=3):

        df = self.wa.vol_per_exercise()
        vol_data = df.sort_values(by='Total Vol', ascending=False)
        vol_data = vol_data.head(items).copy()

        fig, ax = plt.subplots()
        ax.bar(vol_data['Exercise'], vol_data['Total Vol'])
        ax.set_xlabel('Exercise Name')
        ax.set_ylabel('Total volume in kg')
        ax.set_title(f'Total vol for top {items} exercises')

        return fig

    def vol_per_title_chart(self, items=5):

        df = self.wa.vol_per_title().head(items).copy()
        print(df)

        fig, ax = plt.subplots()
        ax.bar(df['Title'], df['Total Vol'])
        ax.set_xlabel('Day Focus')
        ax.set_ylabel('Total volume in kg')
        ax.set_title(f'Total vol for top {items} days')
        plt.setp(ax.get_xticklabels(),rotation=45, ha='right')
        plt.show()
        
        return fig

    def avg_wt_per_rep_per_ex_chart(self, items=5):
        df = self.wa.avg_wt_per_rep_per_exercise().head(items).copy()
        print(df)

        fig, ax = plt.subplots()
        ax.bar(df['Exercise'], df['Weight per rep'])
        ax.set_xlabel('Exercise')
        ax.set_ylabel('Average weight per rep')
        ax.set_title(f'Total vol for top {items} days')
        plt.setp(ax.get_xticklabels(),rotation=45, ha='right')
        plt.show()
        
        return fig

    def total_wt_per_day_chart(self):
        df = self.wa.total_weight_reps_per_day()
        print(df)

        fig, ax1 = plt.subplots()
        plt.title('Total volume and reps over date')
        
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Total Vol (kg)', color='blue')
        ax1.scatter(df['Date'], df['Total Vol'], color='blue', marker='x')

        ax2 = ax1.twinx() #Twin along the same x-axis

        ax2.set_ylabel('Reps', color='red')
        ax2.scatter(df['Date'], df['Reps'], color='red', marker='o')

        fig.autofmt_xdate(rotation=45) #Auto-formats the <date> only
        fig.tight_layout()

        return fig

    def total_wt_per_week_chart(self):
        df = self.wa.total_weight_reps_per_week()
        print(df)

        fig, ax1 = plt.subplots()
        plt.title('Total volume and reps over date')
        
        ax1.set_xlabel('Week')
        ax1.set_ylabel('Total Vol (kg)', color='blue')
        ax1.scatter(df['Week'], df['Total Vol'], color='blue', marker='x')

        ax2 = ax1.twinx() #Twin along the same x-axis

        ax2.set_ylabel('Reps', color='red')
        ax2.scatter(df['Week'], df['Reps'], color='red', marker='o')

        fig.autofmt_xdate(rotation=45) #Auto-formats the <date> only
        fig.tight_layout()

        return fig

    def total_wt_per_month_chart(self):
        df = self.wa.total_weight_reps_per_month()
        print(df)

        fig, ax1 = plt.subplots()
        plt.title('Total volume and reps over date')
        
        ax1.set_xlabel('Month')
        ax1.set_ylabel('Total Vol (kg)', color='blue')
        ax1.scatter(df['Month'], df['Total Vol'], color='blue', marker='x')

        ax2 = ax1.twinx() #Twin along the same x-axis

        ax2.set_ylabel('Reps', color='red')
        ax2.scatter(df['Month'], df['Reps'], color='red', marker='o')

        fig.autofmt_xdate(rotation=45) #Auto-formats the <date> only
        fig.tight_layout()

        return fig

    def avg_workout_duration_chart(self, items=5):
        df = self.wa.avg_workout_duration().sort_values(by='Duration (min)', ascending=False).head(items)
        print(df)

        #Since <matplotlib? takes date as a date-time obj, we need to convert it into a string  
        #String will display only the required values while dt obj will display all the dates
        df['Date_Str'] = df['Date'].dt.strftime('%Y-%m-%d')

        fig, ax = plt.subplots()

        ax.bar(df['Date_Str'], df['Duration (min)'])
        ax.set_title('Average workout duration (max)')
        ax.set_xlabel('Date')
        ax.set_ylabel('Duration (min)')

        fig.autofmt_xdate(rotation=45)

        return fig

    def top_day_in_week_chart(self, week=34):
        df = self.wa.top_day_in_week(week)
        print(df)

        #Convert date from date-time obj to string
        df['Date'] = df['Date'].dt.strftime('%d-%m-%Y')

        fig, ax1 = plt.subplots()
        width = 0.35

        #Create an array of values [0 - <len(date)>]. This does not include actual dates, but an array of their indices
        x = np.arange(len(df['Date']))

        ax1.set_xlabel('Date')
        ax1.set_ylabel('Total Weight')
        ax1.bar(x-width/2, df['Total Vol'], width, color='skyblue')

        ax2 = ax1.twinx()
        ax2.set_ylabel('Duration')
        ax2.bar(x+width/2, df['Duration'], width/2, color='teal')

        #To set ticks on x-axis as per the x array
        ax1.set_xticks(x)
        ax1.set_xticklabels(df['Date'])

        return fig

    def top_day_in_month_chart(self, month=10):
        df = self.wa.top_day_in_month(month)
        print(df)

        #Convert date from date-time obj to string
        df['Date'] = df['Date'].dt.strftime('%d-%m-%Y')

        fig, ax1 = plt.subplots()
        width = 0.35

        #Create an array of values [0 - <len(date)>]. This does not include actual dates, but an array of their indices
        x = np.arange(len(df['Date']))

        ax1.set_xlabel('Date')
        ax1.set_ylabel('Total Weight')
        ax1.bar(x-width/2, df['Total Vol'], width, color='skyblue')

        ax2 = ax1.twinx()
        ax2.set_ylabel('Duration')
        ax2.bar(x+width/2, df['Duration'], width/2, color='teal')

        #To set ticks on x-axis as per the x array
        ax1.set_xticks(x)
        ax1.set_xticklabels(df['Date'])

        plt.show()

wc = workouts_charts(workouts=wa, progress=pa)
wc.top_day_in_month_chart(10)

# fig, axes = plt.subplots(2, 2)  # 2x2 grid of axes
# axes[0, 0].plot([1, 2, 3], [1, 4, 9])   # top-left
# axes[0, 1].bar([1, 2, 3], [3, 2, 5])    # top-right
# axes[1, 0].scatter([1, 2, 3], [5, 7, 9]) # bottom-left
# axes[1, 1].pie([10, 20, 30])             # bottom-right

# plt.show()


x = ['Money', 'Sophie', 'Priya', 'Anne']
y = [1,2,3,4]
age = [41, 5, 36, 15]

# plt.bar(x,y, width=0.6, color='cyan', edgecolor='pink', linewidth=3, alpha=0.3)
# plt.bar(x,age, width=0.6, color='blue', edgecolor='pink', linewidth=3, alpha=0.3)
# plt.title("My first matplotlib graph")
# plt.xlabel("Name", fontsize=21, color='pink')
# plt.ylabel("Order")
# # plt.gca().set_facecolor('black')   # axes background
# # plt.gcf().set_facecolor('black')   # figure background
# plt.show()

