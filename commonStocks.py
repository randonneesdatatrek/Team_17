# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:57:40 2021

@author: Benoit
"""

#Import libraries
import pandas as pd


#Import list of companies traded on various exchanges (the file is available on Nasdaq ftp directory)
target = "ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqtraded.txt"
temp = pd.read_csv(target, sep="|")

#Remove last line containing info about file creation time
main = temp.dropna(subset=['Symbol'])

#Select stocks traded on Nasdaq and NYSE only
stocks = main[(main['Listing Exchange'] == "Q") | (main['Listing Exchange'] == "N")]

#Refine selection and keep common stocks only
common = stocks[stocks['Security Name'].str.contains('Common', case=False)]

#Create final list of common stocks
final = common['Symbol']

#Export list to csv file
final.to_csv("commonStocks.csv", header=False, index=False)
