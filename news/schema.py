import graphene
from graphene_django.types import DjangoObjectType
from .models import News, NewsCategory


class NewsType(DjangoObjectType):
    class Meta:
        model = News


class NewsCategoryType(DjangoObjectType):
    class Meta:
        model = NewsCategory


class Query(graphene.AbstractType):
    all_news = graphene.List(NewsType)

    all_newsCategory = graphene.List(NewsCategoryType)

    def resolve_all_news(self, context, **kwargs):
        return News.objects.all()

    def resolve_all_newsCategory(self, context, **kwargs):
        return NewsCategory.objects.all()

