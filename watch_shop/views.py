from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms

def watch_shop_view(request):
    watches = models.Watches.objects.all()
    return render(request, 'watches/watch.html', {'watch_key': watches})

def watch_shop_detail_view(request, id):
    watch_id = get_object_or_404(models.Watches, id=id)
    return render(request, 'watches/watch_detail.html', {'watch_id_key': watch_id})


def add_watch_shop_view(request):
    method = request.method
    if method == 'POST':
        form = forms.WatchShopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Добавление <<Часов>> прошло успешно!')
    else:
        form = forms.WatchShopForm()
    return render(request, 'watches/crud/create_watch.html', {'form': form})


def delete_watch_shop_view(request, id):
    watch_id_delete = get_object_or_404(models.Watches, id=id)
    watch_id_delete.delete()
    return HttpResponse('Удаление <<Часов>> прошло успешно!')


def update_watch_shop_view(request, id):
    watch_id = get_object_or_404(models.Watches, id=id)
    if request.method == 'POST':
        form = forms.WatchShopForm(instance=watch_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Объект успешно обновлен')
    else:
        form = forms.WatchShopForm(instance=watch_id)

        context = {
            'form': form,
            'object': watch_id
        }
    return render(request, 'watches/crud/update_watch.html', context)

