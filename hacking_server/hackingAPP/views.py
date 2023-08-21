from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Hacking_data
from django.views.decorators.csrf import csrf_exempt


def Home(req):
    return HttpResponse('<h1>Hello</h1>')




def all_hack_view(req):
    data = Hacking_data.objects.all().values()
    data = list(data)

    return JsonResponse(data, safe=False)

@csrf_exempt
def post_hacking(req):

    if req.method == 'POST':
        data = req.POST.copy()
        source = data.get('source')
        content = data.get('data')

        

        hacking_table = Hacking_data()

        hacking_table.source = source
        hacking_table.data = content
        hacking_table.save()
    

    return HttpResponse(Hacking_data.objects.all().values())








