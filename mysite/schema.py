from peed.schema import Query as PeedQuery
from peed.schema import Mutation as PeedMutation
import graphene
import graphql_jwt


class Query(PeedQuery, graphene.ObjectType):
    pass


class Mutation(PeedMutation, graphene.ObjectType,):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query)
