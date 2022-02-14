import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import functions
from smark_app import parking_df, join_city_dist_parking_df, parking_non_sub_df, parking_sub_df

join_city_dist_parking_df['date'] = pd.to_datetime(join_city_dist_parking_df['date'])
# grouped_parking_month_type_district = round(join_city_dist_parking_df.groupby([pd.Grouper(key='date', freq='M'), 'city_district_id', 'type'])['minutes'].mean(), 2)
# print(grouped_parking_month_type_district)
grouped_sub_parking_avg_time = round(parking_sub_df.groupby('city_district_id')['minutes'].mean(), 2)
grouped_non_sub_parking_avg_time = round(parking_non_sub_df.groupby('city_district_id')['minutes'].mean(), 2)

districts = ['Stare Miasto', 'Kazimierz', 'Grzegórzki', 'Zwierzyniec', 'Podgórze', 'Zabłocie']

x_axs = np.arange(1, len(districts)+1)
# print(grouped_non_sub_parking_avg_time)
# print(grouped_sub_parking_avg_time)

plt.bar(x_axs-0.2, grouped_non_sub_parking_avg_time, color='#7DFAC2', width=0.4, label='non-subscription')
plt.bar(x_axs+0.2, grouped_sub_parking_avg_time, color='#44779A', width=0.4, label='subscription')
plt.xticks(x_axs, districts)
plt.xlabel('Cracow districts')
plt.ylabel('Average parking time [min]')
plt.title('Users average parking time distribution per city district')
plt.legend()
plt.ylim(0, 400)
for i in range(1, len(x_axs)+1):
    plt.text(i, grouped_sub_parking_avg_time[i], grouped_sub_parking_avg_time[i], size='small', fontweight='bold', fontstyle='oblique')
    plt.text(i, grouped_non_sub_parking_avg_time[i], grouped_non_sub_parking_avg_time[i], size='small', ha='right', fontweight='bold', fontstyle='oblique')
plt.show()

