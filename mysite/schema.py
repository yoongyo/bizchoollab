from peed.schema import Query as PeedQuery
import graphene


class Query(PeedQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
