from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from .models import Country
from .forms import CountryForm
import pycountry
import math
# Create your views here.
class StatCovid(View):
    def get(self, request):
        form = CountryForm()
        countries = Country.objects.all()

        # ----------------------------------

        country_list = []
        country_list_1 = []
        country_list_2 = []
        country_list_3 = []
        country_list_4 = []
        for country in pycountry.countries:
            country_list.append(country.name)
        stop_1 = math.ceil(len(country_list)/4)
        stop_2 = 2 * stop_1
        stop_3 = 3 * stop_1
        stop_4 = len(country_list)
        for i in range(stop_1):
            country_list_1.append(country_list[i])
        for i in range(stop_1, stop_2):
            country_list_2.append(country_list[i])
        for i in range(stop_2, stop_3):
            country_list_3.append(country_list[i])
        for i in range(stop_3, stop_4):
            country_list_4.append(country_list[i])
        
        # ----------------------------------
        
        response = {
            'countries':countries, 
            'form':form, 
            'country_list_1':country_list_1,
            'country_list_2':country_list_2,
            'country_list_3':country_list_3,
            'country_list_4':country_list_4,
            }
        return render(request, 'index.html', response)

    # gajadi dipake kayakny
    def post(self, request):
        form = CountryForm(request.POST or None)
        if (request.method == "POST" and form.is_valid()):
            print("berhasil")
            new_data = form.save()
            # return JsonResponse({'country': model_to_dict(new_data)}, status=200)
            return redirect('StatCovid')
        else:
            return redirect('StatCovid')

# def stat(request):
#     country_url = []
#     countries = Country.objects.all()
#     for country in countries:
#         country_url.append("https://ourworldindata.org/explorers/coronavirus-data-explorer?zoomToSelection=true&facet=none&pickerSort=asc&pickerMetric=location&Metric=Confirmed+cases&Interval=7-day+rolling+average&Relative+to+Population=true&Align+outbreaks=false&country=~" + getattr(country, 'code') + "&hideControls=true")
#     response = {'country_url':country_url}
#     return render(request, 'stat.html', response)