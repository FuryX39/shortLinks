from django.shortcuts import render
from django.utils.crypto import get_random_string

from .forms import LinkForm
from .models import Link


def index(request):

    short_id = ''
    form = LinkForm()
    if request.method == 'POST':
        short_id = create_short_id()
        Link.objects.create(full_link=request.POST.get('full_link'), short_id=short_id)

    return render(request, 'index.html', {'form': form, 'short_id': short_id})


def create_short_id():

    short_id_len = 6
    while True:
        short_id = get_random_string(short_id_len)
        if not(Link.objects.filter(short_id=short_id)):
            return short_id
