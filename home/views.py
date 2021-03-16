from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
import os


# Create your views here.
def HomeForm_view(request):
    doc = DataDB.objects.all()
    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(request.path)
            # return redirect('success')
    else:
        form = HomeForm()
    return render(request, 'home.html', {'form': form, 'data': doc})


def delete(request, pk):
    doc = DataDB.objects.get(id=pk)
    doc.delete()
    return redirect('/')
