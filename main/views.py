from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

from .forms import LinkForm
from .models import Link


def index(request):

    short_id = ''
    form = LinkForm()
    if request.method == 'POST':
        full_link = f'http://{request.POST.get("full_link")}'
        if Link.objects.filter(full_link=full_link):
            short_id = Link.objects.filter(full_link=full_link).first().short_id
        else:
            short_id = create_short_id()
            Link.objects.create(full_link=full_link, short_id=short_id)

    return render(request, 'index.html', {'form': form, 'short_id': short_id})


def create_short_id():

    short_id_len = 6
    while True:
        short_id = get_random_string(short_id_len)
        if not(Link.objects.filter(short_id=short_id)):
            return short_id


def redirect_to_full(request, short_id):

    try:
        return redirect(Link.objects.filter(short_id=short_id).first().full_link)
    except AttributeError:
        return HttpResponse('')
