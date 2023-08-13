import json
import pytz
from django.shortcuts import render
from django.views import View
from . models import *
from datetime import datetime
from django.utils import timezone

class UploadJsonView(View):
    template_name = 'upload_json.html'

    def get(self, request):
        # EnergyOutlook.objects.all().delete()
        return render(request, self.template_name)

    def post(self,request):
        uploaded_file = request.FILES.get('json_file')

        if uploaded_file and uploaded_file.name.endswith('.json'):
            try:
                json_data = json.load(uploaded_file)
                for entry in json_data:
                    try:
                        likelihood = entry.get('likelihood')
                        relevance = entry.get('relevance')
                        added_date_str = entry.get('added')
                        published_date_str = entry.get('published')

                        added_date = self.convert_datetime_format(added_date_str)
                        published_date = self.convert_datetime_format(published_date_str)

                        intensity_value = entry.get('intensity')
                        if intensity_value is not None and intensity_value != '':
                            intensity = int(intensity_value)
                        else:
                            intensity = 0
                                                
                        EnergyOutlook.objects.create(
                            end_year    =  entry.get('end_year'),
                            intensity   =  intensity,
                            sector      =  entry.get('sector'),
                            topic       =  entry.get('topic'),
                            insight     =  entry.get('insight'),
                            url         =  entry.get('url'),
                            region      =  entry.get('region'),
                            start_year  =  entry.get('start_year'),
                            impact      =  entry.get('impact'),
                            added       =  added_date,
                            published   =  published_date,
                            country     =  entry.get('country'),
                            relevance   =  relevance if relevance else 0,
                            pestle      =  entry.get('pestle'),
                            source      =  entry.get('source'),
                            title       =  entry.get('title'),
                            likelihood  =  likelihood if likelihood else 0
                        )
                    except Exception as e:
                        return render(request, self.template_name, {'error': str(e)})
                        
            except json.JSONDecodeError:
                return render(request, self.template_name, {'error': 'Invalid JSON format'})
                        
        return render(request, self.template_name, {'error': 'Please upload a valid JSON file'})
    
    def convert_datetime_format(self, datetime_str):
        try:
            parsed_datetime = datetime.strptime(datetime_str, "%B, %d %Y %H:%M:%S")
            formatted_datetime = timezone.make_aware(parsed_datetime).strftime("%Y-%m-%d %H:%M:%S")
            return formatted_datetime
        except ValueError:
            return None

def dashboard(request):
    data = EnergyOutlook.objects.all()

    end_year_filter = request.GET.get('end_year')
    if end_year_filter:
        data = data.filter(end_year=end_year_filter)

    topic_filter = request.GET.get('topic')
    if topic_filter:
        data = data.filter(topic=topic_filter)

    sector_filter = request.GET.get('sector')
    if sector_filter:
        data = data.filter(sector=sector_filter)

    region_filter = request.GET.get('region')
    if region_filter:
        data = data.filter(region=region_filter)

    pest_filter = request.GET.get('pest')
    if pest_filter:
        data = data.filter(pestle=pest_filter)

    source_filter = request.GET.get('source')
    if source_filter:
        data = data.filter(source=source_filter)

    swot_filter = request.GET.get('swot')
    if swot_filter:
        data = data.filter(swot=swot_filter)

    country_filter = request.GET.get('country')
    if country_filter:
        data = data.filter(country=country_filter)
        
    return render(request, "dashboard.html", {'data': data})























# def ConvertJsonToDataBase(request):

#     return render(request,"index.html",context)



