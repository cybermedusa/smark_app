import matplotlib.pyplot as plt
import functions
import pandas as pd
from smark_app import db_connection, parking_df


city_district_df = pd.read_sql("select * from city_districts", con=db_connection)
join_city_dist_parking_df = pd.merge(parking_df, city_district_df[['fee', 'id']], left_on='city_district_id', right_on='id')
parking_sub_df = join_city_dist_parking_df.loc[join_city_dist_parking_df['type'] == 'subscription']
parking_non_sub_df = join_city_dist_parking_df.loc[join_city_dist_parking_df['type'] == 'non-subscription']
parking_non_sub_df['total_parking_cost_per_user'] = round((parking_non_sub_df['minutes']/60) * parking_non_sub_df['fee'], 2)
districts = ['Stare Miasto', 'Kazimierz', 'Grzegórzki', 'Zwierzyniec', 'Podgórze', 'Zabłocie']
boxprops = dict(linestyle='-', linewidth=3, color='#44779A')
whiskerprops = dict(color='black', linewidth=1.5, linestyle=':')
medianprops = dict(color='#7DFAC2', linewidth=3)
parking_non_sub_df.boxplot(by='city_district_id', column=['total_parking_cost_per_user'], grid=False,
                           notch=True, boxprops=boxprops, whiskerprops=whiskerprops,
                           medianprops=medianprops)
plt.suptitle('')
plt.title('Avg, max, min parking cost per city district')
plt.xticks([1, 2, 3, 4, 5, 6], districts)
plt.xlabel('')
plt.ylabel('PLN')
plt.show()