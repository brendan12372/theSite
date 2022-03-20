from django.urls import path
from topTen import views
urlpatterns = [
    # path('front/', views.front_list),
    # path('front/<int:pk>/', views.stocks_detail),
    path('sector/', views.sector_view,name='sector'),
    path('home/', views.vTwo,name='sort'),
    path('',views.home,name='home'),
    path('<int:pk>/', views.detail.as_view(),name='detail'),


]