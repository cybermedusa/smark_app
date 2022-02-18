from smark_app import db_connection
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Parking dataframe
parking_df = pd.read_sql('select * from parking', con=db_connection)
parking_df['date'] = pd.to_datetime(parking_df['date'])

# Parking df grouped by months
grouped_parking_df = parking_df.groupby(pd.Grouper(key='date', freq='M'))['id'].count()

# Users without subscription df
non_sub_df = parking_df.loc[parking_df['type'] == 'non-subscription']

# Average parking time per date
avg_non_sub_df = round(non_sub_df.groupby(['date'])['minutes'].mean())

# Non-subscription users grouped by months
grouped_non_sub_df = non_sub_df.groupby(pd.Grouper(key='date', freq='M'))['id'].count()

# Users with subscription
sub_df = parking_df.loc[parking_df['type'] == 'subscription']

# Average parking time per date
avg_sub_df = round(sub_df.groupby(['date'])['minutes'].mean())

# Subscription users grouped by months
grouped_sub_df = sub_df.groupby(pd.Grouper(key='date', freq='M'))['id'].count()

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
number_of_months = 12
x_axis = np.arange(1, number_of_months+1)

plt.bar(x_axis-0.2,
        grouped_sub_df,
        width=0.4,
        label='users with subscription',
        color='#44779A')

plt.bar(x_axis+0.2,
        grouped_non_sub_df,
        width=0.4,
        label='users without subscription',
        color='#7DFAC2')

count = 0
for i in range(1, 13):
    plt.text(i-0.2, grouped_sub_df[count], grouped_sub_df[count], fontweight='bold', fontstyle='oblique',
             size='small', ha='center')

    plt.text(i+0.2, grouped_non_sub_df[count], grouped_non_sub_df[count], fontweight='bold', fontstyle='oblique',
             size='small', ha='center')

    count += 1

plt.xticks(x_axis, months)
plt.ylabel('Number of users parking records')
plt.title('Users parking distribution per months in 2021')
plt.legend()
plt.show()