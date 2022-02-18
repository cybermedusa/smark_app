import pandas as pd
from sqlalchemy import create_engine
import age_gender_distribution_stacked_bar, avg_max_min_pln_per_city_district
import parking_time_before_after_app, parking_time_distribution_sub_non_sub_comparison
import rate_heart, subscription_type_pie, users_registration_distribution
import users_parking_distribution_per_month_bar, profits_costs_distribution_per_months

pd.options.mode.chained_assignment = None

# Connection to the database
db_connection_str = 'mysql+pymysql://root:' + "******" + "@localhost:3306/smark"
db_connection = create_engine(db_connection_str)

# Age & gender distribution of all users
print(age_gender_distribution_stacked_bar)

# Subscription & non-subscription users distribution
print(subscription_type_pie)

# Registration distribution per months in 2021
print(users_registration_distribution)

# Users parking distribution per months
print(users_parking_distribution_per_month_bar)

# Users average parking time distribution per city district
print(parking_time_distribution_sub_non_sub_comparison)

# Avg, max, min parking cost per city district
print(avg_max_min_pln_per_city_district)

# Time needed to find parking spot before and after app
print(parking_time_before_after_app)

# Profits and costs distribution per months in 2021
print(profits_costs_distribution_per_months)

# Average app rate
print(rate_heart)


