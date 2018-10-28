# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import numpy as np
import pandas as pd

os.chdir("C:\\Users\\zhang mali\\Documents\\Alteryx Data\\01_World Bank")

wdi_loan = pd.read_csv("WDI Loan Data.csv", encoding = "ISO-8859-1")
loan_code = pd.read_excel("Loan Lookup Table.xlsx")

loan_code['Topic1'], loan_code['Topic2']=loan_code['Topic'].str.split(': ',1).str

wdi_loan.shape
list(wdi_loan)
wdi_loan.dtypes

wdi_loan_long = pd.melt(wdi_loan, id_vars = ['Country Name','Country Code',
                                             'Indicator Name','Indicator Code'])
wdi_loan_long = wdi_loan_long.rename(columns={"variable": "Year", "value": "Loan"})
wdi_loan_long['Year'] = wdi_loan_long['Year'].astype(int)
wdi_loan_long2 = wdi_loan_long.loc[(wdi_loan_long['Loan'].notnull()) & 
                                   (wdi_loan_long['Year']>=2009)]

wdi_loan_merge = pd.merge(wdi_loan_long2, loan_code, how = 'left', 
                       left_on='Indicator Code', right_on = 'Series Code')
