from django.urls import path
from webapp import views as webapp_views


urlpatterns = [
    path('', webapp_views.create_cat_menu),
    path('action/', webapp_views.action)
]