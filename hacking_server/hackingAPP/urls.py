from django.urls import path
from .views import all_hack_view, Home, post_hacking


urlpatterns = [

    path('', Home),
    path('allhacking/', all_hack_view, name='allhacking-view'),
    path('post-hacking', post_hacking, name='post-hacking-view')

    ]