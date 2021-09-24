from django.http import response
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
import yfinance as yf

import pandas as pd
import requests

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

from rest_framework.views import APIView
from rest_framework.response import Response

from django.views.generic import View

date = []
values = []


def get_data(request, *args, **kwargs):

    data ={
        "sales" : 100,
        "person": 10000,
    }
    return JsonResponse(data) # http response

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
   
    def get(self, request, format = None):
        
        labels = [
            'January',
            'February', 
            'March', 
            'April', 
            'May', 
            'June', 
            'July'
            ]
        chartLabel = "my data"
        chartdata = [0, 10, 5, 2, 20, 30, 45]
        labels = date
        chartdata = values
        data ={
                     "labels":labels,
                     "chartLabel":chartLabel,
                     "chartdata":chartdata,
             }
        return Response(data)

def index(request):
    print(request.GET)
    if request.method=='GET':
        stock=request.GET.get('stock',False)
        start_date=request.GET.get('start date',False)
        end_date=request.GET.get('end date',False )
        if stock:
            tickerData=yf.Ticker(stock)
            tickerDf=tickerData.history(period='1d', start=start_date, end=end_date)
            print(tickerDf)
            stock_data = tickerDf.values.tolist()
            print(stock_data)
            values.clear()
            date.clear()
            
            
            for l in stock_data:
                values.append(l[0])
                values.append(l[3])
    
            data_top = tickerDf.head()
            date.append(start_date)
            for i in range(len(values)-2):
                date.append(" ")
            date.append(end_date)
            print(len(date))
            print(len(values))
            return render(request, 'graph.html')

        # if stock!=None:


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
        # print(my_list.head())

    return render(request, 'index.html')
    