import graphene

import elite.leagues.schema

class Query(elite.leagues.schema.Query, graphene.ObjectType):
    pass

class Mutation(elite.leagues.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
