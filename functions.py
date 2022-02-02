import matplotlib.pyplot as plt

def add_labels_on_chart(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], fontsize=6, ha='center')

def append_results_to_lists(list_with_results, empty_list):
    for i in list_with_results:
        empty_list.append(i[0])

def print_sub_output(sub_result_list, sub_type):
    return f"Number of females and males who has {sub_type} subscription: {str([[res, sub_result_list.count(res)] for res in set(sub_result_list)])}"

