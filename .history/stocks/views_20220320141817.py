from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from stocks.models import Stock,Mysector
from stocks.serializers import StockSerializer, SectorSerializer
from pyFundamental.utils import info,sortStocks,sectorLL,info
from statistics import mean
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from .forms import OptionsForm,sForm
import json
print(sectorLL)

from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


init_data = {
        'sector': 'all',
        'dir': 'down',
        'sortBy':'marketCap'
    }

@csrf_exempt
def stocks_list2(request):
    template_name='test3.html'
    if request.method=="POST":    
        form2=sForm(request.POST)
        form=OptionsForm(request.POST)
        
        if form.is_valid():
            dir=form.data['sortDirection']
            sector=form.data["sector"]
            sortBy=form.data["sortBy"]
            try:
                ii=info[sortBy]
            except:
                ii="test"
            
            if sector=='all':
                stocks=Stock.objects.all()
            else:
                stocks=Stock.objects.filter(sector=sector)
            if form.data["sortDirection"]=='up':
                stocks=stocks.order_by(sortBy)
            else:
                stocks=stocks.order_by('-'+sortBy)
        
            
            serializer = StockSerializer(stocks,many=True)
            serializer.save
            symbols=[]
            vals=[]
            urls=[]
        myDict={}
        for i in range(len(serializer.data)):
            x=serializer.data[i]
            symbols.append(x["symbol"])
            vals.append(x[sortBy])
        
        myDict=dict(zip(symbols,vals))
        myDict2=dict(zip(symbols,urls))
        print(myDict)
        
        context={
            "form2":form2,
            "form":form,
            "info":ii,
            "sortBy":sortBy,
            "data":  myDict,
            "data2": myDict2,
            "dollars": ["marketCap","operatingCashflow","ebita"]
            }
        
       
        return render(template_name=template_name,request=request,context=context)
    if request.method=="GET":    
        
        form=OptionsForm()
        dir='up'
        sector='all'
        sortBy="marketCap"
        
                
        if sector=='all':
            stocks=Stock.objects.all()
        else:
            stocks=Stock.objects.filter(sector=sector)
        if sortBy=='up':
            stocks=stocks.order_by(sortBy)
        else:
            stocks=stocks.order_by('-'+sortBy)
        
        serializer = StockSerializer(stocks,many=True)
        serializer.save
        symbols=[]
        vals=[]
        myDict={}
        for i in range(len(serializer.data)):
            x=serializer.data[i]
            symbols.append(x["symbol"])
            vals.append(x[sortBy])
        myDict=dict(zip(symbols,vals))
        print(myDict)
        context={
            
            "form":form,
            "data":  myDict
            }
        return render(template_name=template_name,request=request,context=context)
  

@api_view(['GET', 'POST'])
def stocks_list(request,sector,sortBy,dir):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        print(sector)
        if sector !='all':
            stocks = Stock.objects.filter(sector=sector)
        else:
            stocks = Stock.objects.all()
        if dir =='up':
            stocks=stocks.order_by(sortBy)
        if dir=='down':
            stocks=stocks.order_by("-"+sortBy)

        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def stocks_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        stock = Stock.objects.get(pk=pk)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StockSerializer(stock)
        return Response(serializer.data)


    elif request.method == 'DELETE':
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET'])
def sector_list(request,sortBy,dir):
    if request.method == 'GET':
        xxx=Mysector.objects.all()

        for s in Mysector.objects.all():
            s.get_ave(sortBy)
            s.save()

        sec_list=Mysector.objects.all()
        stockL=Stock.objects.all()




        if dir=='up':
            serializer = SectorSerializer(sec_list.order_by('-ave'), many=True)
        if dir=='down':
            serializer = SectorSerializer(sec_list.order_by('ave'), many=True)
        
        return Response(serializer.data)


     
def stocks_detail2(request, symbol):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        stock = Stock.objects.get(symbol=symbol)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StockSerializer(stock)
        
        context={"data":serializer.data}
        template_name="sd.html"
        
        return render(template_name=template_name,request=request,context=context)


    elif request.method == 'DELETE':
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

