import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from visuals import WorkoutCharts, ProgressCharts

wc = WorkoutCharts()
pc = ProgressCharts()

#Fetching charts individually from all the functions
vol_per_exercise_fig = wc.vol_per_exercise_chart()
# vol_per_title_fig = wc.vol_per_title_chart()
avg_wt_per_rep_per_ex_fig = wc.avg_wt_per_rep_per_ex_chart()
total_wt_per_day_fig = wc.total_wt_per_day_chart()
total_wt_per_week_fig = wc.total_wt_per_week_chart()
total_wt_per_month_fig = wc.total_wt_per_month_chart()
avg_workout_duration_fig = wc.avg_workout_duration_chart()
top_day_week_fig = wc.top_day_in_week_chart()
top_day_month_fig = wc.top_day_in_month_chart()
top_day_year_fig = wc.top_day_in_year_chart()
top_week_month_fig = wc.top_week_in_month_chart()
top_month_year_fig = wc.top_month_in_year_chart()
ex_monthly_variety_fig = pc.exercise_monthly_variety_chart()

# Create a list of all generated figure objects

all_figures = [
    vol_per_exercise_fig,
    avg_wt_per_rep_per_ex_fig,
    total_wt_per_day_fig,
    total_wt_per_week_fig,
    total_wt_per_month_fig,
    avg_workout_duration_fig,
    top_day_week_fig,
    top_day_month_fig,
    top_day_year_fig,
    top_week_month_fig,
    top_month_year_fig,
    ex_monthly_variety_fig
]

today_date = datetime.now().strftime('%Y-%m-%d')
# Define the base directory and the specific sub-directory
base_dir = '/Users/Money/Dropbox/Python/100-days-of-code-python'
target_sub_dir = 'Capstone_Projects/GymTracker/visuals'

# Construct the full file path using os.path.join
pdf_filename = os.path.join(
    base_dir,
    target_sub_dir,
    f'{today_date}_Workout_Report.pdf'
)

# Ensure the target directory exists before saving
os.makedirs(os.path.dirname(pdf_filename), exist_ok=True)

print(f"\nSaving charts to: {pdf_filename}")

# Use PdfPages to save all figures
with PdfPages(pdf_filename) as pdf:
    for fig in all_figures:
        # Save the figure to the open PDF file
        pdf.savefig(fig)
        # Close the figure to free up memory (optional but recommended)
        plt.close(fig)

print("PDF successfully generated!")