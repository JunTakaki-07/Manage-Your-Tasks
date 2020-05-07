
from django.urls import path
from .views import is_tasklist, is_detail, Is_delete, Is_update, Is_create

urlpatterns = [
    path('tasklist/', is_tasklist, name='tasklist'),
    path('detail/<int:pk>', is_detail, name='detail'),
    path('delete/<int:pk>', Is_delete.as_view(), name='delete'),
    path('create/', Is_create.as_view(), name='create'),
    path('update/<int:pk>', Is_update.as_view(), name='update'),
]

