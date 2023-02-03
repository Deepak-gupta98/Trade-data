from django.shortcuts import render
from django.http import HttpResponse
import csv, json

# Create your views here.

def home(request):
    return HttpResponse("Hello Deepak")

class Trade:
    def __init__(self):
        pass

def convert_into_timeframe(request, csv_file, data_stored, timeframe=10):
    data = {}
    data['BANKNIFTY'] = csv_file[0][0]
    data['DATE'] = csv_file[0][1]
    data['TIME'] = csv_file[0][2]
    data['OPEN'] = csv_file[0][3]
    data['HIGH'] = max(csv_file[:][4])
    data['LOW'] = min(csv_file[:][5])
    data['CLOSE'] = csv_file[:][6]
    data['VOLUME'] = min(csv_file[:][7])
    data_stored.append(data)



def get_csv_file(request):
    file = open(r'NIFTY_F1_Xm8mAtb.csv')
    csv_file = csv.reader(file)
    rows = []
    data_stored = []
    count =0
    timeframe = 10

    for row in csv_file:
        count=count+1
        rows.append(row)
        if(count%timeframe == 0):
            convert_into_timeframe(request, rows, data_stored,timeframe)
            count=0
            rows = []
    
    print(len(data_stored))
    return HttpResponse(json.dumps(data_stored))
