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

    startup = graphene.Field(StartupType, id=graphene.Int())

    all_startupCategory = graphene.List(StartupCategoryType)

    def resolve_all_startup(self, context, **kwargs):
        return Startup.objects.all()

    def resolve_startup(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Startup.objects.get(pk=id)

        return None

    def resolve_all_startupCategory(self, context, **kwargs):
        return StartupCategory.objects.all()

