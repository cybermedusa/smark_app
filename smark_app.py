import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import functions
import numpy as np
import datetime
pd.options.mode.chained_assignment = None

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
# print(avg_age)

# Age distribution among users
# print(age_distribution_bar)

# What is an average female and male age?
avg_age_f_m = round(users_df.groupby(['gender'])['age'].mean())
# print(avg_age_f_m)

# Bar chart presenting how many females and males have a smark app
# print(gender_distribution_bar)

# How many users have subscription?
subscription_users = pd.read_sql("select * from subscription_payments", con=db_connection)
count_subs_types = subscription_users.groupby(['subscription_type_id'])['id'].count()
total_num_of_sub_users = subscription_users['id'].count()
# print(count_subs_types)
# 1 - 861
# 2 - 836
# 3 - 803
# The most popular subscription type - month

# Subscription type pie chart
# print(subscription_type_pie)

# Gender distribution without subscription pie
# print(gender_distribution_bar)


# with db_connection.connect() as con:
#     # results = con.execute('select count(user_id), subscription_type_id from subscription_payments group by subscription_type_id')
#     # results = con.execute("select count(user_id), date from parking_time_payments group by date")
#     inner_join = con.execute('select * from table parking_time_payments inner join parking_time_payments on parking_time_payments.city_district_id = city_districts.id')
#
#     for i in inner_join:
#         print(i)
    # Najwiecej ludzi ktorzy nie maja wykupionej sukbskrypcji parkowalo 1.11.2021.

    # Przez jak dlugo ludzie 1.11.2021 ktorzy nie maja subskrypcji parkowali i ile za to zaplacili?
    # avg, max, min

parking_time_df = pd.read_sql("select * from parking_time_payments", con=db_connection)
# group_date = parking_time_df.groupby(['date'])['user_id'].count()
# print(parking_time_df)

parking_df = pd.read_sql('select * from parking', con=db_connection)

# Users parking distribution per day bar chart
# print(users_parking_distribution_per_day_bar)


city_district_df = pd.read_sql("select * from city_districts", con=db_connection)
join_city_dist_parking_df = pd.merge(parking_df, city_district_df[['fee', 'id']], left_on='city_district_id', right_on='id')
parking_sub_df = join_city_dist_parking_df.loc[join_city_dist_parking_df['type'] == 'subscription']
parking_non_sub_df = join_city_dist_parking_df.loc[join_city_dist_parking_df['type'] == 'non-subscription']
parking_non_sub_df['total_parking_cost_per_user'] = round((parking_non_sub_df['minutes']/60) * parking_non_sub_df['fee'],2)

# avg, max, min parking time for all users, non-sub users, and sub users (2021 year)
# print(functions.return_avg_min_max_non_sub(parking_non_sub_df))
# print(functions.return_avg_min_max_sub(parking_sub_df))
# print(functions.return_avg_min_max_all_types(join_city_dist_parking_df))

# avg, max, min payment for parking for non-sub users
# print(functions.return_avg_min_max_non_sub_payment(parking_non_sub_df))

# Jakie samochody głównie parkują - elektryki czy nie-elektryki?
cars_df = pd.read_sql("select * from cars", con=db_connection)
group_ele_n_ele = cars_df.groupby(['type'])['id'].count()
# print(group_ele_n_ele)



# W jakiej dzielnicy miasta parkuje najwięcej ludzi?
group_city_district_sub = parking_sub_df.groupby(['city_district_id'])['id_x'].count()
# print(group_city_district_sub)
# Najwiecej subskrybentów parkuje na Grzegorzkach.

group_city_district_non_sub = parking_non_sub_df.groupby(['city_district_id'])['id_x'].count()
# print(group_city_district_non_sub)
# Najwiecej nie-subskrybentow parkuje na Podgorzu.


