from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def add(request):
    val1 = request.POST['res']
    no_of_words = len(val1.split())
    
    return render(request, 'result.html', {'no_of_words': no_of_words})
