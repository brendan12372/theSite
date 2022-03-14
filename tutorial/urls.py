from django.urls import path, include
from django.contrib import admin

urlpatterns = [
path('admin/', admin.site.urls),
path('', include('stocks.urls')),
path('topTen/', include('topTen.urls')),

]