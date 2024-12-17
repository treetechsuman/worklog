from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Project, TimeEntry
from .forms import ProjectForm, TimeEntryForm

from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer, TimeEntrySerializer
from rest_framework import generics

from rest_framework.permissions import AllowAny


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_form.html'
    success_url = reverse_lazy('projects')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_form.html'
    success_url = reverse_lazy('projects')

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = reverse_lazy('projects')

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)
    

class TimeEntryListView(LoginRequiredMixin, ListView):
    model = TimeEntry
    template_name = 'time_entries.html'
    context_object_name = 'time_entries'

    def get_queryset(self):
        return TimeEntry.objects.filter(user=self.request.user)

class TimeEntryCreateView(LoginRequiredMixin, CreateView):
    model = TimeEntry
    form_class = TimeEntryForm
    template_name = 'time_entry_form.html'
    success_url = reverse_lazy('time-entries')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TimeEntryUpdateView(LoginRequiredMixin, UpdateView):
    model = TimeEntry
    form_class = TimeEntryForm
    template_name = 'time_entry_form.html'
    success_url = reverse_lazy('time-entries')

    def get_queryset(self):
        return TimeEntry.objects.filter(user=self.request.user)

class TimeEntryDeleteView(LoginRequiredMixin, DeleteView):
    model = TimeEntry
    template_name = 'time_entry_confirm_delete.html'
    success_url = reverse_lazy('time-entries')

    def get_queryset(self):
        return TimeEntry.objects.filter(user=self.request.user)
    

#for api
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]  # Disable authentication for this view

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]  # Disable authentication for this view

class TimeEntryListCreateView(generics.ListCreateAPIView):
    queryset = TimeEntry.objects.all()
    serializer_class = TimeEntrySerializer
    permission_classes = [AllowAny]  # Disable authentication for this view

class TimeEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeEntry.objects.all()
    serializer_class = TimeEntrySerializer
    permission_classes = [AllowAny]  # Disable authentication for this view
    
def index(request):
    # Ensure the user is logged in
    if not request.user.is_authenticated:
        return render(request, 'error.html', {'message': 'You need to log in to view your projects.'})

    # Fetch projects for the logged-in user
    user_projects = Project.objects.filter(user=request.user)

    # Pass the projects to the template
    context = {
        'projects': user_projects,
        'username': request.user.username,  # Optionally pass the username
        'userid': request.user.pk,  # Optionally pass the username
    }
    return render(request, 'index.html', context)
    #return render(request, 'index.html')







