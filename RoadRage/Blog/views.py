from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def home(request):
    title = "RoadRage"

    context = {
        'title': title,
    }

    return render(request, 'index.html', context)

def sign_up(request):
    form = UserCreationForm()
    context = {'form': form}

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'sign_up.html',context)