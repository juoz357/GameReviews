from django.urls import path
from .views import ReviewListView, ReviewDetailView, ReviewCreateView, GameCreateView, ReviewUpdateView, ReviewDeleteView, UserReviewListView
from . import views


urlpatterns = [
    path('', ReviewListView.as_view(), name='reviews-home'),
    path('user/<str:username>', UserReviewListView.as_view(), name='user-reviews'),
    path('about/', views.about, name='reviews-about'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='reviews-detail'),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name='reviews-update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='reviews-delete'),
    path('review/new/', ReviewCreateView.as_view(), name='reviews-create'),
    path('game/new/', GameCreateView.as_view(), name='game-create'),


]