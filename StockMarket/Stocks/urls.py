from django.urls import path
from .views import StockView, AjaxView

urlpatterns = [
    path('stocks/', StockView.as_view(), name='stocks_url'),
    path('astocks/', AjaxView.as_view(), name='stocks_url'),
]