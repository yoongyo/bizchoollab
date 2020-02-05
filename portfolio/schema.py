import graphene
from graphene_django.types import DjangoObjectType
from .models import Portfolio, PortfolioCategory


class PortfolioType(DjangoObjectType):
    class Meta:
        model = Portfolio


class PortfolioCategoryType(DjangoObjectType):
    class Meta:
        model = PortfolioCategory


class Query(graphene.AbstractType):
    all_portfolio = graphene.List(PortfolioType)

    portfolio = graphene.Field(PortfolioType, id=graphene.Int())

    all_all_portfolioCategory = graphene.List(PortfolioCategoryType)

    def resolve_all_portfolio(self, context, **kwargs):
        return Portfolio.objects.all()

    def resolve_portfolio(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Portfolio.objects.get(pk=id)

        return None

    def resolve_all_portfolioCategory(self, context, **kwargs):
        return PortfolioCategory.objects.all()
