import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from smark_app import users_df

users_df['created_at'] = pd.to_datetime(users_df['created_at'])
grouped_users_df = users_df.groupby(pd.Grouper(key='created_at', freq='M'))['id'].count()

avg_per_month = round(10000/12)

x_axs = np.arange(1, 13)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

plt.plot(x_axs,
         grouped_users_df,
         linewidth=3,
         linestyle='dotted',
         color='#44779A',
         marker='o',
         markerfacecolor='#7DFAC2')

for i in range(len(months)):
    plt.annotate(text=grouped_users_df[i],
                 xy=(x_axs[i], grouped_users_df[i]),
                 fontsize='small',
                 fontweight='bold',
                 fontstyle='oblique')

plt.ylabel('Number of users')
plt.title('Registration distribution per months in 2021')
plt.xticks(x_axs, months)
plt.show()