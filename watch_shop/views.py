from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms
from django.views import generic

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from . import forms

















# def watch_shop_view(request):
#     watches = models.Watches.objects.all()
#     return render(request, 'watches/watch.html', {'watch_key': watches})
class WatchesView(generic.ListView):
    template_name = 'watches/watch.html'
    queryset = models.Watches.objects.all()

    def get_queryset(self):
        return models.Watches.objects.all()

# def watch_shop_detail_view(request, id):
#     watch_id = get_object_or_404(models.Watches, id=id)
#     return render(request, 'watches/watch_detail.html', {'watch_id_key': watch_id})
class WatchesDetailView(generic.DetailView):
    template_name = 'watches/watch_detail.html'


    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Watches, id=show_id)

class AddWatchesView(generic.CreateView):
    template_name = 'watches/crud/create_watch.html'
    form_class = forms.WatchShopForm
    queryset = models.Watches.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(AddWatchesView, self).form_valid(form=form)


# def delete_watch_shop_view(request, id):
#     watch_id_delete = get_object_or_404(models.Watches, id=id)
#     watch_id_delete.delete()
#     return HttpResponse('Удаление <<Часов>> прошло успешно!')

class DeleteWatchesView(generic.DeleteView):
    template_name = 'watches/crud/confirm_delete.html'
    success_url = '/'


    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Watches, id=show_id)

class UpdateWatchesView(generic.UpdateView):
    template_name = 'Watches/crud/update_watch.html'
    form_class = forms.WatchShopForm
    success_url = '/'


    def get_object(self, queryset=None):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Watches, id=show_id)


    def form_valid(self, form):
        return super(UpdateWatchesView,self).form_valid(form=form)

class Search(generic.ListView):
    template_name = 'watches/watch.html'
    context_object_name = 'watch'
    paginate_by = 5


    def get_queryset(self):
        return models.Watches.objects.filter(title__icontains=self.request.GET.get('q'))


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context





class RegistrationView(CreateView):
    form_class = forms.RegistrationNewForm
    success_url = '/'
    template_name = 'registration/registration.html'

class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    success_url = '/'
    template_name = 'registration/login.html'


    def get_success_url(self):
        return reverse('users:user_list')

class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'registration/user_list.html'

    def get_queryset(self):
        return User.objects.all()
