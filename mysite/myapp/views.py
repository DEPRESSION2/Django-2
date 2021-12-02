from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def main(request):
    return HttpResponse("Main page")


def articles(request):
    return HttpResponse("Main page of articles")


def articles_id(request, article_id, name=''):
    return render(request, "articles.html", {"idx": article_id, "name": name})
