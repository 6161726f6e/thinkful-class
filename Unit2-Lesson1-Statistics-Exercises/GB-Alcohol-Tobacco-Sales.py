import pandas as pd
from scipy import stats

# format data
data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()
data = [i.split(',') for i in data]

# put data into df

column_names = data[0]  # first row
data_rows = data[1::]  # all following rows
df = pd.DataFrame (data_rows, columns=column_names)

# convert data to float
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

# perform calculations
print('The Alcohol Mean is ')
print(df['Alcohol'].mean())
print('The Alcohol Median is ')
print(df['Alcohol'].median())
print('The Alcohol Mode is ')
print(stats.mode(df['Alcohol']))
print('The Alcohol Range is ')
print(max(df['Alcohol']) - min(df['Alcohol']))
print('The Alcohol Variance is ')
print(df['Alcohol'].var())
print('The Alcohol Std Dev is ')
print(df['Alcohol'].std())
print('********************************************')
print('The Tobacco Mean is ')
print(df['Tobacco'].mean())
print('The Tobacco Median is ')
print(df['Tobacco'].median())
print('The Tobacco Mode is ')
print(stats.mode(df['Tobacco']))
print('The Tobacco Range is ')
print(max(df['Tobacco']) - min(df['Tobacco']))
print('The Tobacco Variance is ')
print(df['Tobacco'].var())
print('The Tobacco Std Dev is ')
print(df['Tobacco'].std())

