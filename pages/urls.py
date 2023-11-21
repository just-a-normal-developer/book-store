from django.urls import path
from . import views


urlpatterns = [
    path('' , views.HomePageView.as_view(), name='home' ),
    path('featured-content/', views.FeaturedContentView.as_view(), name='featured_content'),
    path('recent-updates/', views.RecentUpdatesView.as_view(), name='recent_updates'),

]