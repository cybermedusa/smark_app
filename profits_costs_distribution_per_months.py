import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import functions
from smark_app import db_connection, subscription_users, parking_non_sub_df, parking_df

# Costs analysis
# Koszty posiadania pracowników na rok 2021
employees_df = pd.read_sql('select * from employees', con=db_connection)
employees_costs_df = pd.read_sql('select * from employees_costs', con=db_connection)

emp_total_costs = pd.merge(employees_costs_df, employees_df, left_on='employee_id', right_on='id')
salary_list = list(employees_df['salary'])
emp_total_costs_sum = sum(functions.count_total_emp_costs(salary_list))
# print(salary_list)

# Koszty zamówienia potrzebnych narzędzi do działania aplikacji
tools_df = pd.read_sql('select * from tools', con=db_connection)
tools_costs_df = pd.read_sql('select * from tools_costs', con=db_connection)
tools_costs_join = pd.merge(tools_df, tools_costs_df, left_on='id', right_on='tool_id')
tools_costs_join['quantity*price'] = tools_costs_join['price_per_item'] * tools_costs_join['quantity']
tools_costs_join['date'] = pd.to_datetime(tools_costs_join['date'])
grouped_tools_costs = tools_costs_join.groupby(pd.Grouper(key='date', freq='M'))['quantity*price'].sum()
# print(grouped_tools_costs)

# Monthly costs distribution
emp_total_costs['date'] = pd.to_datetime(emp_total_costs['date'])
grouped_employees_costs = emp_total_costs.groupby(pd.Grouper(key='date', freq='M'))['salary'].sum()
# print(grouped_employees_costs)
total_costs = grouped_employees_costs.add(grouped_tools_costs, fill_value=0)
# print(total_costs)

# Monthly profits distribution

# Profits from subscription users (30% of each subscription purchase)
subscription_type_df = pd.read_sql('select * from subscription_types', con=db_connection)
merge_sub = pd.merge(subscription_users, subscription_type_df, left_on='subscription_type_id', right_on='id')
merge_sub['profit_per_each_purchase'] = merge_sub['price'] * 0.3
# print(merge_sub.columns)
merge_sub['date'] = pd.to_datetime(merge_sub['date'])
grouped_merge_sub = merge_sub.groupby(pd.Grouper(key='date', freq='M'))['profit_per_each_purchase'].sum()
# print(grouped_merge_sub)

# Profits from non - subscription users
parking_non_sub_df['profit_per_each_purchase'] = parking_non_sub_df['total_parking_cost_per_user'] * 0.35
parking_non_sub_df['date'] = pd.to_datetime(parking_non_sub_df['date'])
grouped_parking_non_sub = parking_non_sub_df.groupby(pd.Grouper(key='date', freq='M'))['total_parking_cost_per_user'].sum()
# print(grouped_parking_non_sub)

total_profits = grouped_parking_non_sub.add(grouped_merge_sub)
# print(total_profits)

x = [1,2,3,4,5,6,7,8,9,10,11,12]
costs_profits_merged = functions.merge_lists(total_costs, total_profits)
x_axs_merged = functions.merge_lists(x,x)

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
plt.plot(x, total_costs, color='red', label='costs')
plt.plot(x, total_profits, color='green', label='profits')
plt.ylabel('PLN')
plt.xticks(x, months)
plt.title('Profits & costs distribution per months in 2021')
plt.legend()
for i in range(0, len(x)):
    plt.plot(x_axs_merged[i], costs_profits_merged[i], linestyle='dashed', color='#E6E6E6')
new_x = np.arange(1, 13)
ct = 0
for z, y in zip(new_x, data_label):
    label = str(functions.count_distance(costs_profits_merged)[ct])
    plt.annotate(text=label, xy=(z, y), ha='center', size='small', fontstyle='oblique', fontweight='bold')
    ct += 1
plt.show()
