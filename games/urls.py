from rest_framework.routers import DefaultRouter
from .views import GameViewSet
from .views import GameReviewViewSet
from .views import WishlistViewSet, GameViewSet, RegisterView, GameReviewViewSet
from django.urls import path

router = DefaultRouter()
router.register('games', GameViewSet)
router.register('reviews', GameReviewViewSet)
router.register('wishlist', WishlistViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view()),]+ router.urls

