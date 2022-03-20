from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from stocks.models import Stock,Mysector
from stocks.serializers import StockSerializer, SectorSerializer
from pyFundamental.utils import info
from statistics import mean
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

def stocks_list2(request):
    stocks = Stock.objects.all()
    serializer = StockSerializer(stocks, many=True)
    if request.method == 'GET':
        sector='all'
        dir='up',
        sortBy='MarketCap'
        if sector !='all':
            stocks = Stock.objects.filter(sector=sector)
        else:
            stocks = Stock.objects.all()
        if dir =='up':
            stocks=stocks.order_by(sortBy)
        if dir=='down':
            stocks=stocks.order_by("-"+sortBy)
            
        
       

        serializer = StockSerializer(stocks, many=True)
        x=serializer.data[0]["symbol"]
        symbols=[]
        values=[]
        for s in serializer.data:
            symbols.append(s["symbol"])
            values.append(s[sortBy])
        print(symbols) 
        d=dict(zip(symbols,values))    
       
        
    
    context={
      "data": d,
             }
      
    
    

    template_name="test3.html"

    # stream = io.BytesIO(json)
    # data = JSONParser().parse(stream)
        
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


     
def stocks_detail2(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        stock = Stock.objects.get(pk=pk)
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
    
    

