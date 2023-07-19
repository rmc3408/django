from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from enum import Enum


class MontlyAnswersEnum(Enum):
    january = 'Happy new year'
    february = 'Happy Valentines'
    march = 'End of winter'
    july = 'Raph birthday'


def monthly(request, month):

    # if month in MontlyAnswersEnum.__members__:
    #     return HttpResponse(MontlyAnswersEnum[month].value)

    # return HttpResponseNotFound('Wrong path')

    try:
        return HttpResponse(MontlyAnswersEnum[month].value)
    except:
        return HttpResponseNotFound('Wrong path')


def monthly_byNum(request, month):

    if month > len(MontlyAnswersEnum):
        return HttpResponseNotFound('Wrong month number')
    
    monthsKeyList = [i.name for i in MontlyAnswersEnum]

    redirect_url = reverse('named-month', args=[monthsKeyList[month-1]])
    return HttpResponseRedirect(redirect_url)

def listMonths(request):
    start_Html_view = """
        <h1> Months Avaliable </h1>
        <ul> 
    """

    monthsKeyList = [i.name for i in MontlyAnswersEnum]
    for month in monthsKeyList:
        month_path = reverse('named-month', args=[month])
        start_Html_view += f'<li><a href={month_path} alt={month}>{month.capitalize()}</a></li>'
    list_html_view = start_Html_view + "</ul>"


    return HttpResponse(list_html_view)