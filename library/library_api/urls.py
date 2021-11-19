from django.urls import path, include
from django.contrib.auth import views as auth_views
from graphene_django.views import GraphQLView
from rest_framework import routers

from . import views
from .schema import schema

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'zones', views.ZoneViewSet)
router.register(r'tours', views.TourViewSet)

urlpatterns = [
    path('', views.index, name="index"),
    # path('login/', views.login_user, name="login_user"),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login_user"),
    # path('logout/', views.logout_user, name="logout_user"),
    path('logout/', auth_views.LogoutView.as_view(next_page="/login"), name="logout_user"),
    path("tour/eliminar/<int:id_tour>/", views.eliminar_tour, name="eliminar_tour"),

    path("api/", include(router.urls)),
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),

    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema))
]
