from django.shortcuts import render
from rest_framework import viewsets
from .models import Game
from .serializers import GameSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Review
from .serializers import ReviewSerializer
from .models import Wishlist
from .serializers import WishlistSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .permissions import IsOwnerOrReadOnly

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all() 
    permission_classes = [AllowAny]
    serializer_class = UserSerializer



class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['genre', 'platform', 'year']
    search_fields = ['title', 'description']
    ordering_fields = ['year', 'title']



class GameReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
            serializer.save(user=self.request.user)

class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

