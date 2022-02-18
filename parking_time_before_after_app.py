import pandas as pd
from smark_app import db_connection
import matplotlib.pyplot as plt

# Feedback dataframe
feedback_df = pd.read_sql('select * from feedbacks', con=db_connection)

# Added column 'difference'
feedback_df['difference'] = feedback_df['time_before_app'] - feedback_df['time_after_app']

# Average parking time before application use (without dividing into city districts)
avg_time_before_app = round(feedback_df['time_before_app'].mean(), 2)

# Average parking time after application use (without dividing into city districts)
avg_time_after_app = round(feedback_df['time_after_app'].mean(), 2)

# Average parking time per city district before application use
grouped_before = round(feedback_df.groupby('city_district_id')['time_before_app'].mean(), 2)

# Average parking time per city district after application use
grouped_after = round(feedback_df.groupby('city_district_id')['time_after_app'].mean(), 2)

x_axs = [1, 2, 3, 4, 5, 6]

districts = ['Stare Miasto', 'Kazimierz', 'Grzegórzki', 'Zwierzyniec', 'Podgórze', 'Zabłocie']

plt.plot(x_axs,
         grouped_before,
         color='#44779A',
         label='parking time before app',
         marker='o')

plt.plot(x_axs,
         grouped_after,
         color='#7DFAC2',
         label='parking time after app',
         marker='o')

plt.title('Time needed to find parking spot before and after app')
plt.xticks(x_axs, districts)
plt.legend()
plt.ylim(0, 18)
plt.ylabel('Time [min]')
plt.xlabel('Cracow districts')

for x, y in zip(x_axs, grouped_before):
    plt.annotate(text=y, xy=(x, y), fontstyle='oblique', fontweight='bold',
                 size='small', textcoords='data', ha='center')

for x, y in zip(x_axs, grouped_after):
    plt.annotate(text=y, xy=(x, y), fontstyle='oblique', fontweight='bold',
                 size='small', textcoords='data', ha='center')

plt.show()