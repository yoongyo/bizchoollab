import graphene
from graphene_django.types import DjangoObjectType
from .models import Peed, Category, Tag


class PeedType(DjangoObjectType):
    class Meta:
        model = Peed


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class Query(graphene.AbstractType):
    all_peed = graphene.List(PeedType)

    all_category = graphene.List(CategoryType)

    all_tag = graphene.List(TagType)

    peed = graphene.Field(PeedType, id=graphene.Int())

    def resolve_all_peed(self, context, **kwargs):
        return Peed.objects.all()

    def resolve_peed(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Peed.objects.get(pk=id)

        return None

    def resolve_all_portfolioCategory(self, context, **kwargs):
        return Category.objects.all()

    def resolve_all_tag(self, context, **kwargs):
        return Tag.objects.all()
