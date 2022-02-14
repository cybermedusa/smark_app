import pandas as pd
from smark_app import db_connection
import matplotlib.pyplot as plt

# Jaki jest sredni czas parkowania ludzi przed posiadaniem apki a jaki po?
feedback_df = pd.read_sql('select * from feedbacks', con=db_connection)
feedback_df['difference'] = feedback_df['time_before_app'] - feedback_df['time_after_app']
grouped_before = round(feedback_df.groupby('city_district_id')['time_before_app'].mean(), 2)
# print(grouped_before)
# print(feedback_df.sort_values(by='difference', ascending=False).head(50))
# avg time before app
avg_time_before_app = round(feedback_df['time_before_app'].mean(), 2)
# print(avg_time_before_app)

# avg time after app
avg_time_after_app = round(feedback_df['time_after_app'].mean(), 2)
grouped_after = round(feedback_df.groupby('city_district_id')['time_after_app'].mean(), 2)
# print(grouped_after)
# print(avg_time_after_app)

x_axs = [1, 2, 3, 4, 5, 6]
districts = ['Stare Miasto', 'Kazimierz', 'Grzegórzki', 'Zwierzyniec', 'Podgórze', 'Zabłocie']
plt.plot(x_axs, grouped_before, color='#44779A', label='parking time before app', marker='o')
plt.plot(x_axs, grouped_after, color='#7DFAC2', label='parking time after app', marker='o')
plt.title('Parking time distribution before and after app')
plt.xticks(x_axs, districts)
plt.legend()
plt.ylim(0, 18)
plt.ylabel('Time [min]')
plt.xlabel('Cracow districts')
for x, y in zip(x_axs, grouped_before):
    plt.annotate(text=y, xy=(x, y), fontstyle='oblique', fontweight='bold', size='small', textcoords='data', ha='center')
for x, y in zip(x_axs, grouped_after):
    plt.annotate(text=y, xy=(x, y), fontstyle='oblique', fontweight='bold', size='small', textcoords='data', ha='center')
plt.show()