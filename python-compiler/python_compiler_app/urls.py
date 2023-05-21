from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from python_compiler_app.views import *

urlpatterns = [
    path('',IndexView.as_view(),name='index')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
