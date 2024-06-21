# preproccesing and cleaning techniques

# always make a copy of the dataframe before starting the cleaning process to prevetnt lose data

import sys
sys.exit
# 1)
# -----------------------*----------------*----------------*------*-------*--------------*------------------------*-----------------------------
# converting numbers with ending as k, m, l to numeric values from the not required sting data type as string cannot be used for numerical 
# operations and analysis
# .apply() method is used to apply a function to each element in a DataFrame or Series. 

import pandas as pd
# Example data
data = {
    'salary': ['17.3k', '25.5k', '1.2M', '500', '45.7k', '900']
}
df = pd.DataFrame(data)

# Function to convert salary string to numeric value
def convert_salary(s):
    if isinstance(s, str):
        multiplier = 1
        if s[-1].lower() == 'k':
            multiplier = 1_000
            s = s[:-1]
        elif s[-1].lower() == 'm':
            multiplier = 1_000_000
            s = s[:-1]
        try:
            return float(s) * multiplier
        except ValueError:
            return pd.NA
    return pd.NA

# Apply the conversion function to the salary column
df['salary'] = df['salary'].apply(convert_salary)

# Print the cleaned DataFrame
print(df)

# 2)
# -----------------------*----------------*----------------*------*-------*--------------*------------------------*-----------------------------
# remove any other notations used for representing empty value like [ '--' or 'na' or '-' or 'nan' ] to np.nan
# as NaN is the standard representation for missing values in pandas. This makes it easier to handle missing values in a DataFrame.
import pandas as pd
import numpy as np

# Example DataFrame
data = {
    'Jobs': ['--', '10', '20', '--', '30'],
    'Salaries': ['50k', '--', '70k', '80k', '--']
}
df = pd.DataFrame(data)

# Replace '--' with NaN in the 'Jobs' column
df['Jobs'] = df['Jobs'].replace('--', np.nan)
# Replace '--' with NaN in the entire DataFrame
df = df.replace('--', np.nan)
print(df)

# 3)
# -----------------------*----------------*----------------*------*-------*--------------*------------------------*-----------------------------
# melt function is used to transform or reshape data from wide to long format.
pd.melt(df, id_vars=['column1', 'column2'], value_vars=['column3', 'column4'], var_name='new_column_name', value_name='new_value_name')
# basically unpivots the whole table around the id_vars and creates a new column for the variable names and a new column for the values.
# id_vars: columns to keep as is
# value_vars: columns to melt
# var_name: name of the new column for the variable names
# value_name: name of the new column for the values

# 3)
# -----------------------*----------------*----------------*------*-------*--------------*------------------------*-----------------------------
# if a data is represents range given in string fromat and u need to separate the range in different columns then
treatment['start'], treatment['end'] = treatment['range'].str.split('-', 1).str
# eg : range is '10mg-20mg' then after spliting it will be '10mg' and '20mg' stored in rows of start and end columns respectively

# 4)
# -----------------------*----------------*----------------*------*-------*--------------*------------------------*-----------------------------
perform feature engineering like - converting categorical data [gender = male / female] to numerical data [0 / 1] if it categorical data
makes it difficult to perform ML algortithms on data using map function
# map function is used to map the values of a Series to another set of values.
# Syntax: Series.map(dict)

# 5)
# -----------------------*----------------*----------------*------*-------*--------------*------------------------*-----------------------------
# use crosstabs to find the relationship between two columns and perfrom bivariate analysis, with respect to lambada func define action
pd.crosstab(df['column1'], df['column2']).apply(lambda r: r/r.sum(), axis=1)

# 6)
# -----------------------*----------------*----------------*------*-------*--------------*------------------------*-----------------------------
# use pairplot and heatmap (correlation) to find the relationship between the columns and perform analysis
sns.pairplot(df)
sns.heatmap(df.corr(), annot=True) # shows correlation between two columns gives  idea how they can be related or connected to each other

# 7)
# -----------------------*----------------*----------------*------*-------*--------------*------------------------*-----------------------------
# plot a distplot to see normal distribution drift and get an idea about skewness and kurtosis 
skewness and kurtosis gives an idea about outliers which are harmful to th e data

skewness :
# In a positively skewed distribution, the mean is typically greater than the median because the few high values pull the mean to the right.
# In a negatively skewed distribution, the mean is typically less than the median because the few low values pull the mean to the left.
Impact on Statistical Analysis:
Skewed data can affect the assumptions of various statistical methods, such as regression analysis, which often assume normally distributed residuals.
It may necessitate data transformation (e.g., log transformation) to normalize the data.

kurtosis :
# indicates the presence of outliers and the extremity of those outliers in a dataset. 
# Unlike skewness, which measures asymmetry,kurtosis measures the "tailedness" of the distribution.
A high kurtosis value indicates that the distribution has heavy tails or outliers, while a low kurtosis value indicates that the distribution has
light tails or lacks outliers.
Statistical Analysis:
Distributions with high kurtosis may violate assumptions of certain statistical models, which assume normality.

# 8)
# -----------------------*----------------*----------------*------*-------*--------------*------------------------*-----------------------------
# use boxplot to identify outliers in the data.........far away from the whiskers are outliers
outlier in numerical data can be identified by using boxplot, numerical and IQR method :
numerical method :
1. 99.7% of the data lies within [mean-(3*SD)] and [mean+(3*SD)] in a normal distribution.
2. anything beyond 3*standard deviations is considered an outlier.
IQR method :
1. Calculate the first quartile (Q1) and third quartile (Q3) of the data.
2. Calculate the interquartile range (IQR) as Q3 - Q1.
3. Identify outliers as values below [Q1 - 1.5 * IQR] or above [Q3 + 1.5 * IQR].

outlier in categorical data can be identified by using frequency method :
1. Identify the frequency of each category in the column.
2. Categories with less frequency are considered outliers. eg : male=1000 and female=3 then might as well exclude females as outliers


eg outlier handling : df = df[df[age]<df['age'].quantile(0.95)] # removes the top 5% of the data
df = df[df[age]<df['age'].mean()+(3*df['age'].std())] # removes the data beyond 3 standard deviations from the mean

a = np.percentile(df['fare'], 25)
b = np.percentile(df['fare'], 75)
outlier_lower = a - 1.5*(b-a)
outlier_upper = b + 1.5*(b-a)
df = df[(df['fare'] > outlier_lower) & (df['fare'] < outlier_upper)]

# 9)
# -----------------------*----------------*----------------*------*-------*--------------*------------------------*-----------------------------
# use z-score to identify outliers in the data
# Z-score is a measure of how many standard deviations a data point is from the mean.
# Z-score = (X - μ) / σ
# X = data point, μ = mean, σ = standard deviation
# Z-scores can be used to identify outliers by setting a threshold value, typically 2.5 or 3.
# Data points with a Z-score greater than the threshold are considered outliers.
# Z-scores can be calculated using the zscore() function from the scipy.stats module.
from scipy.stats import zscore
df['z_score'] = zscore(df['column'])
outliers = df[df['z_score'].abs() > 3]  # threshold value of 3

# 10)
# -----------------------*----------------*----------------*------*-------*--------------*------------------------*-----------------------------
# use one hot encoding to convert categorical data to numerical data
pd.get_dummies(data = df, collumns=['sex', 'embarked', 'pclass'], drop_first=True) # drop_first=True to avoid dummy variable trap
we drop the first occurence as 3 columns can be represented by just 2 column 
eg: cities = ['New York', 'London', 'Paris']
now if we hv colmns NY and Paris and both values 0 then it is London , here we dont need to have 3rd column representing London separately