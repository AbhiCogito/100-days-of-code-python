import sys, os
from pathlib import Path

os.system("clear")
# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from analysis.summary import progress_data
from analysis.workouts import WorkoutAnalyzer
from analysis.progress import ProgressAnalyzer
from matplotlib import pyplot as plt

# Now use the analyzers
wa = WorkoutAnalyzer(None)
pa = ProgressAnalyzer(None)

# Get data for plotting
print(progress_data)
vol_data = wa.vol_per_exercise()
print(vol_data)

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

