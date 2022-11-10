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
    """"Convert the price which is in USD into GBP, add it to a list and return the list"""
    price_in_gbp = []
    for one in price: 
        #As the current exchange range is 1 USD = 0.88 GPB, we multiply with price with 0.88. 
        temp = one*0.88
        #Adding the converted value to a list
        price_in_gbp.append(temp)
    #Returning the new list
    return price_in_gbp

def func_price_per_page(page,price): 
    """"Find the price per page, add it to a new list and return the list"""
    price_per_page = []
    #Running a For ;loop for i in the list of page series' index. 
    for i in page.index: 
        #Divinding the number of pages by the price to find the price per page. 
        temp = page[i]/price[i]
        #Adding it to a list
        price_per_page.append(temp)
    #Returning the list
    return price_per_page 
    
def numeric_five_star(five_star,total_reviews): 
    """"Find the total number of reviews with 5 stars, add it to a new list and return the list"""
    list_five_star = []
    #Running a for loop for the star series' index list. 
    for i in five_star.index: 
        #Multiplyting the percentage of star review by the total number of review to get the exact portion of reviews related to that particular star rating. 
        five_star_value = five_star[i] * total_reviews[i]
        #Adding it to a list
        list_five_star.append(five_star_value)
    #Returning the list
    return list_five_star

def numeric_four_star(four_star,total_reviews): 
    """"Find the total number of reviews with 4 stars, add it to a new list and return the list"""
    list_four_star = []
    #Running a for loop for the star series' index list.
    for i in four_star.index: 
        #Multiplyting the percentage of star review by the total number of review to get the exact portion of reviews related to that particular star rating.
        four_star_value = four_star[i] * total_reviews[i]
        #Adding it to a list
        list_four_star.append(four_star_value)
    #Returning the list
    return list_four_star

def numeric_three_star(three_star,total_reviews):
    """"Find the total number of reviews with 3 stars, add it to a new list and return the list"""
    list_three_star = []
    #Running a for loop for the star series' index list.
    for i in four_star.index: 
        #Multiplyting the percentage of star review by the total number of review to get the exact portion of reviews related to that particular star rating.
        three_star_value = three_star[i] * total_reviews[i]
        #Adding it to a list
        list_three_star.append(three_star_value)
    #Returning the list
    return list_three_star

def numeric_two_star(two_star,total_reviews): 
    """"Find the total number of reviews with 2 stars, add it to a new list and return the list"""
    list_two_star = []
    #Running a for loop for the star series' index list.
    for i in two_star.index: 
        #Multiplyting the percentage of star review by the total number of review to get the exact portion of reviews related to that particular star rating.
        two_star_value = two_star[i] * total_reviews[i]
        #Adding it to a list
        list_two_star.append(two_star_value)
    #Returning the list
    return list_two_star

def numeric_one_star(one_star,total_reviews): 
    """"Find the total number of reviews with 1 star, add it to a new list and return the list"""
    list_one_star = []
    #Running a for loop for the star series' index list.
    for i in one_star.index:
        #Multiplyting the percentage of star review by the total number of review to get the exact portion of reviews related to that particular star rating.
        one_star_value = one_star[i] * total_reviews[i]
        #Adding it to a list
        list_one_star.append(one_star_value)
    #Returning the list
    return list_one_star 

#Main Programme
#===========================================================================
#Extracting required data from the CSV file and creating a dataframe 
df_amazonbooks = pd.read_csv('final_book_dataset_kaggle.csv')
#Dropping any rows with any missing values or zero in the dataframe
df_amazonbooks.dropna(axis=0, how='any', thresh=0, subset=None, inplace=True)
#Sorting the dataframe by the number of reviews column
df_amazonbooks.sort_values("n_reviews", inplace = True)
#Extracting prices for books
price = df_amazonbooks['price']
#Extracting Number of pages in the book 
pages = df_amazonbooks['pages']
#Extracting The average rating of the book
rating = df_amazonbooks['avg_reviews']
#Extracting The number of 5 star ratings 
five_star  = df_amazonbooks['star5']
#Extracting The number of 4 star ratings 
four_star = df_amazonbooks['star4']
#Extracting The number of 3 star ratings 
three_star = df_amazonbooks['star3']
#Extracting The number of 2 star ratings
two_star = df_amazonbooks['star2']
#Extracting The number of 1 star ratings
one_star  = df_amazonbooks['star1']
#Extracting The number of reviews provided 
no_reviews = df_amazonbooks['n_reviews']

#Visualisation 
#Plotting a line graph with two axies 
fig, ax1 = plt.subplots()

#Setting a color for the plot and for its label
color = "red"
#Including title and labels
plt.title("Rating vs No of Reviews vs Price")
ax1.set_xlabel('Number of Reviews')
ax1.set_ylabel('Rating', color = color)
#Plotting a line graph for Rating vs the Number of reviews
ax1.plot(no_reviews, rating, color = color, label = "Rating vs Number of Reviews")
ax1.tick_params(axis='y', labelcolor=color)
#Placing the label in upper right corner for ease viewing
plt.legend(loc = "upper right")

ax2 = ax1.twinx()
#Setting a color for the plot and for its label
color = "blue" 
#Including labels
ax2.set_ylabel('Price', color = color)
#Converting the price in USD to GBP 
price_in_gbp = func_price_to_gbp(price)
#plotting a line graph for the Price vs the Number of reviews
ax2.plot(no_reviews, price_in_gbp, color = color, label = "Price vs Number of Reviews")
ax2.tick_params(axis='y', labelcolor = color)
#Deleting the space between o and after 7000, for which we do not have data points for. 
plt.xlim(0,7000)
#Placing the label in lower right corner for ease viewing
plt.legend(loc = "lower right")
#Saving the linegraph as an image
plt.savefig("linegraph.png")
plt.show()


#Plotting a scatter graph with price, page and rating
plt.figure()
#Calling the function to get the price per page. 
price_per_page = func_price_per_page(pages, price)
#Creating a scatter plot for rating and the price per page
plt.scatter(rating,price_per_page)
#Including a title for the graph
plt.title("Rating vs Price per Page")
#Including labels
plt.xlabel("Rating of 5")
plt.ylabel("Price per page")
#Saving the scatter subplots as an image
plt.savefig("subplot_1.png")
plt.show()


#Plotting a boxplot 
#Including all the star rating percentages in one list for the box plot
data = [five_star,four_star, three_star, two_star, one_star]
#Including labels for the boxplot
labels_of_data = ["5 Star Rating","4 Star Rating","3 Star Rating","2 Star Rating","1 Star Rating"]
plt.figure()
#Creating a boxplot for each star rating 
plt.boxplot(data, labels = labels_of_data)
#Including a title for the graph
plt.title("Percentages of all Star Ratings")
plt.ylabel("Percentage")
#Saving the boxplot as an image
plt.savefig("boxplot.png")
plt.show()

#Plotting a scatter plot

#Calling the functions to calculate the number of reviews for each rating and assigning it to a list for the scatter plot
data = [numeric_five_star(five_star, no_reviews),numeric_four_star(four_star, no_reviews),numeric_three_star(three_star, no_reviews),numeric_two_star(two_star, no_reviews),numeric_one_star(one_star, no_reviews)]

plt.figure()
plt.figure(figsize=(10,15))
plt.subplot(3,2,1)
#Plotting the subplot for 5 star ratings
plt.scatter(data[0],no_reviews, label = "5 Star Reviews")
#Including a title for the graph
plt.title("Tot 5 star vs Tot reviews")
plt.xlabel("Tot 5 Star ratings")
plt.ylabel("Tot reviews")
plt.legend(loc = "lower right")

plt.subplot(3,2,2)
#Plotting the subplot for 4 star ratings
plt.scatter(data[1],no_reviews, label = "4 Star Reviews")
#Including a title for the graph
plt.title("Tot 4 star vs Tot reviews")
plt.xlabel("Tot 4 Star ratings")
plt.ylabel("Tot reviews")
plt.legend(loc = "lower right")

plt.subplot(3,2,3)
#Plotting the subplot for 3 star ratings
plt.scatter(data[2],no_reviews, label = "3 Star Reviews")
#Including a title for the graph
plt.title("Tot 3 star vs Tot reviews")
plt.xlabel("Tot 3 Star ratings")
plt.ylabel("Tot reviews")
plt.legend(loc = "lower right")

plt.subplot(3,2,4)
#Plotting the subplot for 2 star ratings
plt.scatter(data[3],no_reviews, label = "2 Star Reviews")
#Including a title for the graph
plt.title("Tot 2 star vs Tot reviews")
plt.xlabel("Tot 2 Star ratings")
plt.ylabel("Tot reviews")
plt.legend(loc = "lower right")

plt.subplot(3,2,5)
#Plotting the subplot for 1 star ratings
plt.scatter(data[4],no_reviews, label = "1 Star Review")
#Including a title for the graph
plt.title("Tot 1 star vs Tot reviews")
plt.xlabel("Tot 1 Star ratings")
plt.ylabel("Tot reviews")
plt.legend(loc = "lower right")

#Saving the scatter subplots as an image
plt.savefig("subplot_2.png")
plt.show()

