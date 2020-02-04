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

    news = graphene.Field(NewsType, id=graphene.Int())

    all_newsCategory = graphene.List(NewsCategoryType)

    def resolve_all_news(self, context, **kwargs):
        return News.objects.all()

    def resolve_news(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return News.objects.get(pk=id)

        return None

    def resolve_all_newsCategory(self, context, **kwargs):
        return NewsCategory.objects.all()

