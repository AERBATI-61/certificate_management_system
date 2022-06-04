from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', indexView, name="index"),
    path('activities/', activityView, name="activity"),

    path('participants/', participantsView, name="participants"),
    path('participants/<int:id>', participantView, name="participant"),


    path('hosts/', hostView, name="hosts"),
    path('organizations/', organizationView, name="organizations"),
    path('activity/<slug:slug>', activityDetail, name="activitydetail"),
    path('activities/<slug:slug>', activity_view_with_category, name='activity_view_with_category'),
    path('contact/', Contactview.as_view(), name="contactview"),
    path('page_404/', decoratorView, name="decorator"),

    path('certificate/<int:id>', certificateView, name="certificate"),
    path('certificates', certificatesView, name="certificates"),
    path('certificalar', certificalar, name="certificalar"),

    path('pdf/<pk>/', render_pdf_view, name="pdf"),
    path('qr/<pk>/', qr_pdf_view, name="qr_pdf"),
    path('barcode/<pk>/', barcode_pdf_view, name="barcode_pdf_view"),
    path('googleForm/<pk>/', googleForm_pdf_view, name="googleForm_pdf_view"),
    path('qr/', qr_code_view, name="qr"),
    path('send_email/', send_email, name="send_email"),
]