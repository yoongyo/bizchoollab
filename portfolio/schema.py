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

    all_all_portfolioCategory = graphene.List(PortfolioCategoryType)

    def resolve_all_portfolio(self, context, **kwargs):
        return Portfolio.objects.all()

    def resolve_all_portfolioCategory(self, context, **kwargs):
        return PortfolioCategory.objects.all()
