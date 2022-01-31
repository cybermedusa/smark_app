import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from collections import Counter
import functions


# connection = mysql.connector.connect(host='localhost', user='root', passwd='Pomidor98!', database='smark')

# my_cursor = connection.cursor()

# my_cursor.execute("show databases")

# my_cursor.execute("select * from users")

# for i in my_cursor:
    # print(i)

db_connection_str = 'mysql+pymysql://root:' + "Pomidor98!" + "@localhost:3306/smark"
db_connection = create_engine(db_connection_str)

users_df = pd.read_sql("select * from users", con=db_connection)
# print(users_df)

# how many female and male are using smark app
gender_count = users_df.groupby(by=['gender'])['id'].count()
# print(gender_count)

# average age of users
avg_age = users_df['age'].mean()
# print(avg_age)

# average female and male age
avg_age_f_m = round(users_df.groupby(['gender'])['age'].mean(),2)
# print(avg_age_f_m)

# print(users_df['gender'].unique())
# plt.bar(users_df['gender'].unique(), gender_count, color='maroon', width=0.4)
# plt.show()
x_axs = ['female', 'male']
plt.bar(x_axs, gender_count, color='maroon', width=0.4)
functions.add_labels(x_axs, gender_count)
plt.show()

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

# with db_connection.connect() as con:
#     results = con.execute('select users.gender from users where users.id in (select subscription_payments.user_id from subscription_payments where subscription_payments.subscription_type_id=1)')
#     res_list = []
#
#     for i in results:
#         res_list.append(i[0])

# print(res_list)
# print(res_list.count("M"))
# print(res_list.count("F"))
# people who have monthly subscription are 83 Males 63 Females

# with db_connection.connect() as con:
#     results = con.execute('select count(user_id), subscription_type_id from subscription_payments group by subscription_type_id')
#
#     for i in results:
#         print(i)

'select count(users.gender, subscription_type_id from )'