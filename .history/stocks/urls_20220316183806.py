from django.urls import path
from stocks import views
from django.contrib import admin

urlpatterns = [
    # path('stocks/', views.stocks_list),
    path('', views.stocks_list2),
    path('<int:pk>/', views.stocks_detail2),
    path('<str:sector>/<str:sortBy>/<str:dir>', views.stocks_list),
    path('sectors/<str:sortBy>/<str:dir>', views.sector_list),
    path('frontend/<int:pk>/',views.stocks_detail2, name= 'myD' )
]