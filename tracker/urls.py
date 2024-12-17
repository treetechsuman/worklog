from django.urls import path, include
from .views import ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, TimeEntryCreateView, TimeEntryListView, TimeEntryUpdateView, TimeEntryDeleteView
from . import views

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    
    path('', views.index, name='index'),
    
]

urlpatterns += [
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/add/', ProjectCreateView.as_view(), name='project-add'),
    path('projects/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
]

urlpatterns += [
    path('time_entries/', TimeEntryListView.as_view(), name='time-entries'),
    path('time_entries/add/', TimeEntryCreateView.as_view(), name='time-entry-add'),
    path('time_entries/<int:pk>/edit/', TimeEntryUpdateView.as_view(), name='time-entry-update'),
    path('time_entries/<int:pk>/delete/', TimeEntryDeleteView.as_view(), name='time-entry-delete'),
]



from .views import ProjectListCreateView, ProjectDetailView, TimeEntryListCreateView, TimeEntryDetailView

urlpatterns += [
    path('api/projects/', ProjectListCreateView.as_view(), name='project-list'),
    path('api/projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('api/time-entries/', TimeEntryListCreateView.as_view(), name='timeentry-list'),
    path('api/time-entries/<int:pk>/', TimeEntryDetailView.as_view(), name='timeentry-detail'),
]
urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]