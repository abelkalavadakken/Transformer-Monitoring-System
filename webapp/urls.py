from django.urls import path
from webapp.views import MonitorView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MonitorView.as_view()),
    path('results.html', MonitorView.as_view(), name='results')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
