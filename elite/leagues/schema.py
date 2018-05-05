import graphene

from graphene_django.types import DjangoObjectType

from elite.leagues.models import User, Squad, League

class UserType(DjangoObjectType):

    class Meta:

        model = User

class CreateUser(graphene.Mutation):
    id = graphene.Int()
    first_name = graphene.String()
    last_name = graphene.String()
    username = graphene.String()
    email = graphene.String()

    class Argument:
        first_name = graphene.String()
        last_name = graphene.String()
        username = graphene.String()
        email = graphene.String()

    def mutate(self, info, first_name, last_name, username, email):
        user = User(first_name=first_name, last_name=last_name, username=username, email=email)
        user.save()

        return CreateUser(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            email=user.email
        )



class SquadType(DjangoObjectType):

    class Meta:

        model = Squad

class CreateSquad(graphene.Mutation):
    id = graphene.Int()
    squad_name = graphene.String()

    class Argument:
        squad_name = graphene.String()


    def mutate(self, info, squad_name):
        squad = Squad(squad_name=squad_name)
        squad.save()

        return CreateSquad(
            id=squad.id,
            squad_name=squad.squad_name
        )


class LeagueType(DjangoObjectType):

     class Meta:

         model = League


class CreateLeague(graphene.Mutation):
    id = graphene.Int()
    league_name = graphene.String()
    league_description = graphene.String()
    season_dates = graphene.String()

    class Argument:
        id = graphene.Int()
        league_name = graphene.String()
        league_description = graphene.String()
        season_dates = graphene.String()

    def mutate(self, info, league_name, league_description, season_dates):
        # league = League(league_name=league_name, league_description=league_description, season_dates=season_dates)
        # league.save()
        #
        # return league
        pass

        # CreateLeague(league_name=league.league_name, league_description=league.league_description, season_dates=league.season_dates)




class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int(),
                            first_name=graphene.String(), last_name=graphene.String(),
                            username=graphene.String(), email=graphene.String())

    all_squads = graphene.List(SquadType)
    squad = graphene.Field(SquadType, id=graphene.Int(), squad_name=graphene.Int())

    all_leagues = graphene.List(LeagueType)
    league = graphene.Field(LeagueType, league_name=graphene.String(),
                            league_description=graphene.String(), season_dates=graphene.String())



    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        first_name = kwargs.get('first_name')
        last_name = kwargs.get('last_name')
        username = kwargs.get('username')
        email = kwargs.get('email')

        if id is not None:
            return User.objects.get(pk=id)

        if first_name is not None:
            return User.objects.get(first_name=first_name)

        if last_name is not None:
            return User.objects.get(last_name=last_name)

        if username is not None:
            return User.objects.get(username=username)

        if email is not None:
            return User.objects.get(email=email)

        return None



    def resolve_all_squads(self, info, **kwargs):
        return Squad.objects.all()

    def resolve_squad(self, info, **kwargs):
        id = kwargs.get('id')
        squad_name = kwargs.get('squad_name')

        if id is not None:
            return Squad.objects.get(pk=id)

        if squad_name is not None:
            return Squad.objects.get(squad_name=squad_name)

        return None

    def resolve_all_leagues(self, info, **kwargs):
        return League.objects.all()

    def resolve_league(self, info, **kwargs):
        id = kwargs.get('id')
        league_name = kwargs.get('league_name')
        league_description = kwargs.get('league_description')

        if id is not None:
            return League.objects.get(pk=id)

        if league_name is not None:
            return League.objects.get(league_name=league_name)

        if league_descriptions is not None:
            return League.objects.get(league_description=league_description)


        return None


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_squad = CreateSquad.Field()
    create_league = CreateLeague.Field()
