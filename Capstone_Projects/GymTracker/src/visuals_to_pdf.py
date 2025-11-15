import os
import matplotlib.pyplot as plt
from visuals import WorkoutCharts, ProgressCharts

wc = WorkoutCharts()
pc = ProgressCharts()


vol_per_exercise_fig = wc.vol_per_exercise_chart()
# vol_per_title_fig = wc.vol_per_title_chart()

avg_wt_per_rep_per_ex_fig = wc.avg_wt_per_rep_per_ex_chart()

# total_wt_per_day_fig = wc.total_wt_per_day_chart()
# total_wt_per_week_fig = wc.total_wt_per_week_chart()
# total_wt_per_month_fig = wc.total_wt_per_month_chart()
# avg_workout_duration_fig = wc.avg_workout_duration_chart()
# top_day_week_fig = wc.top_day_in_week_chart()
# top_day_month_fig = wc.top_day_in_month_chart()
# top_day_year_fig = wc.top_day_in_year_chart()
# top_week_month_fig = wc.top_week_in_month_chart()
# top_month_year_fig = wc.top_month_in_year_chart()
# ex_monthly_variety_fig = pc.exercise_monthly_variety_chart()

plt.show()