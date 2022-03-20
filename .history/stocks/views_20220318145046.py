from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from stocks.models import Stock,Mysector
from stocks.serializers import StockSerializer, SectorSerializer
from pyFundamental.utils import info,sortStocks
from statistics import mean
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from .forms import OptionsForm
import json
init_data = {
        'sector': 'Technology',
        'dir': 'up',
        'sortBy':'yearReturn'
    }
form=OptionsForm()
@csrf_exempt
def stocks_list2(request):
    template_name='test3.html'
    if request.method=="POST":    
        
        form=OptionsForm(request.POST)
        dir=form.data['sortDirection']
        sector=form.data["sector"]
        sortBy=form.data["sortBy"]
        stocks=Stock.objects.filter(sector=form.data["sector"])
        serializer = StockSerializer(stocks)
        serializer.save

    
        context={
            "form":form,
            "data":  serializer.data
            }
        
       
        return render(template_name=template_name,request=request,context=context)
    if request.method=="GET":    
        form=OptionsForm()
        form=OptionsForm(init_data)
        dir='up'
        sector='all'
        sortBy="marketCap"
        stocks = Stock.objects.filter(sector=sector)
        context={"form":form,
                 "data":stocks
                 }
        stocks=stocks.order_by(sortBy)
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
    
    

