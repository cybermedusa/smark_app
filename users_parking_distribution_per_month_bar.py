import functions
from smark_app import parking_df
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

parking_df['date'] = pd.to_datetime(parking_df['date'])
x = parking_df.groupby(pd.Grouper(key='date', freq='M'))['id'].count()

non_sub_df = parking_df.loc[parking_df['type'] == 'non-subscription']
# avg_non_sub_df = round(non_sub_df.groupby(['date'])['minutes'].mean())
grouped_non_sub_df = non_sub_df.groupby(pd.Grouper(key='date', freq='M'))['id'].count()
# print(grouped_non_sub_df)

sub_df = parking_df.loc[parking_df['type'] == 'subscription']
# avg_sub_df = round(sub_df.groupby(['date'])['minutes'].mean())
grouped_sub_df = sub_df.groupby(pd.Grouper(key='date', freq='M'))['id'].count()
# print(grouped_sub_df)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
number_of_months = 12
x_axis = np.arange(1, number_of_months+1)
plt.bar(x_axis-0.2, grouped_sub_df, width=0.4, label='users with subscription', color='#44779A')
plt.bar(x_axis+0.2, grouped_non_sub_df, width=0.4, label='users without subscription', color='#7DFAC2')

count = 0
for i in range(1, 13):
    plt.text(i-0.2, grouped_sub_df[count], grouped_sub_df[count], fontweight='bold', fontstyle='oblique', size='small', ha='center')
    plt.text(i+0.2, grouped_non_sub_df[count], grouped_non_sub_df[count], fontweight='bold', fontstyle='oblique', size='small', ha='center')
    count += 1

plt.xticks(x_axis, months)
plt.ylabel('Number of users parking records')
plt.title('Users parking distribution per months in 2021')
plt.legend()
plt.show()

print(grouped_sub_df, grouped_non_sub_df)