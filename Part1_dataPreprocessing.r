---
title: "R Notebook for ML_A-Z step by step Part1 Data processing"
output: html_notebook
---
#by default naming is bad, so I used R studio set working directory to replace this operation
#setwd("D:\\AI_Docs\Udemy\ML_A-Z\Machine Learning A-Z Template Folder\\Part 1 - Data Preprocessing\\Section 2 -------------------- Part 1 - Data Preprocessing --------------------")

dataset = read.csv("Data.csv")
head(dataset)

X = dataset[,1:length(dataset)-1]
X
length(dataset)# length of DataFrame.coloums

Y = dataset[,length(dataset)]
Y


#taking care of missing data
#ifelse(booleanExp, T-process, F-process) 很像三元運算子
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN=function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Salary, FUN=function(x) mean(x, na.rm = TRUE)),
                     dataset$Salary)
dataset
