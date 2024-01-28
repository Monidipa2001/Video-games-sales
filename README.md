# Video-games-sales
This repository contains code and data for analysing and visualising video game sales. The dataset used includes information on various video games, such as sales figures, genres, platforms, and release dates.

**IMPORTING DATA**

import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv(r'Video_Game_Sales_as_of_Jan_2017.csv')
df

**BAR CHART**

import pandas as pd
import matplotlib.pyplot as plt
file_path = 'Video_Game_Sales_as_of_Jan_2017.csv'
df = pd.read_csv(file_path)

total_sales_by_genre = df.groupby('Genre')['Global_Sales'].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.bar(total_sales_by_genre['Genre'], total_sales_by_genre['Global_Sales'], color='skyblue')
plt.xlabel('Genre')
plt.ylabel('Total Global Sales (in millions)')
plt.title('Total Sales by Genre')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

**LINE CHART**

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Video_Game_Sales_as_of_Jan_2017.csv')

df['Year_of_Release'] = pd.to_datetime(df['Year_of_Release'], errors='coerce')

df.set_index('Year_of_Release', inplace=True)
sales_by_year = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].resample('Y').sum()

plt.figure(figsize=(12, 6))
plt.plot(sales_by_year.index, sales_by_year['NA_Sales'], marker='o', label='NA_Sales', color='b')
plt.plot(sales_by_year.index, sales_by_year['EU_Sales'], marker='o', label='EU_Sales', color='g')
plt.plot(sales_by_year.index, sales_by_year['JP_Sales'], marker='o', label='JP_Sales', color='r')
plt.plot(sales_by_year.index, sales_by_year['Other_Sales'], marker='o', label='Other_Sales', color='c')
plt.plot(sales_by_year.index, sales_by_year['Global_Sales'], marker='o', label='Global_Sales', color='m')

plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales Trend Over Years')
plt.legend()
plt.grid(True)
plt.show()

**SCATTER PLOT**

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Video_Game_Sales_as_of_Jan_2017.csv')  

variable1 = 'User_Count'
variable2 = 'Global_Sales'

plt.figure(figsize=(12, 6))
plt.scatter(df[variable1], df[variable2], alpha=0.5, color='pink')
plt.title(f'Scatter Plot: {variable1} vs {variable2}')
plt.xlabel(variable1)
plt.ylabel(variable2)
plt.grid(True)
plt.show()

**PIE CHART**

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Video_Game_Sales_as_of_Jan_2017.csv')  
total_sales_by_genre = df.groupby('Genre')['Global_Sales'].sum().reset_index()

plt.figure(figsize=(8, 8))
plt.pie(total_sales_by_genre['Global_Sales'], labels=total_sales_by_genre['Genre'], autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Total Sales by Product Category')
plt.show()

**HEATMAP**

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Video_Game_Sales_as_of_Jan_2017.csv')

selected_columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales',
                    'Critic_Score', 'Critic_Count', 'User_Score', 'User_Count']

correlation_matrix = df[selected_columns].corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()

**TREEMAP**

import pandas as pd
import plotly.express as px

df = pd.read_csv('Video_Game_Sales_as_of_Jan_2017.csv') 

fig = px.treemap(df, path=['Genre'], values='Global_Sales', title='Treemap of Sales by Product Categories')
fig.show()

**BOXPLOT**

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Video_Game_Sales_as_of_Jan_2017.csv')

plt.figure(figsize=(12, 8))
sns.boxplot(y='Global_Sales', data=df)
plt.title('Box Plot of Global Sales')
plt.ylabel('Global Sales')
plt.show()

**BUBBLE CHART**

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Video_Game_Sales_as_of_Jan_2017.csv')
selected_column = 'NA_Sales'

plt.figure(figsize=(12, 8))
sns.scatterplot(x=selected_column, y='EU_Sales', data=df, alpha=0.7, palette='viridis')
plt.title(f'Scatter Plot of {selected_column} vs EU_Sales')
plt.xlabel(selected_column)
plt.ylabel('EU_Sales')
plt.show()

**HISTOGRAM**

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Video_Game_Sales_as_of_Jan_2017.csv') 
selected_category = 'Sports'
selected_category_data = df[df['Genre'] == selected_category]

plt.figure(figsize=(10, 6))
plt.hist(selected_category_data['Platform'], bins=20, color='skyblue', edgecolor='black')
plt.title(f'Histogram of Platform for {selected_category}')
plt.xlabel('Platform')
plt.ylabel('Frequency')
plt.xticks(rotation=90)
plt.show()

**WORD CLOUD**

from wordcloud import WordCloud
import matplotlib.pyplot as plt

text_data = " ".join(pd.read_csv('Video_Game_Sales_as_of_Jan_2017.csv')['Name'])  

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Key Terms')
plt.show()
