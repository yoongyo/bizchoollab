import graphene
from graphene_django.types import DjangoObjectType
from .models import TechCategory, Technology


class TechnologyType(DjangoObjectType):
    class Meta:
        model = Technology


class TechCategoryType(DjangoObjectType):
    class Meta:
        model = TechCategory


class Query(graphene.AbstractType):
    all_tech = graphene.List(TechnologyType)

    tech = graphene.Field(TechnologyType, id=graphene.Int())

    all_techCategory = graphene.List(TechCategoryType)

    def resolve_all_tech(self, context, **kwargs):
        return Technology.objects.all()

    def resolve_tech(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Technology.objects.get(pk=id)

        return None

    def resolve_all_techCategory(self, context, **kwargs):
        return TechCategory.objects.all()

