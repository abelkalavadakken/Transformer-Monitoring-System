from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import View
from .forms import ImageForm
from .models import ImageUpload

# Create your views here.


class MonitorView(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'results.html')
