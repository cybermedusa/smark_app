import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from smark_app import db_connection
from avg_max_min_pln_per_city_district import city_districts_parking_merged

# Subscription users dataframe
parking_sub_df = city_districts_parking_merged.loc[city_districts_parking_merged['type'] == 'subscription']

# Non-subscription users dataframe
parking_non_sub_df = city_districts_parking_merged.loc[city_districts_parking_merged['type'] == 'non-subscription']

# City districts dataframe
city_district_df = pd.read_sql("select * from city_districts", con=db_connection)

city_districts_parking_merged['date'] = pd.to_datetime(city_districts_parking_merged['date'])

# Average parking time per city district for subscription users
grouped_sub_parking_avg_time = round(parking_sub_df.groupby('city_district_id')['minutes'].mean(), 2)

# Average parking time per city district for non-subscription users
grouped_non_sub_parking_avg_time = round(parking_non_sub_df.groupby('city_district_id')['minutes'].mean(), 2)

districts = ['Stare Miasto', 'Kazimierz', 'Grzegórzki', 'Zwierzyniec', 'Podgórze', 'Zabłocie']

x_axs = np.arange(1, len(districts)+1)

plt.bar(x_axs-0.2,
        grouped_non_sub_parking_avg_time,
        color='#7DFAC2',
        width=0.4,
        label='non-subscription')

plt.bar(x_axs+0.2,
        grouped_sub_parking_avg_time,
        color='#44779A',
        width=0.4,
        label='subscription')

plt.xticks(x_axs, districts)
plt.xlabel('Cracow districts')
plt.ylabel('Average parking time [min]')
plt.title('Users average parking time distribution per city district')
plt.legend()
plt.ylim(0, 400)

for i in range(1, len(x_axs)+1):
    plt.text(i, grouped_sub_parking_avg_time[i], grouped_sub_parking_avg_time[i],
             size='small', fontweight='bold', fontstyle='oblique')

    plt.text(i, grouped_non_sub_parking_avg_time[i], grouped_non_sub_parking_avg_time[i],
             size='small', ha='right', fontweight='bold', fontstyle='oblique')

plt.show()

