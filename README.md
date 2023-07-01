#Rental Price Checker - Readme

This repository aims to provide a Rental Price Checker (Singapore context) based on a Gradient Boosting Model. 
The objective is to assess whether a room rental price is reasonable or not using this model.

#Purpose

The main purpose of this project is to develop a tool that can be used for personal use in the future, specifically for price negotiation when considering a move from a current rented room.

#Data Collection

The original dataset used for training the model consists of more than 100 records. These records were collected randomly from actual listings on Carousell. Only listings directly posted by owners (not agents) in June 2023 were selected. The raw data can be found in the 'sample_carousell.xlsx' file included in this repository.

#Dataset Description

The dataset comprises 13 features, consisting of 12 categorical variables and 1 continuous variable. The features collected are as follows: Postal Code, Lease, Type, Room, Gender, Air-Con, Cooking, Internet, No Owner Staying, PUB included, Visitors allowed, and (Seller's) Asking Price.

#Demo Website

To try out the Rental Price Checker, you can visit the Demo Website at mrharton1.pythonanywhere.com.
This website showcases the functionality and usage of the model.

Feel free to explore the repository for further details and the implementation of the Gradient Boosting Model for rental price assessment.
