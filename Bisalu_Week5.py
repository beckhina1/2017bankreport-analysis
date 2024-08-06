# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_excel('C:\\Users\\patri\\Downloads\\top100banks2017-12-31.xlsx')

df.head()
df.tail()
df.sample(10)
 # Data Prep and Cleaning
df.info()
print(df.shape)
df.describe().T
df.isnull().sum()
df.dtypes
#### The top 100 banks data ranging from 2016-12-31 to 2017-12-31 contains 120 entries with 5 attributes. It includes banks names, ranking, country, total assets and balance sheet.Df contains both numerical (rank and total assets_us_b) and categorical variables(bank, country,balance sheet 'period'). The dataset included 120 banks, with ranks ranging from 1 to 120, and total assets ranging from  201.192𝑏𝑖𝑙𝑙𝑖𝑜𝑛𝑡𝑜
 4005.58 billion, with an average of $832.298 billion. The balance sheet dates predominantly fall on December 31, 2017, with a few entries from the previous year, and the ranking distribution is centered around a median of 60.5.

# Bank overview
### To familiariaze ourselves with the data, I am going to find out who the top 10 banks are based on their total assets, and focusing on those institutions for my presentations.
# 1. Bar Plot of the Top 10 Banks by Total Assets
top_10_banks = df.nlargest(10, 'total_assets_us_b')
plt.figure(figsize=(10, 6))
plt.bar(top_10_banks['bank'], top_10_banks['total_assets_us_b'], color='skyblue')
plt.xlabel('Bank Name')
plt.ylabel('Total Assets (in billions)')
plt.title('Top 10 Banks by Total Assets')
plt.xticks(rotation=90, va="center")
plt.tight_layout()
plt.savefig('top_10_banks_by_assets.png')
plt.show()

# 2. Line Plot of the Market Share of the Top 10 Banks

top_10_banks['Market Share'] = (top_10_banks['total_assets_us_b'] / top_10_banks['total_assets_us_b'].sum()) * 100
plt.figure(figsize=(10, 6))
plt.plot(top_10_banks['bank'], top_10_banks['Market Share'], marker='o', linestyle='-', color='orange')
plt.xlabel('Bank Name')
plt.ylabel('Market Share (%)')
plt.title('Market Share of the Top 10 Banks')
plt.xticks(rotation=90, va="center")
plt.tight_layout()
plt.savefig('market_share_top_10_banks.png')
plt.show()

# 3. Scatter Plot of Total Assets vs. rank
plt.figure(figsize=(10, 6))
plt.scatter(df['total_assets_us_b'], df['rank'], color='green')
plt.xlabel('Total Assets (in billions)')
plt.ylabel('Rank')
plt.title('Total Assets vs. Rank')
plt.tight_layout()
plt.savefig('assets_vs_rank.png')
plt.show()

# 4. Heatmap of Total Assets by Country
# Group data by country and sum total assets
country_assets = df.groupby('country')['total_assets_us_b'].sum().reset_index()
country_assets = country_assets.sort_values(by='total_assets_us_b', ascending=False)
plt.figure(figsize=(12, 8))
plt.imshow([country_assets['total_assets_us_b']], cmap='YlGnBu', aspect='auto')
plt.colorbar(label='Total Assets (in billions)')
plt.xlabel('Country')
plt.ylabel('Total Assets (in billions)')
plt.title('Heatmap of Total Assets by Country')
plt.xticks(range(len(country_assets['country'])), country_assets['country'], rotation=45)
plt.yticks([])





