from django.urls import path
from .views import ClientListCreateView, ClientCommentListCreateView, ClientDetailView

app_name = 'crm'

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('clients/<int:client_id>/comments/', ClientCommentListCreateView.as_view(), name='client-comment-list-create')
]