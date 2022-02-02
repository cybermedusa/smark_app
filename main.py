import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import functions

db_connection_str = 'mysql+pymysql://root:' + "Pomidor98!" + "@localhost:3306/smark"
db_connection = create_engine(db_connection_str)

# Users dataframe
users_df = pd.read_sql("select * from users", con=db_connection)
# print(users_df)

# How many females and males are using smark app?
gender_count = users_df.groupby(by=['gender'])['id'].count()
# print(gender_count)

# What is an average age of users?
avg_age = round(users_df['age'].mean())
print(avg_age)

# Age distribution among users
x_age_axs = [str(item) for item in range(18,61)]
y_age_axs = list(users_df.groupby(by=['age'])['id'].count())
plt.bar(x_age_axs, y_age_axs, color='#A8E9A5')
functions.add_labels_on_chart(x_age_axs, y_age_axs)
plt.xticks(x_age_axs, rotation='vertical', fontsize='small')
plt.xlabel('Age')
plt.ylabel('Number of users')
plt.vlines(str(avg_age), 0, 40, linestyles='dashed', colors='#35888F')
plt.show()

# What is an average female and male age?
avg_age_f_m = round(users_df.groupby(['gender'])['age'].mean())
# print(avg_age_f_m)

# Bar chart presenting how many females and males have a smark app
x_gender_axs = ['female', 'male']
# plt.bar(x_gender_axs, gender_count, color='#A8E9A5', width=0.4)
# functions.add_labels_on_chart(x_gender_axs, gender_count)
# plt.show()
# print(x_gender_axs)
# print(gender_count)

# how many users have subscription?
subscription_users = pd.read_sql("select * from subscription_payments", con=db_connection)
count_subs_types = subscription_users.groupby(['subscription_type_id'])['id'].count()
# print(count_subs_types)
# 1 - 146
# 2 - 144
# 3 - 110
# The most popular subscription type - month

# print(subscription_users)
# subscription_users.info()
# print(subscription_users.columns)

# with db_connection.connect() as con:
#     rs = con.execute('select subscription_payments.user_id from subscription_payments where subscription_payments.subscription_type_id=1')

    # for row in rs:
    #     print(row)

with db_connection.connect() as con:

    all_res = []

    for i in range(1,4):
        results = con.execute('select users.gender from users where users.id in (select subscription_payments.user_id from subscription_payments where subscription_payments.subscription_type_id='+str(i)+')')
        all_res.append(results)

    r1 = []
    r2 = []
    r3 = []
    r = []

    for result in all_res:
        r.append(result)

    functions.append_results_to_lists(r[0], r1)
    functions.append_results_to_lists(r[1], r2)
    functions.append_results_to_lists(r[2], r3)

    functions.print_sub_output(r1, "monthly")
    functions.print_sub_output(r2, "half-year")
    functions.print_sub_output(r3, "yearly")

# How many people parked on specific day from 1-7 Nov?

with db_connection.connect() as con:
    results = con.execute('select count(user_id), subscription_type_id from subscription_payments group by subscription_type_id')
    # results = con.execute("select count(user_id), date from parking_time_payments group by date")
    # inner_join = con.execute('select * from table parking_time_payments inner join parking_time_payments on parking_time_payments.city_district_id = city_districts.id')

    # for i in inner_join:
    #     print(i)
    # Najwiecej ludzi ktorzy nie maja wykupionej sukbskrypcji parkowalo 1.11.2021.

    # Przez jak dlugo ludzie 1.11.2021 ktorzy nie maja subskrypcji parkowali i ile za to zaplacili?
    # avg, max, min

parking_time_df = pd.read_sql("select * from parking_time_payments", con=db_connection)
group_date = parking_time_df.groupby(['date'])['user_id'].count()
# print(group_date)

avg_parking_time = round(parking_time_df.groupby(['date'])['minutes'].mean())
# print(avg_parking_time)

# add column where you calculate how much people paid for parking on specific day
city_district_df = pd.read_sql("select * from city_districts", con=db_connection)
join_df = pd.merge(parking_time_df, city_district_df[['fee', 'id']], left_on='city_district_id', right_on='id')
join_df['total_parking_cost_per_user'] = round((join_df['minutes']/60) * join_df['fee'],2)
# print(join_df.sort_values(by='total_parking_cost_per_user', ascending=False).tail(10))
#avg, max, min cost in zl
# print(round(join_df['total_parking_cost_per_user'].mean()))
# print(join_df['total_parking_cost_per_user'].max())
# print(join_df['total_parking_cost_per_user'].min())

# Jakie samochody głównie parkują - elektryki czy nie-elektryki?
cars_df = pd.read_sql("select * from cars", con=db_connection)
group_ele_n_ele = cars_df.groupby(['type'])['id'].count()
# print(group_ele_n_ele)

# Jaka jest średnia ocena apki?
rate_df = pd.read_sql('select * from rates', con=db_connection)
avg_rate = round(rate_df['value'].mean(),2)
# print(avg_rate)

# W jakiej dzielnicy miasta parkuje najwięcej ludzi?
group_city_district = parking_time_df.groupby(['city_district_id'])['id'].count()
# print(group_city_district)
# Najwiecej parkuje na Zabłociu.

# Jaki jest sredni czas parkowania ludzi przed posiadaniem apki a jaki po?
feedback_df = pd.read_sql('select * from feedbacks', con=db_connection)
feedback_df['difference'] = feedback_df['time_before_app'] - feedback_df['time_after_app']
# print(feedback_df.sort_values(by='difference', ascending=False).head(50))
# avg time before app
avg_time_before_app = feedback_df['time_before_app'].mean()
# print(avg_time_before_app)
# avg time after app
avg_time_after_app = feedback_df['time_after_app'].mean()
# print(avg_time_after_app)