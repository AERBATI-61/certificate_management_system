from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('index/', indexView, name="index"),
    path('activities/', activityView, name="activity"),

    path('participants/', participantsView, name="participants"),
    path('participants/<int:id>', participantView, name="participant"),


    path('hosts/', hostView, name="hosts"),
    path('organizations/', organizationView, name="organizations"),
    path('activity/<slug:slug>', activityDetail, name="activitydetail"),
    path('activities/<slug:slug>', activity_view_with_category, name='activity_view_with_category'),
    path('basarili/', Contactview.as_view(), name="contactview"),

    path('certificate/<int:id>', certificateView, name="certificate"),
    path('certificates', certificatesView, name="certificates"),
    path('certificalar', certificalar, name="certificalar"),
    path('pdf/<pk>/', render_pdf_view, name="pdf"),
]