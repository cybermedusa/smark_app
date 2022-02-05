import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import functions
import numpy as np
import datetime

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
x_age_axs = [str(item) for item in range(18,61)]
y_age_axs = list(users_df.groupby(by=['age'])['id'].count())
# plt.bar(x_age_axs, y_age_axs, color='#A8E9A5')
# functions.add_labels_on_chart(x_age_axs, y_age_axs)
# plt.xticks(x_age_axs, rotation='vertical', fontsize='small')
# plt.xlabel('Age')
# plt.ylabel('Number of users')
# plt.vlines(str(avg_age), 0, 40, linestyles='dashed', colors='#35888F')
# plt.show()

# What is an average female and male age?
avg_age_f_m = round(users_df.groupby(['gender'])['age'].mean())
# print(avg_age_f_m)

# Bar chart presenting how many females and males have a smark app
# x_gender_axs = ['female', 'male']
# plt.bar(x_gender_axs, gender_count, color='#A8E9A5', width=0.4)
# functions.add_labels_on_chart(x_gender_axs, gender_count)
# plt.show()

# How many users have subscription?
subscription_users = pd.read_sql("select * from subscription_payments", con=db_connection)
count_subs_types = subscription_users.groupby(['subscription_type_id'])['id'].count()
total_num_of_sub_users = subscription_users['id'].count()
# print(count_subs_types)
# 1 - 146
# 2 - 144
# 3 - 110
# The most popular subscription type - month

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

    cmap = plt.colormaps['tab20c']
    outer_colors = cmap(np.arange(3)*4)
    inner_colors = cmap([1, 2, 5, 6, 9, 10])
    size = 0.3

    # plt.pie(np.array(functions.return_nest_sub_list(r1,r2,r3)).sum(axis=1),
    #         colors=outer_colors,
    #         autopct=lambda pct: functions.show_pct_int_pie_chart(pct, np.array(functions.return_nest_sub_list(r1,r2,r3)).sum(axis=1)),
    #         pctdistance=0.8,
    #         labels=['month', 'half-year', 'year'],
    #         labeldistance=1.05,
    #         radius=1,
    #         wedgeprops=dict(width=size, edgecolor='w'))
    #
    # plt.pie(np.array(functions.return_nest_sub_list(r1,r2,r3)).flatten(),
    #         autopct=lambda pct: functions.show_pct_int_pie_chart(pct, np.array(functions.return_nest_sub_list(r1,r2,r3)).flatten()),
    #         pctdistance=0.7,
    #         radius = 1 - size,
    #         colors=inner_colors,
    #         labels=('F', 'M')*3,
    #         labeldistance=0.9,
    #         wedgeprops=dict(width=size, edgecolor='w'))
    # plt.show()

with db_connection.connect() as con:
    res = con.execute('select users.gender from users where users.id in (select parking_time_payments.id from parking_time_payments where parking_time_payments.user_id >= 401)')
    non_sub_usr_lst = []
    for i in res:
        non_sub_usr_lst.append(i[0])

    f_non_sub_usr = non_sub_usr_lst.count('F')
    m_non_sub_usr = non_sub_usr_lst.count('M')

    # plt.pie([f_non_sub_usr, m_non_sub_usr], labels=['F', 'M'],
    # autopct=lambda pct: functions.show_pct_int_pie_chart(pct, [f_non_sub_usr,m_non_sub_usr])),
    # plt.show()

# How many people parked on specific day from 1-7 Nov?

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
sub_df = parking_df.loc[parking_df['type'] == 'non-subscription']
avg_sub_df = round(sub_df.groupby(['date'])['minutes'].mean())

non_sub_df = parking_df.loc[parking_df['type'] == 'subscription']

avg_non_sub_df = round(non_sub_df.groupby(['date'])['minutes'].mean())
plot_df = pd.DataFrame([avg_sub_df, avg_non_sub_df])
plot_df = plot_df.T
start_date = datetime.date(2021, 11, 0o1)
number_of_days = 14
date_list = [(start_date + datetime.timedelta(days = day)).isoformat() for day in range(number_of_days)]
x_axis = np.arange(1, len(date_list)+1)
days_range = [x for x in range(1,15)]
# plt.bar(x_axis-0.2, avg_sub_df, width=0.4, label='users with subscription')
# plt.bar(x_axis+0.2, avg_non_sub_df, width=0.4, label='users without subscription')
# plt.xticks(x_axis)
# plt.xlabel('2021-11-01 : 2021-11-14')
# plt.ylabel('Number of users')
# plt.legend()
# plt.show()

# add column where you calculate how much people paid for parking on specific day
city_district_df = pd.read_sql("select * from city_districts", con=db_connection)
join_df = pd.merge(parking_df, city_district_df[['fee', 'id']], left_on='city_district_id', right_on='id')
join_df['total_parking_cost_per_user'] = round((join_df['minutes']/60) * join_df['fee'],2)
join_sub_df = join_df.loc[join_df['type'] == 'subscription']
join_non_sub_df = join_df.loc[join_df['type'] == 'non-subscription']
# print(join_df.sort_values(by='total_parking_cost_per_user', ascending=False).head(10))
#avg, max, min cost in zl
avg_all_usr_parking_payment = join_df['total_parking_cost_per_user'].mean()
max_all_usr_parking_payment = join_df['total_parking_cost_per_user'].max()
min_all_usr_parking_payment = join_df['total_parking_cost_per_user'].min()

avg_sub_usr_parking_payment = join_sub_df['total_parking_cost_per_user'].mean()
max_sub_usr_parking_payment = join_sub_df['total_parking_cost_per_user'].max()
min_sub_usr_parking_payment = join_sub_df['total_parking_cost_per_user'].min()

avg_non_sub_usr_parking_payment = join_non_sub_df['total_parking_cost_per_user'].mean()
max_non_sub_usr_parking_payment = join_non_sub_df['total_parking_cost_per_user'].max()
min_non_sub_usr_parking_payment = join_non_sub_df['total_parking_cost_per_user'].min()

# Jakie samochody głównie parkują - elektryki czy nie-elektryki?
# cars_df = pd.read_sql("select * from cars", con=db_connection)
# group_ele_n_ele = cars_df.groupby(['type'])['id'].count()
# print(group_ele_n_ele)

# Jaka jest średnia ocena apki?
# rate_df = pd.read_sql('select * from rates', con=db_connection)
# avg_rate = round(rate_df['value'].mean(),2)
# print(avg_rate)


# W jakiej dzielnicy miasta parkuje najwięcej ludzi?
group_city_district_sub = join_sub_df.groupby(['city_district_id'])['id_x'].count()
# print(group_city_district_sub)
# Najwiecej subskrybentów parkuje na Zabłociu.

group_city_district_non_sub = join_non_sub_df.groupby(['city_district_id'])['id_x'].count()
# print(group_city_district_non_sub)
# Najwiecej nie-subskrybentow parkuje na Kazimierzu.

# Jaki jest sredni czas parkowania ludzi przed posiadaniem apki a jaki po?
# feedback_df = pd.read_sql('select * from feedbacks', con=db_connection)
# feedback_df['difference'] = feedback_df['time_before_app'] - feedback_df['time_after_app']
# print(feedback_df.sort_values(by='difference', ascending=False).head(50))
# avg time before app
# avg_time_before_app = feedback_df['time_before_app'].mean()
# print(avg_time_before_app)
# avg time after app
# avg_time_after_app = feedback_df['time_after_app'].mean()
# print(avg_time_after_app)

# Costs analysis
# Koszty posiadania pracowników na miesiąc
employees_df = pd.read_sql('select * from employees', con=db_connection)
employees_costs_df = pd.read_sql('select * from employees_costs', con=db_connection)

emp_total_costs = pd.merge(employees_costs_df, employees_df, left_on='employee_id', right_on='id')
salary_list = list(employees_df['salary'])
emp_total_costs_sum = sum(functions.count_total_emp_costs(salary_list))
# print(emp_total_costs_sum)

# Koszty zamówienia potrzebnych narzędzi do działania aplikacji
