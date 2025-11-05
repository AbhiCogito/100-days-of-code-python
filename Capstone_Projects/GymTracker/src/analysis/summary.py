import pandas as pd
import datetime, os
from workouts import WorkoutAnalyzer
os.system("clear")

data = {}

wa = WorkoutAnalyzer(None)

progress_data = {
    "Vol per title": wa.vol_per_title().to_dict(orient='records'),
    "Vol per exercise": wa.vol_per_exercise().to_dict(orient='records'),
    "Daily exercises": wa.daily_exercise().to_dict(orient='records'),
    "Avg wt per rep per exercise": wa.avg_wt_per_rep_per_exercise().to_dict(orient='records'),
    "Avg wt per workout": wa.avg_weight_per_workout(), #Single value so no need to convert to dict
    "Total wt and reps per day": wa.total_weight_reps_per_day().to_dict(orient='records'),
    "Total wt and reps per week": wa.total_weight_reps_per_week,
}

for key, value in progress_data.items():
    print(f"Key --> {key} \nValue --> \n{value}")
# print(progress_data)
# print(daily_exercises)
