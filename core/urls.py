from django.urls import path
from core import views


urlpatterns = [
    # path('',views.index)
    path('',views.homepage,name='home'),
    path('about/',views.aboutpage, name= 'about'),
    path('contact/',views.contact, name='contact'),
]
