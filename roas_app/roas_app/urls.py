"""
roas_app URL Configuration.
"""
from ad_campaign import views
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"campaigns", views.CampaignViewSet)
router.register(r"adgroups", views.AdGroupViewSet)
router.register(r"searchterms", views.SearchTermViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path(
        "api/structure-value/<str:structure_value>/",
        views.CampaignDetailView.as_view(),
        name="structure-value-list",
    ),
    path(
        "api/alias/<str:alias>/", views.AdGroupDetailView.as_view(), name="alias-list"
    ),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
