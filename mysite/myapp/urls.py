from django.urls import path
from .views import articles, articles_id


urlpatterns = [
    path('', articles),
    path('<int:article_id>/', articles_id, name='articles'),
    path('<int:article_id>/<slug:name>/', articles_id, name='article_name'),
]