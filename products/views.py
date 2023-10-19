from django.shortcuts import render
# from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


# def search_records(request):
#     return HttpResponse('This is search...')



