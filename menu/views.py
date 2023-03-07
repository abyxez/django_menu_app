from django.shortcuts import render
from menu.forms import GenreForm
from menu.models import Genre

def create_menu(request):
    form = GenreForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
    context = {
        'form': form,
    }
    return render(request, 'menu/create_menu.html', context)


def index(request):
    return render(request, 'menu/index.html', {'genres': Genre.objects.all()})