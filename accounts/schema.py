from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Profile
import graphene
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    profile = graphene.Field(ProfileType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=False)
        name = graphene.String(required=False)

    def mutate(self, info, username, password, email, name):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        profile = Profile.objects.create(
            user=User.objects.get(username=user),
            name=name
        )
        profile.save()

        return CreateUser(user=user, profile=profile)


class LoginUser(graphene.Mutation):
    profile = graphene.Field(ProfileType)

    class Argument:
        username = graphene.String(required=True)

    def mutate(self, username):
        profile = Profile.objects.get(user__username=username)
        return LoginUser(profile=profile)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    login_user = LoginUser.Field()


class Query(graphene.ObjectType):
    profile = graphene.Field(ProfileType, username=graphene.String())

    def resolve_profile(self, info, **kwargs):
        username = kwargs.get("username")

        if username is not None:
            return Profile.objects.get(user__username=username)

        return None