from django.contrib import admin
from django.urls import path
from products import views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.DirectorListAPIView.as_view()),
    path('api/v1/directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('api/v1/movies/', views.MovieListAPIView.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieDetailAPIView.as_view()),
    path('api/v1/reviews/', views.ReviewListAPIView.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewDetailAPIView.as_view()),
    path('api/v1/movies/reviews/', views.GetAverage.as_view()),
    path('api/v1/users/registration/', user_views.RegistrationAPIView.as_view()),
    path('api/v1/users/authorization/', user_views.AuthorizationAPIView.as_view()),
    path('api/v1/users/confirm/', user_views.ConfirmAPIView.as_view())
]