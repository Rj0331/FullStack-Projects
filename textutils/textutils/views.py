# Created by User
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcounter = request.GET.get('charcounter', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif fullcaps == "on":
        analyzed = " "
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif charcounter == "on":
        analyzed = len(djtext)
        
        params = {'purpose': 'Total Characters is', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")
# def captfirst(request):
#     return HttpResponse("captfirst")
# def charcount(request):
#     return HttpResponse("charcount")
# def spaceremove(request):
#     return HttpResponse("spaceremove")
# def newlineremove(request):
#     return HttpResponse("newlineremove")
