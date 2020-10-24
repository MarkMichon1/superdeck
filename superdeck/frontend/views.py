from django.shortcuts import redirect, render
from django.views.generic import ListView

from frontend.models import Article


def home(request):
    return render(request, 'frontend/home.html')


def about(request):
    return render(request, 'frontend/about.html')


def articles(request):
    return render(request, 'frontend/articles.html')


class ArticleListView(ListView):
    model = Article
    template_name = 'frontend/articles.html'
    context_object_name = 'articles'
    extra_context = {
        'title': 'Articles'
    }
    paginate_by = 10


def article_detail(request, url_slug):
    return render(request, 'frontend/article_detail.html')


def contact(request):
    return render(request, 'frontend/contact.html')


def services(request):
    return render(request, 'frontend/services.html')


def error_404(request, exception):
    return redirect('frontend-home')


# to do:  testimonials, previous work
