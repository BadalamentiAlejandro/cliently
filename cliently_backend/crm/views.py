from rest_framework import generics
from .models import Client, Comment
from .serializers import ClientSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


User = get_user_model()


class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]


class ClientCommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated] # El usuario que crea el comentario debe estar autenticado.

    def get_queryset(self):
        client_id = self.kwargs['client_id']
        client = get_object_or_404(Client, id=client_id)
        return Comment.objects.filter(client = client) # Retorna los comentarios del cliente con el id especificado.

    def perform_create(self, serializer):
        client_id = self.kwargs['client_id']
        client = get_object_or_404(Client, id=client_id)
        serializer.save(user = self.request.user, client = client) # Pasa el usuario autenticado y cliente referido al modelo ya que son read_only.


class ClientCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated] # El usuario que crea el comentario debe estar autenticado.

    def get_queryset(self):
        client_id = self.kwargs['client_id']
        client = get_object_or_404(Client, id=client_id)
        return Comment.objects.filter(client = client) # Retorna los comentarios del cliente con el id especificado.