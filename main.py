# Pandas: Convert GroupBy results to Dictionary of Lists

import pandas as pd

df = pd.DataFrame({
    'Animal': ['Cat', 'Cat', 'Cat', 'Dog', 'Dog', 'Dog'],
    'Max Speed': [25, 35, 45, 55, 65, 75]
})

print(df)

a_dict = df.groupby('Animal')['Max Speed'].apply(list).to_dict()

print('-' * 50)

# 👇️ {'Cat': [25, 35, 45], 'Dog': [55, 65, 75]}
print(a_dict)