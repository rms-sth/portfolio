from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def blogs(request):
	return render(request, 'blogs.html')


def blog_detail(request):
	return render(request, 'blog_detail.html')

def contact(request):
	return render(request, 'contactme.html')

def portfolio(request):
	return render(request, 'portfolio.html')

def services(request):
	return render(request, 'services.html')

def about(request):
	return render(request, 'aboutme.html')