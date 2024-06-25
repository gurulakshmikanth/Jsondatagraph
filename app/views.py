from django.http import JsonResponse
from app.models import *
from django.shortcuts import render
import json
from datetime import datetime
from django.http import HttpResponse




def data(self):

    

    with open('C:\\Users\\guruk\\OneDrive\\Desktop\\django\\kanth\\Scripts\\Dashboard2\\app\\jsondata.json','r',encoding='utf-8') as f:
        data1 = json.load(f)

    for entry in data1:
        published1=datetime.strptime(entry['published'], "%B, %d %Y %H:%M:%S") if 'published' in entry and entry['published'] else None
        intensity=entry['intensity'] if 'intensity' in entry and entry['intensity'] else None
        likelihood=entry['likelihood'] if 'likelihood' in entry and entry['likelihood'] else None
        relevance=entry['relevance'] if 'relevance' in entry and entry['relevance'] else None
        DataEntry.objects.create(
            end_year=entry.get('end_year'),
            intensity=intensity,
            sector=entry.get('sector'),
            topic=entry['topic'],
            insight=entry['insight'],
            url=entry['url'],
            region=entry['region'],
            start_year=entry.get('start_year'),
            impact=entry.get('impact'),
            added=datetime.strptime(entry['added'], "%B, %d %Y %H:%M:%S"),

            published=published1,
            country=entry.get('country'),
            relevance=relevance,
            pestle=entry['pestle'],
            source=entry['source'],
            title=entry['title'],
            likelihood=likelihood
        )
    return HttpResponse('Data entered successfully')
    




def get_data(request):
    entries = DataEntry.objects.all().values()
    return JsonResponse(list(entries), safe=False)

def dashboard(request):
    return render(request, 'dashboard.html')
