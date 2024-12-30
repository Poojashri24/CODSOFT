import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
df = pd.read_csv("C:\\Users\\pooja\\OneDrive\\ドキュメント\\IMDb Movies India.csv")

