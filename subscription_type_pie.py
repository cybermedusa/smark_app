import functions
from smark_app import db_connection
import matplotlib.pyplot as plt
import pandas as pd

# Users dataframe
users_df = pd.read_sql("select * from users", con=db_connection)

with db_connection.connect() as con:

    all_res = []

    for i in range(1, 4):
        if i == 1:
            results_1 = con.execute('select users.id from users where users.id in (select subscription_payments.user_id from subscription_payments where subscription_payments.subscription_type_id='+str(i)+')')

        if i == 2:
            results_2 = con.execute('select users.id from users where users.id in (select subscription_payments.user_id from subscription_payments where subscription_payments.subscription_type_id='+str(i)+')')

        if i == 3:
            results_3 = con.execute('select users.id from users where users.id in (select subscription_payments.user_id from subscription_payments where subscription_payments.subscription_type_id='+str(i)+')')

    sub_1 = []
    sub_2 = []
    sub_3 = []

    for j in results_1:
        sub_1.append(j)

    for j in results_2:
        sub_2.append(j)

    for j in results_3:
        sub_3.append(j)

    sub_type_1 = len(sub_1)
    sub_type_2 = len(sub_2)
    sub_type_3 = len(sub_3)
    index = users_df.index
    non_subscription_part = len(index) - sum([sub_type_1, sub_type_2, sub_type_3])

    textprops = dict(size=10,
                     fontstyle='oblique',
                     fontweight='bold')

    pie_data = [non_subscription_part, sub_type_1, sub_type_2, sub_type_3]

    plt.pie(pie_data,
            labels=['non-subscription', 'month', 'half year', 'year'],
            textprops=textprops,
            autopct=lambda pct: functions.show_pct_int_pie_chart(pct, pie_data),
            pctdistance=0.75,
            colors=['#44779A', '#7DFAC2', '#4AD6BE', '#2AB1B1'],
            labeldistance=1.1)

    centre_circle = plt.Circle((0, 0), 0.50, fc='white')
    plt.text(0, 0,
             len(index),
             ha='center',
             va='center',
             fontsize=18,
             fontstyle='oblique',
             fontweight='bold')
    fig = plt.gcf()

    fig.gca().add_artist(centre_circle)
    plt.title('Subscription and non-subscription users distribution')
    plt.show()

