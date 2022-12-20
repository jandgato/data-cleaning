import numpy as np
import pandas as pd

exp_vida_df = pd.read_csv("/datasets/Life expectancy.csv")
taza_suic_df = pd.read_csv("/datasets/Suicide Rate.csv")

percent_missing = exp_vida_df.isnull().sum() * 100 / len(exp_vida_df)
missing_value_df = pd.DataFrame({'column_name': exp_vida_df.columns,
                                 'percent_missing': percent_missing})
missing_value_df.sort_values('percent_missing', ascending=False).style.background_gradient(cmap='Accent')