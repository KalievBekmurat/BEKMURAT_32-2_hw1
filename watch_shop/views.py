from django.shortcuts import render, get_object_or_404

from . import models

def watch_shop_view(request):
    watches = models.Watches.objects.all()
    return render(request, 'watches/watch.html', {'watch_key': watches})

def watch_shop_detail_view(request, id):
    watch_id = get_object_or_404(models.Watches, id=id)
    return render(request, 'watches/watch_detail.html', {'watch_id_key': watch_id})
