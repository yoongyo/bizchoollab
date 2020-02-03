import graphene
from graphene_django.types import DjangoObjectType
from .models import StartupCategory, Startup


class StartupType(DjangoObjectType):
    class Meta:
        model = Startup


class StartupCategoryType(DjangoObjectType):
    class Meta:
        model = StartupCategory


class Query(graphene.AbstractType):
    all_startup = graphene.List(StartupType)

    all_all_startupCategory = graphene.List(StartupCategoryType)

    def resolve_all_startup(self, context, **kwargs):
        return Startup.objects.all()

    def resolve_all_startupCategory(self, context, **kwargs):
        return StartupCategory.objects.all()

