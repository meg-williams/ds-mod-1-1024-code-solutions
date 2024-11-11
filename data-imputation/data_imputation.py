# -*- coding: utf-8 -*-
"""data_imputation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ID11-E29KSc7JHCEsQow0sGMVAe0kQ7a

**Why is it important to handle null values in datasets?**

Because most programs or machine learning algorithms cannot deal with null values. In addition missing values can bias your data or lead to in acturate pridictions.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')
df

df.isna().sum()

df['Age_med'] = df_age['Age'].fillna(df_age['Age'].mean())

df.groupby('Sex')['Age'].mean()

apply(lambda x: if x == 'male': 1 else 0)

df['Age_mean_sex'] = df.groupby('Sex', group_keys=False)['Age'].apply(lambda x: x.fillna(x.mean()))

df

df['Cabin'] = df['Cabin'].fillna('unknown')

df.isna().sum()

"""I used arbitrary value imputation. Given that this column is
categorical mean and median cannot be used but more
importantly 687 of the Cabin values are null. Since there are
only 891 rows that means well over half do not have a value for
 Cabin and therefore we cannot draw any patterns or observations
with any degree of confidence.
"""
