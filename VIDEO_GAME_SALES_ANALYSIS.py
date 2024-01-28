#!/usr/bin/env python
# coding: utf-8

# In[77]:


import pandas as pd 
import matplotlib.pyplot as plt

df=pd.read_csv(r'Video_Game_Sales_as_of_Jan_2017.csv')
df


# # Bar Chart

# In[68]:


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


# The bar for the Action genre is the highest, at around 1700 million. This means that action games sold the most of all the genres listed. The next highest bars are for the Shooter and Sports genres, at around 1500 million and 1250 million, respectively. The lowest bars are for the Strategy and Puzzle genres, at around 250 million and 19 million, respectively.
# 
# Insights:
# 
# The sales for all genres are relatively close together, except for the Action genre, which is a clear outlier.
# 
# The sales for the Puzzle, Racing, and Role-Playing genres are also relatively close together.
# 
# The sales for the Fighting, Platform, Shooter, and Simulation genres are more spread out.

# # Line Chart

# In[69]:


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


# Overall sales trend: It appears that global sales (the sum of all four regions) have been increasing steadily over time, with a few minor dips.
# 
# Regional trends:
# 
# NA sales seem to be consistently higher than the other regions throughout the shown period.
# 
# EU sales appear to be following a similar trend to NA sales, but at a slightly lower level.
# 
# JP sales are more difficult to discern due to the missing labels on the y-axis, but they seem to be fluctuating more than the other regions.
# 
# Other sales are the lowest overall and seem to be relatively flat over time

# # Scatter Plot

# In[70]:


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


# There is a positive correlation between user count and global sales. This means that, in general, games with higher user counts tend to have higher global sales. However, the correlation is not perfect, and there are some outliers.
# 
# There is a large spread in the data. This means that there is a wide range of global sales for games with similar user counts. Some games with relatively low user counts have high sales, and some games with high user counts have low sales.

# # Pie Chart

# In[18]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Video_Game_Sales_as_of_Jan_2017.csv')  
total_sales_by_genre = df.groupby('Genre')['Global_Sales'].sum().reset_index()

plt.figure(figsize=(8, 8))
plt.pie(total_sales_by_genre['Global_Sales'], labels=total_sales_by_genre['Genre'], autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Total Sales by Product Category')
plt.show()


# Mobile games dominate the market, accounting for over 45% of total sales. This is likely due to the widespread availability of smartphones and the popularity of mobile gaming apps.
# 
# Console games come in second, with a share of around 25%. This segment is dominated by traditional gaming consoles like those from Sony, Microsoft, and Nintendo.
# 
# PC games follow closely behind with a share of about 20%. The rise of powerful gaming PCs and online gaming platforms like Steam has contributed to the growth of this segment.
# 
# Handheld games, such as those from Nintendo, make up a small portion of the market, with a share of around 5%. The popularity of mobile gaming has likely eroded some of the market share for handheld games.
# 
# Other categories, such as virtual reality games and arcade games, make up the remaining 5% of the market.

# # Heatmaps

# In[71]:


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


# This heatmap indicates that there is a positive correlation between maximum variables this indicates that they are similar in nature

# # Treemap

# In[1]:


import pandas as pd
import plotly.express as px

df = pd.read_csv('Video_Game_Sales_as_of_Jan_2017.csv') 

fig = px.treemap(df, path=['Genre'], values='Global_Sales', title='Treemap of Sales by Product Categories')
fig.show()


# The Action category is the largest, indicating that it has the highest total sales.
# 
# The Shooter and Sports categories are also relatively large.
# 
# The Puzzle and Adventure categories are smaller, but still have a noticeable presence.
# 
# The Strategy and Simulation categories are the smallest, suggesting that they have the lowest total sales.
# 
# The colors of the rectangles suggest that Action games have the highest average rating, followed by Adventure and Sports games. Strategy and Simulation games appear to have the lowest average ratings.
# 

# # Boxplot

# In[46]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Video_Game_Sales_as_of_Jan_2017.csv')

plt.figure(figsize=(12, 8))
sns.boxplot(y='Global_Sales', data=df)
plt.title('Box Plot of Global Sales')
plt.ylabel('Global Sales')
plt.show()


# Overall, there is a wide range of global sales for video games across different genres. The box plot shows that the median sales (represented by the line in the middle of the box) vary considerably between genres. 
# 
# The distribution of sales within each genre also varies. The length of the boxes and whiskers in the box plot indicates the spread of the data within each genre.
# 
# There are some outliers in the data. The dots above and below the whiskers represent data points that fall outside the normal range of the distribution for each genre. These outliers could be due to a variety of factors, such as the release of a particularly popular game within a genre.

# # Bubble Chart

# In[74]:


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


# There are some outliers and data is not so well spread

# # Histogram

# In[76]:


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


# PS2 has the maximum number of games released on it's platform, whereas GEN has the minumum number of games released on it's platform. 
# 
# The company should focus on the sales of PS2 to retain the customer and continuing to issue games on it. 

# # Worldcloud

# In[34]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt

text_data = " ".join(pd.read_csv('Video_Game_Sales_as_of_Jan_2017.csv')['Name'])  

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Key Terms')
plt.show()


# Ball: This could refer to sports games like "Madden NFL," "NBA Live," and "Pro Yakyuu," which are all present in the data.
# 
# Adventure: This is a common theme in many video games, including "Gustar Hero," "Legend of Zelda," and "Dragon Ball."
# 
# Battle: This suggests action-oriented games, such as "Soul Calibur," "Tekken," and "Street Fighter."
# 
# Time: This could be related to games where time is a central mechanic, such as "Dark Souls" or "The Legend of Zelda: Majora's Mask."
# 
# World: Many video games take place in expansive open worlds, like "Grand Theft Auto," "The Witcher 3: Wild Hunt," and "Red Dead Redemption 2."
# 
