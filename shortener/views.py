import hashlib

from django.shortcuts import render, redirect
from shortener.forms import SetUrlForm
from shortener.models import Link


def set_url(request):
    if request.method == 'POST':
        form = SetUrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('full_url')
            url_hash = hashlib.sha256(url.encode()).hexdigest()
            form.instance.short = url_hash
            form.save()
            return render(request, 'shortener/original_url.html',
                          {'short_url': f'{request.get_host()}/{url_hash}'})
    else:
        form = SetUrlForm()
    return render(request, 'shortener/home.html', {'form': form})


def go_to_original(request, short):
    original = Link.objects.get(short=short)
    original_url = original.full_url
    return redirect(original_url)
