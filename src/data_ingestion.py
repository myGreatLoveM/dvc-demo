import os
import numpy as np
import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv')

df = df.iloc[:, 4:]

df = df[df['Length of Membership'] > 1]

df.to_csv(os.path.join("data", "customers.csv"))
