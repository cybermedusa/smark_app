from smark_app import db_connection
import matplotlib.pyplot as plt
import functions

with db_connection.connect() as con:
    type = "non-subscription"
    res = con.execute('select users.gender from users where users.id in (select parking_time_payments.parking_id from parking_time_payments where parking_id in (select parking.id from parking where parking.type=%s))', type)
    non_sub_usr_lst = []
    for i in res:
        non_sub_usr_lst.append(i[0])

    f_non_sub_usr = non_sub_usr_lst.count('F')
    m_non_sub_usr = non_sub_usr_lst.count('M')
    f_m_list = [f_non_sub_usr, m_non_sub_usr]

    textprops = dict(horizontalalignment="center",
                     verticalalignment="top",
                     size=8,
                     fontstyle='oblique',
                     fontweight='bold')

    plt.pie([f_non_sub_usr, m_non_sub_usr], labels=['F', 'M'], colors=['#44779A', '#7DFAC2'],
            autopct=lambda pct: functions.show_pct_int_pie_chart(pct, [f_non_sub_usr, m_non_sub_usr]),
            textprops=textprops)

    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.title('Gender distribution of users without subscription')
    plt.show()