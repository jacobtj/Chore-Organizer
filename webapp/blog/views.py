from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import (
	ListView, 
	CreateView,
	DetailView, 
	DeleteView
	)
from rest_framework import viewsets
from .serializers import ModelSerializer
from .models import Post


# Create your views here.
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'points']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostView(viewsets.ModelViewSet):
	serializer_class = ModelSerializer
	queryset = Post.objects.all()

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

