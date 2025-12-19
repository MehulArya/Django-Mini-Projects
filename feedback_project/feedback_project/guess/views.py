from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def process_number(request):
    if request.method == "GET":
        value = request.GET.get('guess', 'No guess Provided')
        ctx = { 'val' : value }
        return render(request, 'guess/your_answer.html', ctx)
    return render(request, 'guess/your_answer.html', { 'val': 'No Value Found' })

