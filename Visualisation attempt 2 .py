#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 13:00:51 2022

@author: thiwanka
"""
#Importing modules
#===========================================================================
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

#Functions
#===========================================================================


#Main Programme
#===========================================================================
#Extracting required data and including them into variables 
df_amazonbooks = pd.read_csv('final_book_dataset_kaggle.csv')
#Prices for books
price = df_amazonbooks['price']
#Number of pages in the book 
pages = df_amazonbooks['pages']
#The average rating of the book
rating = df_amazonbooks['avg_reviews']
#The number of 5 star ratings 
five_star = rating = df_amazonbooks['star5']
#The number of 4 star ratings 
four_star = rating = df_amazonbooks['star4']
#The number of 3 star ratings 
three_star = rating = df_amazonbooks['star3']
#The number of 2 star ratings
two_star = rating = df_amazonbooks['star2']
#The number of 1 star ratings
one_star = rating = df_amazonbooks['star1']
#The number of reviews provided 
no_reviews = df_amazonbooks['n_reviews']

#Visualisation 
#Plotting a line graph 
# plt.figure()
# plt.plot(rating,no_reviews,label="Rating VS Number of Reviews")
# plt.xlabel('Rating')
# plt.ylabel('Number of Reviews')
# plt.legend()
# plt.show()

# #Plotting a line graph 
# plt.figure()
# plt.plot(one_star,no_reviews,label="One Rating VS Number of Reviews")
# plt.xlabel('No of 1 Star Ratings')
# plt.ylabel('Number of Reviews')
# plt.legend()
# plt.show()

#Plotting a a histogram 
data = [five_star,four_star,three_star,two_star,one_star]
labels = ["Five Star Rating","Four Star Rating","Three Star Rating","Two Star Rating","One Star Rating"]
plt.figure()
plt.subplots_adjust(hspace=0.6, wspace=0.6)
i=0
for i in range(len(data)):
    plt.subplot(2, 2, i+1)
    plt.hist(data[i])
    plt.xlabel(labels[i])
    plt.ylabel("Number of total reviews")
    
plt.show()



