from django.conf.urls import url
from drones import views

urlpatterns = [
    url(r'^drone-categories/$',views.DroneCategoryList.as_view(),name=views.DroneCategoryList.name),
    url(r'^drone-categories/(?P<pk>[0-9]+)$',views.DroneCategoryDetail.as_view(),name=views.DroneCategoryDetail.name),
    url(r'^drones/$',views.DroneList.as_view(),name=views.DroneList.name),
    url(r'^drones/(?P<pk>[0-9]+)$',views.DroneDetail.as_view(),name=views.DroneDetail.name),
    url(r'^pilots/$',views.PilotList.as_view(),name=views.PilotList.name),
    url(r'^pilots/(?P<pk>[0-9]+)$',views.PilotDetail.as_view(),name=views.PilotDetail.name),
    url(r'^competitions/$',views.CompetitionList.as_view(),name=views.CompetitionList.name),
    url(r'^competitions/(?P<pk>[0-9]+)$',views.CompetitionDetail.as_view(),name=views.CompetitionDetail.name),
    url(r'^$',views.ApiRoot.as_view(),name=views.ApiRoot.name),
]

#   /drone-categories/          DroneCategoryList       GET, POST, and OPTIONS
#   /drone-categories/{id}      DroneCategoryDetail     GET,PUT,PATCH,DELETE,and OPTIONS
#   /drones/                    DroneList               GET,POST, and OPTIONS
#   /drones/{id}                DroneDetail             GET,PUT,PATCH,DELETE,and OPTIONS
#   /pilots/                    PilotList               GET, POST and OPTIONS
#   /pilot/{id}                 PilotDetail             GET, PUT, PATCH, DELETE and OPTIONS
#   /competitions/              CompetitionList         GET, POST and OPTIONS
#   /competition/{id}           CompetitionDetail       GET, PUT, PATCH, DELETE and OPTIONS























