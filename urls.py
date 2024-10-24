from django.urls import path
from .views import AboutView,ContactView,HomeView, get_teachers

urlpatterns = [
    path('', HomeView.as_view(), name='HomeView'),
    path('about/', AboutView.as_view(template_name='Home/about.html'), name='AboutView'),
    path('contact/', ContactView.as_view(template_name='Home/contact.html'), name='ContactView'),
    #path('login/',
         #auth_views.LoginView.as_view(template_name='Review/login.html'),
         #name='LoginView'),

    path('ajax_calls/autocomplete_search_func', get_teachers, name='get_teachers'),
]
