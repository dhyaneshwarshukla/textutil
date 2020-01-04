# This is my self created file | File Name - views.py

from django.http import HttpResponse
from django.shortcuts import render


# Main Index Page
def index(request):
    params = {'title': 'Index Page', 'au_name': 'Dhyaneshwar Shukla'}
    return render(request, 'index.html', params)


# About Page
def about(request):
    return HttpResponse("Hello, This is My about Page")


# Remove Function
def analyze(request):
    # Getting The Text
    analyzed = ""
    # getting text
    djtext = request.POST.get('string_data', 'default')

    # checking adding conditions and checks
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc == "on":
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char

        params = {'work_process': 'Removing Punctuation', 'analyzed_text': analyzed}
        # Passing the Text to Templates
        return render(request, 'analyze.html', params)

    # if making Caps Lock
    elif fullcaps == 'on':

        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'work_process': 'Making Caps Lock On', 'analyzed_text': analyzed}
        # Passing the Text to Templates
        return render(request, 'analyze.html', params)

    # if Removing Spaces
    elif extraspaceremover == "on":

        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'work_process': 'Extra Space Remover', 'analyzed_text': analyzed}
        # Passing the Text to Templates
        return render(request, 'analyze.html', params)

    # if Removing NewLines
    elif newlineremover == "on":

        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'work_process': 'Removing New Line', 'analyzed_text': analyzed}
        # Passing the Text to Templates
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")

#
# def capfirst(request):
#     return HttpResponse("Captilize First")
#
#
# def newlinerm(request):
#     return HttpResponse("New line Remove")
#
#
# def spacerm(request):
#     return HttpResponse("Space Remove")
#
#
# def charcount(request):
#     return HttpResponse("Count Character")
