#!/usr/bin/env python
# coding: utf-8

# # <font color='#3f6569'><u>Valorant Weapon Stats - IT Project</u></font>

# In[1]:


# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

st.header("Valorant Weapon Stats - IT Project")
st.markdown("Lets open the file:")

# ## <font color='#3f6569'><u>Lets open the file:</u></font>

# In[2]:


data = pd.read_csv(r'valorant-stats.csv') # upload a file
data

st.subheader("Name change:")
# ## <font color='#3f6569'><u>Data cleanup:</u></font>

st.code('''columns = list(data.columns)
columns = [column.lower() for column in columns]
columns = [column.replace(' ', '_') for column in columns]
data.columns = columns
# bring the column names to snake_case
data[:0]
''')
# In[3]:


columns = list(data.columns)
columns = [column.lower() for column in columns]
columns = [column.replace(' ', '_') for column in columns]
data.columns = columns
# bring the column names to snake_case
data[:0]


# ## <font color='#3f6569'><u>Descriptive statistics:</u></font>

# #### <font color='#3f6569'>Let's find the arithmetic mean, median and standard deviation of some values</font>

# ### <font color='#3f6569'>For the price column:</font>

# In[4]:


print('\tArithmetic mean:', data.price.mean())
print('\tMedian:', data.price.median())
print('\tStandard deviation:', data.price.std())


# ### <font color='#3f6569'>For column hdmg_0 (Head Damage from close range):</font>

# In[5]:


print('\tArithmetic mean:', data.hdmg_0.mean())
print('\tMedian:', data.hdmg_0.median())
print('\tStandard deviation:', data.hdmg_0.std())


# ### <font color='#3f6569'>For column magazine_capacity:</font>

# In[6]:


print('\tArithmetic mean:', data.magazine_capacity.mean())
print('\tMedian:', data.magazine_capacity.median())
print('\tStandard deviation:', data.magazine_capacity.std())

st.subheader('Data Cleanup:')
# ## <font color='#3f6569'><u>Data Cleanup:</u></font>
st.markdown("Let's check the data for empty rows. To do this, let's display information about the entire data type of all rows and columns:")
# #### <font color='#3f6569'>Let's check the data for empty rows. To do this, let's display information about the entire data type of all rows and columns:</font>

# In[7]:


st.data.info() # Display information about the dataset


# #### <font color='#3f6569'>As we can see, the data is clean and with the correct type!</font>

# ## <font color='#3f6569'><u>Light and complex plots</u></font>

# ### <font color='#3f6569'>1. Let's take a look at the prices of each weapon:
# #### <font color='#3f6569'>We can construct a scatter plot for accurate analysis</font>

# In[21]:


x = data.name # x denotes the name of each weapon
y = data.price # y shows the price of each weapon
 
plt.scatter(x, y, color = '#3c8c99')
plt.xticks(x, rotation='vertical')

plt.xlabel('Names of weapons')
plt.ylabel('The price of each weapon')
 
plt.show()


# #### <font color='#3f6569'>The graph clearly shows that the most expensive weapon is the "operator" which costs almost 5000, and the cheapest is the "classic" which costs 0 (since the "classic" is given to each person for free each round)</font>
# #### <font color='#3f6569'>This pricing is easy to explain! Operator is a heavy weapon that can kill with 1 shot, so the developers have set a high price for it to have a balance in the game. This is how it works with all weapons. For example, vandal and phantom cost the same, they also shoot about the same and do the same amount of damage</font>
# 

# ### <font color='#3f6569'>2. Now let's compare the rate of fire of each weapon:</font>
# #### <font color='#3f6569'>To do this, let's use a pie chart for better clarity</font>

# In[9]:


# Creating dataset
names = data.name
fire_rate_of_each_weapon = data.fire_rate

# Creating plot
fig = plt.figure(figsize =(10, 7))
other_colors = ["#c2e2e7", "#a7d5dc", "#8ac7d1", 
                 "#5ab0be", "#449eac", "#3c8c99", '#327580', '#2a626c', '#1e464d']

plt.pie(fire_rate_of_each_weapon, labels = names,
        colors = other_colors, explode=[0.05]*12+[0.15]+[0.25]+[0.45]+[0.05]*2, autopct='%.0f%%')

plt.xlabel('Fire rates')

plt.show()


# #### <font color='#3f6569'>As you can see, the "stinger" has the highest rate of fire, the "spectrum" is in 2nd place, and 2 weapons - "phantom" and "odin" - are in third place at once</font>
# #### <font color='#3f6569'>I can only assume it's because of their size. "Stinger" is a rather small weapon, it will be useful only if it shoots fast, while, for example, "Operator", which has 1% speed - it is a sniper weapon, respectively large and requires concentration</font>

# ### <font color='#3f6569'> 3. Now let's see how many weapons of each kind we have:</font>
# #### <font color='#3f6569'> We can use a bar chart to do this</font>

# In[10]:


data.weapon_type.value_counts().plot.bar(color = other_colors)

plt.xlabel('Types of weapons')
plt.ylabel('The number of weapons of this kind')

plt.show()


# #### <font color='#3f6569'>Well, we see that the most weapons of the sidearm kind exist</font>
# #### <font color='#3f6569'>I think it's because this type of weapon is more affordable than the others, plus they can be a good addition to the main weapon, which is different for all players</font>

# ## <font color='#3f6569'><u>Detailed Overview:</u></font>
# ### <font color='#3f6569'>4. Let's see, maybe the price depends on the rate of fire of the weapon </font>

# In[35]:


sns.barplot(x="price", y="fire_rate", data=data, palette = other_colors)
plt.xticks(rotation=45) # Rotate titles by 45 degrees

plt.xlabel('Price of each weapon')
plt.ylabel('The rate of fire')

plt.show()


# #### <font color='#3f6569'>Well, apparently it doesn't matter how fast a gun fires, its price can be anything despite the rate of fire</font>

# ### <font color='#3f6569'>5. Let's look at the dependence of damage to the body at close range and the price of the weapon</font>

# In[20]:


need_colors = ["#5ab0be", "#449eac", "#3c8c99", '#327580', '#2a626c', '#1e464d']
fig = sns.scatterplot(hue='weapon_type', y='price', x="bdmg_0", 
                palette = need_colors, data=data, size = 'price')

plt.xlabel('Body Damage')
plt.ylabel('Price of each weapon')

plt.legend(loc="lower right")
plt.show()


# #### <font color='#3f6569'>In the lower left corner there are small light dots - these are weapons with a small price, if you look to the right, we notice how the dots slowly increase and become darker - the price becomes higher and the weapon becomes more powerful</font>
# #### <font color='#3f6569'>Well, we can safely conclude that the higher the price of the weapon, the more damage to the body!</font>

# ### <font color='#3f6569'> 6. Now let's check the correlation between price and head damage at long range</font>

# In[39]:


pivot_data = data.pivot_table(index='weapon_type', columns='price', values='hdmg_0', aggfunc='mean')
plt.figure(figsize=(8, 6))
sns.heatmap(pivot_data, cmap= other_colors, annot=True, fmt='.2f')
plt.xlabel('Price')
plt.ylabel('Weapon Type')
plt.title('Price vs. Head Damage (Close Range)', color = '#3f6569')
plt.show()


# #### <font color='#3f6569'>The graph clearly shows that Shotgun weapons do about the same amount of damage despite their price, unlike Sidearm, where almost all weapons have different head damage.</font>
# #### <font color='#3f6569'>I think there is no correlation in price and head damage of different types of weapons, as all types are used for different tactics and mechanics</font>

# ### <font color='#3f6569'> 7. Now let's look at the amount of damage each weapon type does at different distances</font>
# #### <font color='#3f6569'>For this, it would be best to get a heat map for a detailed review:</font>

# In[14]:


weapon_types = data['weapon_type'].unique()
for weapon_type in weapon_types:
    weapon_subset = data[data['weapon_type'] == weapon_type]
    attributes = ['hdmg_0', 'bdmg_0', 'ldmg_0', 'hdmg_1', 'bdmg_1', 'ldmg_1', 'hdmg_2', 'bdmg_2', 'ldmg_2']
    attributes_data = weapon_subset[attributes].mean().values.reshape(3, 3)

    plt.figure(figsize=(4, 4))
    sns.heatmap(attributes_data, cmap=other_colors, annot=True, fmt='.2f', xticklabels=['Close', 'Medium', 'Long'], yticklabels=['Head', 'Body', 'Leg'])
    plt.xlabel('Range')
    plt.ylabel('Damage Type')
    plt.title(f'{weapon_type} Performance across Ranges')
    plt.show()


# #### <font color='#3f6569'>You can clearly see here that the strongest weapon is the sniper, as expected. Next comes the Rifle, followed by the Sidearm, Heavy, Smg and finally the Shotgun</font>
# #### <font color='#3f6569'>Personally, I think that the best weapon is the riffle, because it is not slow, if you hit the head with it, you will probably kill, and it does not require perfect accuracy!</font>

# ## <font color='#3f6569'><u>Hypothesis: </u></font>
# ### <font color='#3f6569'> If I have a gun '...' I have enough bullets to kill five players with body shots at close range, provided they don't return fire and all of them have full HP</font>

# In[15]:


max_hp = 150 #In this game, the man has 100hp and a 50hp shield.
target_count = 5


# #### <font color='#3f6569'>To confirm or deny the hypothesis (for each weapon), we need to understand how many bullets our weapon has, as well as to understand the maximum amount of damage I can do with this weapon to a person in the body at close range</font>
# #### <font color='#3f6569'>If that amount of damage we have is greater than and equal to how much damage it takes to kill all 5 people, then I win</font>
# #### <font color='#3f6569'>How much damage you need to do to win can be calculated by multiplying the number of players on the other team and their HP (both are maxed out by convention)</font>

# In[16]:


data['is_hypothesis_correct'] = (data.magazine_capacity * data.bdmg_0 >= 
                                 target_count * max_hp)

data['is_hypothesis_correct']


# In[17]:


colors = ['#3c8c99' if correct else '#1e464d' for 
          correct in data.is_hypothesis_correct]


# In[18]:


plt.figure(figsize=(3,10), dpi= 80)
plt.hlines(y=data.index, xmin=0, xmax=1, color=colors, alpha=0.4, linewidth=5)

plt.gca().set(ylabel='Weapons')
plt.yticks(data.index, data.name, fontsize=12)
plt.title('Hypythesis check', fontdict={'size':20, 'color':'#0f3539'})
plt.grid(linestyle='--', alpha=0.5)
plt.gca().xaxis.set_visible(False)

plt.show()


# #### <font color='#3f6569'>Here you can see for which weapons the hypothesis is fulfilled and for which it is not</font>
# 
# #### <font color='#3f6569'>Unfortunately, in many variants we will lose, but we should not forget that there are many other conditions because of which we could have won (taking weapons from the opponents, using 2 weapons at once, stabbing someone, winning just for time)</font>
