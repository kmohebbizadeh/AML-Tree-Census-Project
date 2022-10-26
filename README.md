# AML-Tree-Census-Project

**COMS 4995 - Applied Machine Learning: Fall 2022**

**Group 8 Project Proposal**

**Names:** 
Kiyan Mohebbizadeh (km3826), Anne Wei (yw3939), Wenxi Zhang (wz2615), Zhening Zhang (zz3040), Tal Zussman (tz2294)

***Background & Context***

Every decade since 1995, New York City has conducted a census of all trees within city borders. This census involves collecting data about each tree, such as species, diameter, health status, and many more data points. The most recent census occurred in 2015, and surveyed more than 680,000 trees in NYC. In this dataset, each tree’s health status is recorded as either Good, Fair, or Poor. We aim to determine a given tree’s health status based on the various parameters available in the data set.

***Identification and Description***

**Source:**
New York City Open Data

**Dataset:**
data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh

The dataset includes every tree in New York City as of 2015 and includes (but is not limited to) the tree's location by borough, zip code, and latitude/longitude, species by both Latin and common names, size, health, and issues with the tree's roots, trunk, and branches.

There are a total of 45 features and 683,788 rows, with each row corresponding to a single unique tree.
Proposed ML Techniques
Since tree health statuses are categories in this dataset (Good, Fair, and Poor), predicting a tree’s health will be a classification task. As such, linear and ridge regression are not the best models for this task.

The following are potential ML techniques which are viable for classification tasks:
Logistic regression with ordinal responses 
Decision Tree
Random Forest
K-nearest-neighbor
Support Vector Machine
Naive Bayes Classification

Using these techniques, we will create models and evaluate them to find the best model for this particular task.
