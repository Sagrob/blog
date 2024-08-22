from .views import index, about, contact, contact_view, login_view, signup_view, logout_view, post, Post_view, publication_list
from django.urls import path


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('contact/', contact_view, name='contact'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('post/', post, name='post'),
    path('post/', Post_view, name='post'),
    path('publications/', publication_list, name='publications')
]