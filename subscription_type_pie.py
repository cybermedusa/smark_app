import functions
from smark_app import db_connection
import numpy as np
import matplotlib.pyplot as plt

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

    cmap = plt.colormaps['tab20b']
    outer_colors = cmap(np.arange(3)*4)
    inner_colors = cmap([1, 2, 5, 6, 9, 10])
    size = 0.3

    textprops = dict(size=8,
                     fontstyle='oblique',
                     fontweight='bold')

    plt.pie(np.array(functions.return_nest_sub_list(r1,r2,r3)).sum(axis=1),
            colors=outer_colors,
            autopct=lambda pct: functions.show_pct_int_pie_chart(pct, np.array(functions.return_nest_sub_list(r1,r2,r3)).sum(axis=1)),
            pctdistance=0.8,
            labels=['month', 'half-year', 'year'],
            labeldistance=1.05,
            radius=1,
            wedgeprops=dict(width=size, edgecolor='w'),
            textprops=textprops)

    plt.pie(np.array(functions.return_nest_sub_list(r1,r2,r3)).flatten(),
            autopct=lambda pct: functions.show_pct_int_pie_chart(pct, np.array(functions.return_nest_sub_list(r1,r2,r3)).flatten()),
            pctdistance=0.7,
            radius=1 - size,
            colors=inner_colors,
            labels=('F', 'M')*3,
            labeldistance=0.9,
            wedgeprops=dict(width=size, edgecolor='w'),
            textprops=textprops)

    plt.title('Gender & subscription distribution of users with subscription')
    plt.show()