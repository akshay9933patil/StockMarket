from django.shortcuts import render
from django import views
from bsedata.bse import BSE
import random
from django.http import JsonResponse


class StockView(views.View):

    def get(self, request):
        template_name = 'Stocks/stocks.html'
        number = random.randint(1, 10)
        bse = BSE(update_codes=True)
        stock_codes = [str(code) for code in bse.getScripCodes()]
        # print(len(stock_codes))
        stocks = []
        for code in stock_codes[:number:]:
            try:
                quote = bse.getQuote(code)
                stocks.append(quote)
            except Exception as e:
                pass

        context = {'data':['akshay', 'patil'], 'stocks':stocks}
        return render(request=request, template_name=template_name, context=context)

class AjaxView(views.View):

    def get(self, request):
        template_name = 'Stocks/stocks.html'

        number = random.randint(1, 10)
        bse = BSE(update_codes=True)

        # returns companys stock's code number with which we can access stock data
        stock_codes = [str(code) for code in bse.getScripCodes()]
        stocks = []
        for code in stock_codes[:number:]:

            # Exception handeling used to handle the exception raise
            # due to inactive stock_code
            try:
                quote = bse.getQuote(code)
                stocks.append(quote)
            except Exception as error:
                pass
        """use below for loop instead of above"""
        """
        for code in stock_codes[:10:]:

            # Exception handeling used to handle the exception raise
            # due to inactive stock_code
            try:
                quote = bse.getQuote(code)
                stocks.append(quote)
            except Exception as e:
                pass
        """
        
        return JsonResponse({'stocks':stocks})

