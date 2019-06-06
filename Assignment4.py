
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **weather phenomena** (see below) for the region of **Ann Arbor, Michigan, United States**, or **United States** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Ann Arbor, Michigan, United States** to Ann Arbor, USA. In that case at least one source file must be about **Ann Arbor, Michigan, United States**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Ann Arbor, Michigan, United States** and **weather phenomena**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **weather phenomena**?  For this category you might want to consider seasonal changes, natural disasters, or historical trends.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[82]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("https://datadryad.org/bitstream/handle/10255/dryad.138429/aegypti_albopictus.csv")
df.head()

df1 = pd.read_csv("countryContinent.csv", encoding = 'latin-1')
df = df.merge(df1[['code_3','continent']],how='left',left_on = 'COUNTRY_ID', right_on = 'code_3')
df['CONTINENT'] = df.continent
df = df[df.YEAR != '2006-2008']


# In[83]:

df= df.drop(df.columns[[3,4,9,10,11,12,13]], axis = 1)

df.head()


# In[84]:

null_columns=df.columns[df.isnull().any()]
print(df[df['CONTINENT'].isnull()][null_columns])
df = df[pd.notnull(df['CONTINENT'])]


# In[85]:

aeg = df[df.VECTOR == "Aedes aegypti"]
alb = df[df.VECTOR == "Aedes albopictus"]
aeg = aeg.reset_index(drop = True)
alb = alb.reset_index(drop = True)

aeg.head(10)


# In[86]:

alb.head()


# In[87]:

aeg1 = aeg.groupby(["YEAR","CONTINENT"]).size().unstack()
alb1 = alb.groupby(["YEAR","CONTINENT"]).size().unstack()


# In[88]:

#aeg1 = aeg1.reset_index()
#aeg1.index.rename("Index")
#aeg1.head()


# In[91]:

color_map = ["#9b59b6", "#e74c3c", "#34495e", "#2ecc71","#9ACD32"]
ax1 = aeg1.plot(kind='bar',stacked=True,figsize = (20,12),colors = color_map)
ax2 = alb1.plot(kind='bar',stacked=True,figsize = (20,12),colors = color_map)
ax1.set_title("Occurence of Aedes Aegypti from 1958-2014 in different continents ",size = 20)
ax2.set_title("Occurence of Aedes Albopictus from 1964-2014 in different continents ",size = 20)
ax1.set_ylabel("Number of occurences")
ax2.set_ylabel("Number of occurences")
ax1.set_xlabel("Years")
ax1.set_xlabel("Years")
ax1.grid(False)
ax2.grid(False)
[plt.gca().spines[loc].set_visible(False) for loc in ['top', 'right']]
plt.show()
plt.savefig("Assignment4.png")


# In[75]:




# In[ ]:



