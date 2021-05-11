from django.shortcuts import render

from django.http import JsonResponse
def names(request):
    return JsonResponse({'names': ['William', 'Rod', 'Grant']})
