import os
import pandas as pd 
import matplotlib.pyplot as plt 
x=pd.read_csv(r"c:\Users\aksha\Downloads\titanic.csv")

"plotting graph to check which gender survival rate was more "

def survival_rate_by_sex():
    x.groupby('Sex')['Survived'].mean().plot(kind='bar')
    plt.title("SURVIVAL RATE BY SEX ")
    plt.xlabel('SEX')
    plt.ylabel('Survival rate')
    plt.show()
survival_rate_by_sex()

"plotting graph to check which class passenger survived the most "

def survival_rate_by_class():
    x.groupby('Pclass')['Survived'].mean().plot(kind='bar')
    plt.title("SURVIVAL RATE BY CLASS ")
    plt.xlabel('PASSENGER_CLASS')
    plt.ylabel('Survival rate')
    plt.show()
survival_rate_by_class()
    