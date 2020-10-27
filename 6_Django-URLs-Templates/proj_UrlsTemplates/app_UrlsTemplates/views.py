from django.shortcuts import render

# Create your views here.
def index(request):

    context_dict = {'text': 'hola mundo', 'number': 100}
    
    return render(request, 'app_UrlsTemplates/index.html', context_dict)

def other(request):
    
    return render(request, 'app_UrlsTemplates/other.html')

def relative(request):
    
    return render(request, 'app_UrlsTemplates/urls-templates.html')