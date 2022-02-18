import pandas as pd
from sqlalchemy import create_engine

pd.options.mode.chained_assignment = None

# Connection to the database
db_connection_str = 'mysql+pymysql://root:' + "*********" + "@localhost:3306/smark"
db_connection = create_engine(db_connection_str)

# Age & gender distribution of all users
# age_gender_distribution_stacked_bar.py

# Subscription & non-subscription users distribution
# subscription_type_pie.py

# Registration distribution per months in 2021
# users_registration_distribution

# Users parking distribution per months
# users_parking_distribution_per_month_bar.py

# Users average parking time distribution per city district
# parking_time_distribution_sub_non_sub_comparison

# Avg, max, min parking cost per city district
# avg_max_min_pln_per_city_district

# Time needed to find parking spot before and after app
# parking_time_before_after_app.py

# Profits and costs distribution per months in 2021
# profits_costs_distribution_per_month.py

# Average app rate
# rate_heart.py


