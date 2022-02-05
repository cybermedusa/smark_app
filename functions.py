import matplotlib.pyplot as plt
import numpy as np

def add_labels_on_chart(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], fontsize=6, ha='center')

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


