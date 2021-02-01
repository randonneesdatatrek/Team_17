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
clean = temp.dropna(subset=['Symbol'])

#Export full clean list to local machine
clean.to_csv("nasdaqtraded.txt", sep ="|", index=False)


#Keep stocks without Test Issue
safe = clean[clean['Test Issue'] == "N"]

#Remove Warrant
warrant = safe[~safe['Security Name'].str.contains('Warrant', case=False)]

#Remove symbols with dollar sign
dollar = warrant[~warrant['Symbol'].str.contains('$', regex=False)]

#Remove symbols with period sign
period = dollar[~dollar['Symbol'].str.contains('.', regex=False)]

#Refine selection and keep common stocks only
common = period[period['Security Name'].str.contains('Common', case=False)]

#Select stocks traded on Nasdaq and NYSE only
nasdaq = common[common['Listing Exchange'] == "Q"]
nyse = common[common['Listing Exchange'] == "N"]

#Create final list for both markets
nasdaq_final = nasdaq['Symbol']
nyse_final = nyse['Symbol']

#Export list to csv file on local machine
nasdaq_final.to_csv("commonNasdaq.csv", index=False)
nyse_final.to_csv("commonNYSE.csv", index=False)


