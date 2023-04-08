# 7-eleven optimization model
We have known 7-11 is a most famous convenience store which have more than 13,000 branches in Thailand, average more than 900 person per day for each branch. From problem, what do we eat when coming to 7-11, it is a simple question but difficult to answer because 7-11 has a lot of kinds of products that look very tasty. Have you ever faced this situation when it is time to eat but you are unable to decide what to eat? Your stomach is dying out of hunger while your brain is like ‘what should I eat?’. During that time, you wish someone, or something could help you make the right choice. Because you have no idea what exactly you want to eat.  

# Project Overview Diagram 
Input:
The input of this project separates to 3 inputs as the following: 
1. 7-11 Product data which extracted nutrients such as calories, fat, carbohydrate and protein and categorize it from web scraping.  
2. 7-11 Product Price from web scraping. 
3. User preferences such as expectation cost, expectation for each nutrient. 

Product Category: 
We categorize 7-11 food products as the following categories. We are interested in only the food products category. Other categories are not included. 

Food product categories
1.	Frozen Food
2.	Appetizer
3.	Beverage
4.	Milk
5.	Bakery
6.	Snack
7.	Ice Cream
8.	Instant Food

Process
Product data Extraction

In this project, we have extracted data from fit-d.com and 7eleven.co.th due to their availability for data scraping. These websites have information about the list of 7-eleven products, cost, and the nutrition of each product and we have extracted and transformed data into SQL database.
