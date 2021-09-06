from django.shortcuts import render
from django.http import HttpResponse
import yfinance as yf

from datetime import datetime, timedelta
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like #For solving import pandas_datareader issue
import numpy as np
import datetime
import csv
import requests
import pandas_datareader.data as web
import pandas_datareader as pdr
from pandas_datareader import data, wb


def index(request):
    print(request.GET)
    if request.method=='GET':
        stock=request.GET.get('stock',False)
        start_date=request.GET.get('start date',False)
        end_date=request.GET.get('end date',False )
        tickerData=yf.Ticker(stock)
        tickerDf=tickerData.history(period='1d', start=start_date, end=end_date)
        print(tickerDf)

        # start = datetime.datetime(2018,4,20)
        # end = datetime.datetime(2018,5,20)
        # Today = datetime.datetime.now().strftime ("%Y-%m-%d")

        # # Import list of stock names from NSE website
        # with requests.Session() as s:
        #     download = s.get('https://www.nseindia.com/products/content/sec_bhavdata_full.csv')
        #     decoded_content = download.content.decode('utf-8')
        #     cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        #     my_list = pd.DataFrame(list(cr))
            
        # #View the top rows
        # printmy_list.head()

    return render(request, 'index.html')
    