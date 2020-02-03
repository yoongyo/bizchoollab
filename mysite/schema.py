from news.schema import Query as FestivalQuery
from portfolio.schema import Query as PortfolioQuery
from startup.schema import Query as startupQuery
from tech.schema import Query as techQuery

import graphene


class Query(FestivalQuery, PortfolioQuery, startupQuery, techQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
