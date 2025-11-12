import pandas as pd
from .workouts import load_workout_data, DEFAULT_SOURCE_FILE


class ProgressAnalyzer:

    def __init__(self, source_file):
        if source_file is None:
            source_file = DEFAULT_SOURCE_FILE
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
                    selected_exercise = self.exercises_list[choice - 1]
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
                    selected_exercise = self.exercises_list[choice - 1]
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
                'Variety Score': round(variety_score, 3)
            })

        df_summary = pd.DataFrame(exercises_summary)
        df_sorted = df_summary.sort_values(by='Month', ascending=False)

        return df_sorted

    def streaks_and_gaps(self):
        # Convert and sort unique workout dates
        dates = sorted(pd.to_datetime(self.df['Date'].unique()))
        
        streaks = []
        gaps = []
        current_streak = [dates[0]]

        for i in range(1, len(dates)):
            delta = (dates[i] - dates[i - 1]).days

            if delta == 1:
                current_streak.append(dates[i])
            elif delta == 2:
                if len(current_streak) >= 5:
                    current_streak.append(dates[i])
                else:
                    if len(current_streak) >= 2:
                        streaks.append(current_streak)
                    current_streak = [dates[i]]
            else:
                if len(current_streak) >= 2:
                    streaks.append(current_streak)
                gaps.append((dates[i - 1], dates[i]))
                current_streak = [dates[i]]

        if len(current_streak) >= 2:
            streaks.append(current_streak)

        # Format streaks into a DataFrame
        streak_rows = []
        for s in streaks:
            start = s[0]
            end = s[-1]
            streak_rows.append({
                'Streak (days)': len(s),
                'Month(Start)': start.month,
                'Month(End)': end.month,
                'Year': start.year,
                'Details': [d.strftime('%d-%b-%Y') for d in s]
            })
        df_streaks = pd.DataFrame(streak_rows)

        # Format gaps into a DataFrame
        gap_rows = []
        for g in sorted(gaps, key=lambda x: (x[1] - x[0]).days, reverse=True):
            start, end = g
            gap_days = (end - start).days
            gap_rows.append({
                'Gap (days)': gap_days,
                'Month(Start)': start.month,
                'Month(End)': end.month,
                'Year': start.year,
                'Details': f"{start.strftime('%d-%b-%Y')} to {end.strftime('%d-%b-%Y')}"
            })
        df_gaps = pd.DataFrame(gap_rows)

        return df_streaks, df_gaps