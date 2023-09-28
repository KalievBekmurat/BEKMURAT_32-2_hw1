from django.urls import path
from . import views

urlpatterns = [
    path('', views.WatchesView.as_view(), name='watch'),
    path('watch_detail/<int:id>/', views.WatchesDetailView.as_view(), name = 'watch_detail'),
    path('watch_detail/<int:id>/update/', views.UpdateWatchesView.as_view(), name='update_watch'),
    path('watch_detail/<int:id>/delete/', views.DeleteWatchesView.as_view(), name="delete_watch"),
    path('create_watch/', views.AddWatchesView.as_view(), name='create_watch'),
    path('search/', views.Search.as_view(), name='search')
]