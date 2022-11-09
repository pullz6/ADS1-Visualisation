#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 10:05:18 2022

@author: Pulsara
"""

#Importing modules
#===========================================================================
import pandas as pd 
import matplotlib.pyplot as plt

#Functions
#===========================================================================
def func_price_to_gbp(price):
    price_in_gbp = []
    for one in price: 
        temp = one*0.88
        price_in_gbp.append(temp)
    return price_in_gbp

def func_price_per_page(page,price): 
    price_per_page = []
    for i in page.index: 
        temp = page[i]/price[i]
        price_per_page.append(temp)
    return price_per_page
    

def func_five_star(five_star,total_reviews): 
    list_five_star = []
    avg = five_star.mean()
    for i in five_star.index: 
        if five_star[i] > avg: 
            list_five_star.append("High")
        elif five_star[i] < avg:
            list_five_star.append("low") 
        else: 
            list_five_star.append("avg")
    return list_five_star

def func_four_star(four_star,total_reviews): 
    list_four_star = []
    avg = four_star.mean()
    for i in four_star.index: 
        if four_star[i] > avg: 
            list_four_star.append("High")
        elif four_star[i] < avg: 
            list_four_star.append("low") 
        else: 
            list_four_star.append("avg")
    return list_four_star

def func_three_star(three_star,total_reviews): 
    list_three_star = []
    avg = three_star.mean()
    for i in three_star.index: 
        if three_star[i] > avg: 
            list_three_star.append("High")
        elif three_star[i] < avg: 
            list_three_star.append("low") 
        else: 
            list_three_star.append("avg")
    return list_three_star

def func_two_star(two_star,total_reviews): 
    list_two_star = []
    avg = two_star.mean()
    for i in two_star.index: 
        if two_star[i] > avg: 
            list_two_star.append("High")
        elif two_star[i] < avg: 
            list_two_star.append("low") 
        else: 
            list_two_star.append("avg")
    return list_two_star

def func_one_star(one_star,total_reviews): 
    list_one_star = []
    avg = one_star.mean()
    for i in one_star.index: 
        if one_star[i] > avg: 
            list_one_star.append("High")
        elif one_star[i] < avg: 
            list_one_star.append("low") 
        else: 
            list_one_star.append("avg")
    return list_one_star

#########

def numeric_five_star(five_star,total_reviews): 
    list_five_star = []
    for i in five_star.index: 
        five_star_value = five_star[i] * total_reviews[i]
        list_five_star.append(five_star_value)
    return list_five_star

def numeric_four_star(four_star,total_reviews): 
    list_four_star = []
    for i in four_star.index: 
        four_star_value = four_star[i] * total_reviews[i]
        list_four_star.append(four_star_value)
    return list_four_star

def numeric_three_star(three_star,total_reviews): 
    list_three_star = []
    for i in four_star.index: 
        three_star_value = three_star[i] * total_reviews[i]
        list_three_star.append(three_star_value)
    return list_three_star

def numeric_two_star(two_star,total_reviews): 
    list_two_star = []
    for i in two_star.index: 
        two_star_value = two_star[i] * total_reviews[i]
        list_two_star.append(two_star_value)
    return list_two_star

def numeric_one_star(one_star,total_reviews): 
    list_one_star = []
    for i in one_star.index: 
        one_star_value = one_star[i] * total_reviews[i]
        list_one_star.append(one_star_value)
    return list_one_star

#Main Programme
#===========================================================================
#Extracting required data and including them into variables 
df_amazonbooks = pd.read_csv('final_book_dataset_kaggle.csv')
df_amazonbooks.dropna(axis=0, how='any', thresh=0, subset=None, inplace=True)
df_amazonbooks.sort_values("n_reviews", inplace = True)
print(df_amazonbooks['star2'])
#Prices for books
price = df_amazonbooks['price']
#Number of pages in the book 
pages = df_amazonbooks['pages']
#The average rating of the book
rating = df_amazonbooks['avg_reviews']
#The number of 5 star ratings 
five_star  = df_amazonbooks['star5']
#The number of 4 star ratings 
four_star = df_amazonbooks['star4']
#The number of 3 star ratings 
three_star = df_amazonbooks['star3']
#The number of 2 star ratings
two_star = df_amazonbooks['star2']
#The number of 1 star ratings
one_star  = df_amazonbooks['star1']
#The number of reviews provided 
no_reviews = df_amazonbooks['n_reviews']

#Visualisation 
#Plotting a line graph 
fig, ax1 = plt.subplots()
color = "red"
ax1.set_xlabel('Number of Reviews')
ax1.set_ylabel('Rating', color=color)
ax1.plot(no_reviews, rating, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = "blue" 
ax2.set_ylabel('Price', color=color)
price_in_gbp = func_price_to_gbp(price)
ax2.plot(no_reviews, price_in_gbp, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
plt.show()


#Plotting a a histogram
plt.figure()
price_per_page = func_price_per_page(pages, price)
plt.scatter(rating,price_per_page)
plt.xlabel("Rating of 5")
plt.ylabel("Price per page")
plt.show()



#Plotting a histogram too
data = []
data.append(func_five_star(five_star, no_reviews))
data.append(func_four_star(four_star, no_reviews))
data.append(func_three_star(three_star, no_reviews))
data.append(func_two_star(two_star, no_reviews))
data.append(func_one_star(one_star, no_reviews))
print(data)


labels = ["5 Star Rating","4 Star Rating","3 Star Rating","2 Star Rating","1 Star Rating"]
plt.figure()
plt.subplots_adjust(hspace=0.6, wspace=0.6)
i=0
for i in range(len(data)):
    plt.subplot(2, 3, i+1)
    plt.hist(data[i])
    plt.xlabel("% of "+labels[i])
    plt.ylabel("Number of reviews")
    
plt.show()

# #Plotting a violin plot 
# plt.figure
# # we need the subplot to get access to the axes object
# fig, ax = plt.subplots(1, 1)
# plt.violinplot(data, showmedians=True) # list with returns data from above
# ax.set_xticks([1, 2, 3, 4,5])
# ax.set_xticklabels(labels)
# plt.ylabel("Ranges")
# # plt.savefig("violines.png")
# plt.show()

#Scatter plot
# data = [numeric_five_star(five_star, no_reviews),numeric_four_star(four_star, no_reviews),numeric_three_star(three_star, no_reviews),numeric_two_star(two_star, no_reviews),numeric_one_star(one_star, no_reviews)]
# labels = ["5 Star Rating","4 Star Rating","3 Star Rating","2 Star Rating","1 Star Rating"]
# plt.figure()
# #plt.figure(figsize=(10,10))
# plt.subplot(3,2,1)
# plt.bar(data[0],no_reviews)
# plt.xlabel("Tot 5 Star ratings")
# plt.ylabel("Tot reviews")

# plt.subplot(3,2,2)
# plt.scatter(data[1],no_reviews)
# plt.xlabel("Tot 4 Star ratings")
# plt.ylabel("Tot reviews")

# plt.subplot(3,2,3)
# plt.scatter(data[2],no_reviews)
# plt.xlabel("Tot 3 Star ratings")
# plt.ylabel("Tot reviews")

# plt.subplot(3,2,4)
# plt.scatter(data[3],no_reviews)
# plt.xlabel("Tot 2 Star ratings")
# plt.ylabel("Tot reviews")

# plt.subplot(3,2,5)
# plt.scatter(data[4],no_reviews)
# plt.xlabel("Tot 1 Star ratings")
# plt.ylabel("Tot reviews")


#plt.show()
