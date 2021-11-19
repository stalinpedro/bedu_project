import graphene
from graphene_django import DjangoObjectType

from .models import *


class UserType(DjangoObjectType):
    class Meta:
        model = User


class ZoneType(DjangoObjectType):
    class Meta:
        model = Zone


class TourType(DjangoObjectType):
    class Meta:
        model = Tour


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_zones = graphene.List(ZoneType)
    all_tours = graphene.List(TourType)

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_all_zones(self, info, **kwargs):
        return Zone.objects.all()

    def resolve_all_tours(self, info, **kwargs):
        return Tour.objects.all()


class CreateZone(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()
        latitud = graphene.Decimal()
        longitude = graphene.Decimal()

    zone = graphene.Field(ZoneType)

    def mutate(self, info, name, description=None, latitud=None, longitude=None):
        new_zone = Zone(name=name, description=description, latitud=latitud, longitude=longitude)
        new_zone.save()

        return CreateZone(zone=new_zone)


class DeleteZone(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        status = False
        try:
            zone = Zone.objects.get(pk=id)
            zone.delete()
            status = True
        except Zone.DoesNotExist:
            status = False

        return DeleteZone(ok=status)


class Mutation(graphene.ObjectType):
    create_zone = CreateZone.Field()
    delete_zone = DeleteZone.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
