from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# from models import Tour, Zone
from library_api.models import Tour, Zone, User

from rest_framework import viewsets, serializers


@login_required()
def index(request):
    # Se obtiene la lista de todos los Tours y Zonas
    tours = Tour.objects.all()
    zonas = Zone.objects.all()

    es_editor = request.user.groups.filter(name="editores").exists()

    return render(request, "index.html", {"tours": tours, "zonas": zonas, "es_editor": es_editor})


@login_required()
def eliminar_tour(request, id_tour):
    tour = Tour.objects.get(pk=id_tour)
    tour.delete()

    return redirect("/")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'last_name', 'email', 'birthday', 'genre', 'key', 'type')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')

    serializer_class = UserSerializer


class TourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tour
        fields = ('id', 'nombre', 'zonaSalida', 'zonaLlegada')


class ZoneSerializer(serializers.HyperlinkedModelSerializer):
    tours_salida = TourSerializer(many=True, read_only=True)

    class Meta:
        model = Zone
        fields = ('id', 'name', 'description', 'tours_salida', 'tours_llegada')


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all().order_by('id')

    serializer_class = ZoneSerializer


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all().order_by('id')

    serializer_class = TourSerializer

# def login_user(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         next = request.GET.get("next", "/")
#
#         acceso = authenticate(username=username, password=password)
#
#         if acceso is not None:
#             login(request, acceso)
#             return redirect(next)
#         else:
#             msg = "Datos incorrectos"
#
#     else:
#         msg = ""
#
#     return render(request, "registration/login.html", {"msg": msg, })


# def logout_user(request):
#     logout(request)
#
#     return redirect('/login/')


# curl -d '{"name": "Pluto", "last_name": "Mac Perro", "email":"pluto@pato.org", "birthday":"2000-01-01", "genre": "H"}' -H 'Content-Type: application/json' http://localhost:8000/api/users/
