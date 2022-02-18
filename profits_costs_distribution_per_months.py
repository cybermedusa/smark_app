import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import functions
from smark_app import db_connection
from avg_max_min_pln_per_city_district import parking_non_sub_df

# Employees dataframe
employees_df = pd.read_sql('select * from employees', con=db_connection)

# Employees costs dataframe
employees_costs_df = pd.read_sql('select * from employees_costs', con=db_connection)

# Employees df & employees_costs df merged
emp_costs_merged = pd.merge(employees_costs_df, employees_df, left_on='employee_id', right_on='id')
emp_costs_merged['date'] = pd.to_datetime(emp_costs_merged['date'])

salary_list = list(employees_df['salary'])

# Returns salary list after adding contributions
emp_costs_merged_sum = sum(functions.count_total_emp_costs(salary_list))

# Employees costs grouped by months
grouped_employees_costs = emp_costs_merged.groupby(pd.Grouper(key='date', freq='M'))['salary'].sum()

# Tools dataframe
tools_df = pd.read_sql('select * from tools', con=db_connection)

# Tools costs dataframe
tools_costs_df = pd.read_sql('select * from tools_costs', con=db_connection)

# Tools df & tools_costs df merged
tools_costs_merged = pd.merge(tools_df, tools_costs_df, left_on='id', right_on='tool_id')

# Added column 'quantity * price'
tools_costs_merged['quantity*price'] = tools_costs_merged['price_per_item'] * tools_costs_merged['quantity']

tools_costs_merged['date'] = pd.to_datetime(tools_costs_merged['date'])

# Tools costs grouped by months
grouped_tools_costs = tools_costs_merged.groupby(pd.Grouper(key='date', freq='M'))['quantity*price'].sum()

# Tools costs & employees costs combined together
total_costs = grouped_employees_costs.add(grouped_tools_costs, fill_value=0)

# Subscription type dataframe
subscription_type_df = pd.read_sql('select * from subscription_types', con=db_connection)

subscription_users = pd.read_sql("select * from subscription_payments", con=db_connection)

# Subscription users df & subscription type df merged
subscription_users_type_merged = pd.merge(subscription_users, subscription_type_df, left_on='subscription_type_id', right_on='id')

# Added column 'profit_per_each_purchase' for subscription users
subscription_users_type_merged['profit_per_each_purchase'] = subscription_users_type_merged['price'] * 0.3

subscription_users_type_merged['date'] = pd.to_datetime(subscription_users_type_merged['date'])

# Subscription_users_type_merged grouped by months
grouped_subscription_users_type_merged = subscription_users_type_merged.groupby(pd.Grouper(key='date', freq='M'))['profit_per_each_purchase'].sum()

# Added column 'profit_per_each_purchase' for non-subscription users
parking_non_sub_df['profit_per_each_purchase'] = parking_non_sub_df['total_parking_cost_per_user'] * 0.35

parking_non_sub_df['date'] = pd.to_datetime(parking_non_sub_df['date'])

# Non-subscription users grouped by months
grouped_parking_non_sub = parking_non_sub_df.groupby(pd.Grouper(key='date', freq='M'))['total_parking_cost_per_user'].sum()

# Subscription users & non-subscription users profits combined together
total_profits = grouped_parking_non_sub.add(grouped_subscription_users_type_merged)

months_costs_profits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Costs & profits merged
costs_profits_merged = functions.merge_lists(total_costs, total_profits)

x_axs_merged = functions.merge_lists(months_costs_profits, months_costs_profits)

cord_1 = (1, functions.count_distance(costs_profits_merged)[0]/2)

data_label = []
count = 0

for j in functions.count_distance(costs_profits_merged):
    if j < 0:
        data_label.append(round(abs((j/2)) + total_profits[count]))
        count += 1
    else:
        data_label.append(round(abs((j/2)) + total_costs[count]))
        count += 1

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.plot(months_costs_profits,
         total_costs,
         color='red',
         label='costs')

plt.plot(months_costs_profits,
         total_profits,
         color='green',
         label='profits')

plt.ylabel('PLN')
plt.xticks(months_costs_profits, months)
plt.title('Profits & costs distribution per months in 2021')
plt.legend()

for i in range(0, len(months_costs_profits)):
    plt.plot(x_axs_merged[i],
             costs_profits_merged[i],
             linestyle='dashed',
             color='#E6E6E6')

new_x = np.arange(1, 13)
count = 0

for z, y in zip(new_x, data_label):
    label = str(functions.count_distance(costs_profits_merged)[count])
    plt.annotate(text=label, xy=(z, y), ha='center', size='small', fontstyle='oblique', fontweight='bold')
    count += 1

plt.show()
