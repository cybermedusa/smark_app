import matplotlib.pyplot as plt
import numpy as np
import math

def add_labels_on_chart(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], fontsize=8, ha='center', fontweight='bold', fontstyle='oblique')

def append_results_to_lists(list_with_results, empty_list):
    for i in list_with_results:
        empty_list.append(i[0])

def print_sub_output(sub_result_list, sub_type):
    return f"{sub_type} subscription: {str([[res, sub_result_list.count(res)] for res in set(sub_result_list)])}"

def show_pct_int_pie_chart(pct_val, int_val):
    absolute_val = int(round(pct_val/100.*np.sum(int_val)))
    return absolute_val

def return_nest_sub_list(l1, l2, l3):
    x1 = [[res, l1.count(res)] for res in set(l1)]
    x2 = [[res, l2.count(res)] for res in set(l2)]
    x3 = [[res, l3.count(res)] for res in set(l3)]
    f1 = x1[0][1]
    f2 = x2[0][1]
    f3 = x3[0][1]
    m1 = x1[1][1]
    m2 = x2[1][1]
    m3 = x3[1][1]
    f_m_lst = list([[f1,m1],[f2,m2],[f3,m3]])
    return f_m_lst

def count_total_emp_costs(salary_list):
    emp_total_cost_lst = []
    for i in salary_list:
        total_cost = round(i+i*0.0976+i*0.065+i*0.0167+i*0.0245+i*0.001)
        emp_total_cost_lst.append(total_cost)
    return emp_total_cost_lst

def return_avg_min_max_all_types(df):
    avg_all_usr_parking_time = round(df['minutes'].mean(), 2)
    max_all_usr_parking_time = round(df['minutes'].max(), 2)
    min_all_usr_parking_time = round(df['minutes'].min(), 2)
    return f"avg: {avg_all_usr_parking_time}\nmax: {max_all_usr_parking_time}\nmin: {min_all_usr_parking_time}"

def return_avg_min_max_sub(df):
    avg_sub_usr_parking_time = round(df['minutes'].mean(), 2)
    max_sub_usr_parking_time = round(df['minutes'].max(), 2)
    min_sub_usr_parking_time = round(df['minutes'].min(), 2)
    return f"avg: {avg_sub_usr_parking_time}\nmax: {max_sub_usr_parking_time}\nmin: {min_sub_usr_parking_time}"

def return_avg_min_max_non_sub(df):
    avg_non_sub_usr_parking_time = round(df['minutes'].mean(), 2)
    max_non_sub_usr_parking_time = round(df['minutes'].max(), 2)
    min_non_sub_usr_parking_time = round(df['minutes'].min(), 2)
    return f"avg: {avg_non_sub_usr_parking_time}\nmax: {max_non_sub_usr_parking_time}\nmin: {min_non_sub_usr_parking_time}"

def return_avg_min_max_non_sub_payment(df):
    grouped_avg = round(df.groupby('city_district_id')['total_parking_cost_per_user'].mean(), 2)
    grouped_max = round(df.groupby('city_district_id')['total_parking_cost_per_user'].max(), 2)
    grouped_min = round(df.groupby('city_district_id')['total_parking_cost_per_user'].min(), 2)
    # avg_non_sub_usr_parking_payment = round(df['total_parking_cost_per_user'].mean(), 2)
    # max_non_sub_usr_parking_payment = round(df['total_parking_cost_per_user'].max(), 2)
    # min_non_sub_usr_parking_payment = round(df['total_parking_cost_per_user'].min(), 2)
    # return f"avg: {avg_non_sub_usr_parking_payment}\nmax: {max_non_sub_usr_parking_payment}\nmin: {min_non_sub_usr_parking_payment}"
    return grouped_avg, grouped_max, grouped_min

def count_distance(list_of_tuples):
    results = []
    for i in list_of_tuples:
        distance = round((i[1] - i[0]), 2)
        results.append(distance)
    return results

def merge_lists(list1, list2):
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list
