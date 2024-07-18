from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import MyForm

def myview(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            # cleaned_data로 관련 로직 처리
            return HttpResponseRedirect('/success/')
    else:
        form = MyForm(initial={'key': 'value'})
        return render(request, 'form_template.html', {'form': form})
