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


data = pd.read_csv(r'D:\valorant-stats.csv')  # upload a file
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
st.subheader("Descriptive statistics:")

st.markdown("For the price column:")

st.code('''print('\tArithmetic mean:', data.price.mean())
print('\tMedian:', data.price.median())
print('\tStandard deviation:', data.price.std())''')

# ### <font color='#3f6569'>For column hdmg_0 (Head Damage from close range):</font>

# In[5]:

st.markdown("For column hdmg_0 (Head Damage from close range):")
st.code('''print('\tArithmetic mean:', data.hdmg_0.mean())
print('\tMedian:', data.hdmg_0.median())
print('\tStandard deviation:', data.hdmg_0.std())''')

# ### <font color='#3f6569'>For column magazine_capacity:</font>

# In[6]:

st.markdown("For column magazine_capacity:")
st.code('''print('\tArithmetic mean:', data.magazine_capacity.mean())
print('\tMedian:', data.magazine_capacity.median())
print('\tStandard deviation:', data.magazine_capacity.std())''')

st.subheader('Data Cleanup:')
# ## <font color='#3f6569'><u>Data Cleanup:</u></font>
st.markdown(
    "Let's check the data for empty rows. To do this, let's display information about the entire data type of all rows and columns:")
# #### <font color='#3f6569'>Let's check the data for empty rows. To do this, let's display information about the entire data type of all rows and columns:</font>

# In[7]:


# #### <font color='#3f6569'>As we can see, the data is clean and with the correct type!</font>

st.subheader("Light and complex plots")
st.subheader("1. Let's take a look at the prices of each weapon:")
st.markdown("We can construct a scatter plot for accurate analysis")

# ## <font color='#3f6569'><u>Light and complex plots</u></font>

# ### <font color='#3f6569'>1. Let's take a look at the prices of each weapon:
# #### <font color='#3f6569'>We can construct a scatter plot for accurate analysis</font>

# In[21]:


fig, ax = plt.subplots()
ax.scatter(data['name'], data['price'], color='#3c8c99')
ax.set_xticklabels(data['name'], rotation='vertical')
ax.set_xlabel('Names of weapons')
ax.set_ylabel('The price of each weapon')
ax.set_title('Prices of each weapon', color='#3f6569')

st.pyplot(fig)

st.markdown("The graph clearly shows that the most expensive weapon is the 'operator' which costs almost 5000, and the cheapest is the 'classic' which costs 0 (since the 'classic' is given to each person for free each round")
# #### <font color='#3f6569'>The graph clearly shows that the most expensive weapon is the "operator" which costs almost 5000, and the cheapest is the "classic" which costs 0 (since the "classic" is given to each person for free each round)</font>
# #### <font color='#3f6569'>This pricing is easy to explain! Operator is a heavy weapon that can kill with 1 shot, so the developers have set a high price for it to have a balance in the game. This is how it works with all weapons. For example, vandal and phantom cost the same, they also shoot about the same and do the same amount of damage</font>
st.markdown("This pricing is easy to explain! Operator is a heavy weapon that can kill with 1 shot, so the developers have set a high price for it to have a balance in the game. This is how it works with all weapons. For example, vandal and phantom cost the same, they also shoot about the same and do the same amount of damage")

st.subheader("2. Now let's compare the rate of fire of each weapon:")
st.markdown("To do this, let's use a pie chart for better clarity")
# ### <font color='#3f6569'>2. Now let's compare the rate of fire of each weapon:</font>
# #### <font color='#3f6569'>To do this, let's use a pie chart for better clarity</font>

# In[9]:


# Creating dataset
names = data['name']
fire_rate_of_each_weapon = data['fire_rate']

fig, ax = plt.subplots(figsize=(10, 7))
other_colors = ["#c2e2e7", "#a7d5dc", "#8ac7d1", "#5ab0be", "#449eac", "#3c8c99", "#327580", "#2a626c", "#1e464d"]
explode = [0.05] * 12 + [0.15] + [0.25] + [0.45] + [0.05] * 2

ax.pie(fire_rate_of_each_weapon, labels=names, colors=other_colors, explode=explode, autopct='%.0f%%')
ax.set_xlabel('Fire rates')
ax.set_title('Rate of fire of each weapon', color='#3f6569')

st.pyplot(fig)

st.markdown('As you can see, the "stinger" has the highest rate of fire, the "spectrum" is in 2nd place, and 2 weapons - "phantom" and "odin" - are in third place at once')
st.markdown('I can only assume it is because of their size. "Stinger" is a rather small weapon, it will be useful only if it shoots fast, while, for example, "Operator", which has 1% speed - it is a sniper weapon, respectively large and requires concentration')

# #### <font color='#3f6569'>As you can see, the "stinger" has the highest rate of fire, the "spectrum" is in 2nd place, and 2 weapons - "phantom" and "odin" - are in third place at once</font>
# #### <font color='#3f6569'>I can only assume it's because of their size. "Stinger" is a rather small weapon, it will be useful only if it shoots fast, while, for example, "Operator", which has 1% speed - it is a sniper weapon, respectively large and requires concentration</font>


st.subheader("3. Now let's see how many weapons of each kind we have:")
st.markdown('We can use a bar chart to do this')
# ### <font color='#3f6569'> 3. Now let's see how many weapons of each kind we have:</font>
# #### <font color='#3f6569'> We can use a bar chart to do this</font>

# In[10]:


fig, ax = plt.subplots()
data['weapon_type'].value_counts().plot.bar(color=other_colors)
ax.set_xlabel('Types of weapons')
ax.set_ylabel('The number of weapons of this kind')
ax.set_title('Weapons of each kind', color='#3f6569')

st.pyplot(fig)

st.markdown('Well, we see that the most weapons of the sidearm kind exist')
st.markdown("I think it's because this type of weapon is more affordable than the others, plus they can be a good addition to the main weapon, which is different for all players")
# #### <font color='#3f6569'>Well, we see that the most weapons of the sidearm kind exist</font>
# #### <font color='#3f6569'>I think it's because this type of weapon is more affordable than the others, plus they can be a good addition to the main weapon, which is different for all players</font>


st.subheader("Detailed Overview:")
st.subheader("4. Let's see, maybe the price depends on the rate of fire of the weapon")
# ## <font color='#3f6569'><u>Detailed Overview:</u></font>
# ### <font color='#3f6569'>4. Let's see, maybe the price depends on the rate of fire of the weapon </font>

# In[35]:


fig, ax = plt.subplots()
sns.barplot(x='price', y='fire_rate', data=data, palette=other_colors)
ax.set_xticklabels(ax.get_xticks())
ax.set_xlabel('Price of each weapon')
ax.set_ylabel('The rate of fire')
ax.set_title('Dependence of price and rate of fire', color='#3f6569')

st.pyplot(fig)

st.markdown("Well, apparently it doesn't matter how fast a gun fires, its price can be anything despite the rate of fire")

st.subheader("5. Let's look at the dependence of damage to the body at close range and the price of the weapon")

# #### <font color='#3f6569'>Well, apparently it doesn't matter how fast a gun fires, its price can be anything despite the rate of fire</font>

# ### <font color='#3f6569'>5. Let's look at the dependence of damage to the body at close range and the price of the weapon</font>

# In[20]:


fig, ax = plt.subplots()
need_colors = ["#5ab0be", "#449eac", "#3c8c99", "#327580", "#2a626c", "#1e464d"]
sns.scatterplot(hue='weapon_type', y='price', x="bdmg_0", palette=need_colors, data=data, size='price')
ax.set_xlabel('Body Damage')
ax.set_ylabel('Price of each weapon')
ax.legend(loc="lower right")
ax.set_title('Dependence of price and Body Damage', color='#3f6569')

st.pyplot(fig)

st.markdown("In the lower left corner there are small light dots - these are weapons with a small price, if you look to the right, we notice how the dots slowly increase and become darker - the price becomes higher and the weapon becomes more powerful")
st.markdown("Well, we can safely conclude that the higher the price of the weapon, the more damage to the body!")
# #### <font color='#3f6569'>In the lower left corner there are small light dots - these are weapons with a small price, if you look to the right, we notice how the dots slowly increase and become darker - the price becomes higher and the weapon becomes more powerful</font>
# #### <font color='#3f6569'>Well, we can safely conclude that the higher the price of the weapon, the more damage to the body!</font>


st.subheader("6. Now let's check the correlation between price and head damage at long range")
# ### <font color='#3f6569'> 6. Now let's check the correlation between price and head damage at long range</font>

# In[39]:
pivot_data = data.pivot_table(index='weapon_type', columns='price', values='hdmg_0', aggfunc='mean')

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(pivot_data, cmap=other_colors, annot=True, fmt='.2f')
ax.set_xlabel('Price')
ax.set_ylabel('Weapon Type')
ax.set_title('Price vs. Head Damage (Close Range)', color='#3f6569')

st.pyplot(fig)


st.markdown("The graph clearly shows that Shotgun weapons do about the same amount of damage despite their price, unlike Sidearm, where almost all weapons have different head damage")
st.markdown("I think there is no correlation in price and head damage of different types of weapons, as all types are used for different tactics and mechanics")
# #### <font color='#3f6569'>The graph clearly shows that Shotgun weapons do about the same amount of damage despite their price, unlike Sidearm, where almost all weapons have different head damage.</font>
# #### <font color='#3f6569'>I think there is no correlation in price and head damage of different types of weapons, as all types are used for different tactics and mechanics</font>

st.subheader("7. Now let's look at the amount of damage each weapon type does at different distances")
st.markdown("For this, it would be best to get a heat map for a detailed review:")
# ### <font color='#3f6569'> 7. Now let's look at the amount of damage each weapon type does at different distances</font>
# #### <font color='#3f6569'>For this, it would be best to get a heat map for a detailed review:</font>

# In[14]:


weapon_types = data['weapon_type'].unique()

for weapon_type in weapon_types:
    weapon_subset = data[data['weapon_type'] == weapon_type]
    attributes = ['hdmg_0', 'bdmg_0', 'ldmg_0', 'hdmg_1', 'bdmg_1', 'ldmg_1', 'hdmg_2', 'bdmg_2', 'ldmg_2']
    attributes_data = weapon_subset[attributes].mean().values.reshape(3, 3)

    fig, ax = plt.subplots(figsize=(3, 3))
    sns.heatmap(attributes_data, cmap=other_colors, annot=True, fmt='.2f', xticklabels=['Close', 'Medium', 'Long'],
                yticklabels=['Head', 'Body', 'Leg'])
    ax.set_xlabel('Range')
    ax.set_ylabel('Damage Type')
    ax.set_title(f'{weapon_type} Performance across Ranges')

    # Display the plot using streamlit
    st.pyplot(fig)

st.markdown("You can clearly see here that the strongest weapon is the sniper, as expected. Next comes the Rifle, followed by the Sidearm, Heavy, Smg and finally the Shotgun")
st.markdown("Personally, I think that the best weapon is the riffle, because it is not slow, if you hit the head with it, you will probably kill, and it does not require perfect accuracy!")

# #### <font color='#3f6569'>You can clearly see here that the strongest weapon is the sniper, as expected. Next comes the Rifle, followed by the Sidearm, Heavy, Smg and finally the Shotgun</font>
# #### <font color='#3f6569'>Personally, I think that the best weapon is the riffle, because it is not slow, if you hit the head with it, you will probably kill, and it does not require perfect accuracy!</font>

st.subheader("Hypothesis:")
st.markdown("If I have a gun '...' I have enough bullets to kill five players with body shots at close range, provided they don't return fire and all of them have full HP")
st.code("max_hp = 150 #In this game, the man has 100hp and a 50hp shield.")

# ## <font color='#3f6569'><u>Hypothesis: </u></font>
# ### <font color='#3f6569'> If I have a gun '...' I have enough bullets to kill five players with body shots at close range, provided they don't return fire and all of them have full HP</font>

# In[15]:


max_hp = 150  # In this game, the man has 100hp and a 50hp shield.
target_count = 5

st.markdown("To confirm or deny the hypothesis (for each weapon), we need to understand how many bullets our weapon has, as well as to understand the maximum amount of damage I can do with this weapon to a person in the body at close range")
st.markdown("If that amount of damage we have is greater than and equal to how much damage it takes to kill all 5 people, then I win")
st.markdown("How much damage you need to do to win can be calculated by multiplying the number of players on the other team and their HP (both are maxed out by convention)")
# #### <font color='#3f6569'>To confirm or deny the hypothesis (for each weapon), we need to understand how many bullets our weapon has, as well as to understand the maximum amount of damage I can do with this weapon to a person in the body at close range</font>
# #### <font color='#3f6569'>If that amount of damage we have is greater than and equal to how much damage it takes to kill all 5 people, then I win</font>
# #### <font color='#3f6569'>How much damage you need to do to win can be calculated by multiplying the number of players on the other team and their HP (both are maxed out by convention)</font>

# In[16]:


data['is_hypothesis_correct'] = (data.magazine_capacity * data.bdmg_0 >=
                                 target_count * max_hp)


# In[17]:


colors = ['#3c8c99' if correct else '#1e464d' for correct in data['is_hypothesis_correct']]

fig, ax = plt.subplots(figsize=(2, 4), dpi=50)
ax.hlines(y=data.index, xmin=0, xmax=1, color=colors, alpha=0.4, linewidth=5)
ax.set_ylabel('Weapons')
ax.set_yticks(data.index)
ax.set_yticklabels(data['name'], fontsize=8)
ax.set_title('Hypothesis check', fontdict={'size': 12, 'color': '#0f3539'})
ax.grid(linestyle='--', alpha=0.5)
ax.xaxis.set_visible(False)

st.pyplot(fig)

st.markdown("Here you can see for which weapons the hypothesis is fulfilled and for which it is not")
st.markdown("Unfortunately, in many variants we will lose, but we should not forget that there are many other conditions because of which we could have won (taking weapons from the opponents, using 2 weapons at once, stabbing someone, winning just for time)")
# #### <font color='#3f6569'>Here you can see for which weapons the hypothesis is fulfilled and for which it is not</font>
#
# #### <font color='#3f6569'>Unfortunately, in many variants we will lose, but we should not forget that there are many other conditions because of which we could have won (taking weapons from the opponents, using 2 weapons at once, stabbing someone, winning just for time)</font>
