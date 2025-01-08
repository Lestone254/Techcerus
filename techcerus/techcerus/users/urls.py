from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', techcerus, name='techcerus'),
    path('BlogItem/<int:pk>/', blogItem, name='blogItem'),
    path('Quote/', freeview, name='freeQuote'),
    path('Management System/', managementSystem, name='managementSystem'),
    path('Mobile Services/', mobileService, name='mobileServices'),
    path('ProjectItem/<int:pk>/', projectItem, name='projectItem'),
    path('UI UX Design/', uiUxDesign, name='uiUxDesign'),
    path('Web Design And Development/', webDesignAndDevelopment, name='webDesignAndDevelopment'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)