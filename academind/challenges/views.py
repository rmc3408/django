from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from enum import Enum


class MontlyAnswersEnum(Enum):
    january = 'Happy new year'
    february = 'Happy Valentines'
    march = 'End of winter'
    july = 'Raph birthday'
    december = None


def monthly(request, month):

    # if month in MontlyAnswersEnum.__members__:
    #     return HttpResponse(MontlyAnswersEnum[month].value)

    # return HttpResponseNotFound('Wrong path')

    try:
        textMonth = MontlyAnswersEnum[month].value
        return render(request, "challenges/month.html", { "month": month, "text": textMonth })

        # response = render_to_string("challenges/index.html")
        # return HttpResponse(response)
        
        # return HttpResponse(MontlyAnswersEnum[month].value)
    except:
        # raise Http404()
        
        response_stringed = render_to_string('404.html')
        return HttpResponseNotFound(response_stringed)
        
        # return HttpResponseNotFound('Wrong path')


def monthly_byNum(request, month):

    if month > len(MontlyAnswersEnum):
        return HttpResponseNotFound('Wrong month number')
    
    monthsKeyList = [i.name for i in MontlyAnswersEnum]

    redirect_url = reverse('named-month', args=[monthsKeyList[month-1]])
    return HttpResponseRedirect(redirect_url)


def listMonths(request):

    monthsKeyList = [i.name for i in MontlyAnswersEnum]
    monthsKeyList = MontlyAnswersEnum._member_names_

    # start_Html_view = """
    #     <h1> Months Avaliable </h1>
    #     <ul> 
    # """
    # for month in monthsKeyList:
    #     month_path = reverse('named-month', args=[month])
    #     start_Html_view += f'<li><a href={month_path} alt={month}>{month.capitalize()}</a></li>'
    # final_html_view = start_Html_view + "</ul>"
    # return HttpResponse(final_html_view)

    return render(request, "challenges/list.html", { "months": monthsKeyList })

