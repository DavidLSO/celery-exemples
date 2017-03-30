from django.shortcuts import render
from tcelery.core.tasks import add_sum


def lister(request):
    for x in range(0, 10):
        add_sum.delay(x)
    return render(request, 'index.html', {})
