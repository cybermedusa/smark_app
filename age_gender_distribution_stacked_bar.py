import matplotlib.pyplot as plt
import pandas as pd
from subscription_type_pie import users_df

bins = [18, 30, 40, 50, 60]
labels = ['18-29', '30-39', '40-49', '50-60']
users_df['age_range'] = pd.cut(users_df['age'], bins, labels=labels, include_lowest=True)

# Female df
users_df_f = users_df.loc[users_df['gender'] == 'F']

# Male df
users_df_m = users_df.loc[users_df['gender'] == 'M']

# Female users grouped
grouped_f = users_df_f.groupby('age_range')['gender'].count()

# Male users grouped
grouped_m = users_df_m.groupby('age_range')['gender'].count()

y_age_axs = list(users_df.groupby(by=['age_range'])['id'].count())
plt.bar(labels,
        y_age_axs,
        width=0.5)

plt.bar(labels,
        grouped_f,
        color='#44779A',
        label='F',
        width=0.5)

plt.bar(labels,
        grouped_m,
        bottom=grouped_f,
        color='#7DFAC2',
        label='M',
        width=0.5)

plt.xticks(labels,
           rotation='vertical',
           fontsize='small')

plt.xlabel('Age range')
plt.ylabel('Number of users')
plt.title('Age & gender distribution of all users')

for i in range(len(labels)):
    plt.text(i, grouped_f[i]*1.5, grouped_f[i],
             size='8', ha='center', fontweight='bold', fontstyle='oblique')

    plt.text(i, grouped_m[i]/2, grouped_m[i],
             size='8', ha='center', fontweight='bold', fontstyle='oblique')

plt.legend()
plt.show()

