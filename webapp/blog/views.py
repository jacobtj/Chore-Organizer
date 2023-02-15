from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author': 'a',
		'title': 'b',
		'content': 'c',
		'date_posted': 'd'
	},
	{
		'author': 'e',
		'title': 'f',
		'content': 'g',
		'date_posted': 'h'
	}
]

# Create your views here.
def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})