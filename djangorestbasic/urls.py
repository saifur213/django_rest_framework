"""
URL configuration for djangorestbasic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from djangoapi import views

#Model View Set
from rest_framework.routers import DefaultRouter
#Create router object
router = DefaultRouter()
#register
router.register('teacher-model-view-set',views.teacherModelViewSet, basename='teacher')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('teacherinfo/',views.teacher_infos),
    path('teacherinfo/<int:pk>',views.teacher_info),
    # path('teachercreate/<int:pk>',views.teacher_create,name='teachercreate'),
    path('teachercreate/',views.teacher_create,name='teachercreate'),
    path('teachercreateapi/',views.teacher_create_api,name='teachercreateapi'),
    path('teachercreateapi/<int:pk>',views.teacher_create_api,name='teachercreateapi'),
    path('teachercreateclassbasedapiview/',views.teacher_create_class_based_api_view.as_view(),name='teachercreateclassbasedapiview'),
    path('teachercreateclassbasedapiview/<int:pk>',views.teacher_create_class_based_api_view.as_view(),name='teachercreateclassbasedapiview'),
    #List model mixin
    path('teacherlistcreate/',views.teacherListCreate.as_view(),name='teacherlistcreate'),
    path('teacherListRetrieveUpdateDelete/<int:pk>',views.teacherListRetrieveUpdateDelete.as_view(),name='teacherListRetrieveUpdateDelete'),
    #List create api view
    path('teacherListCreateApiView/',views.teacherListCreateApiView.as_view(),name='teacherListCreateApiView'),
    path('teacherListApiViewRetrieveUpdateDelete/<int:pk>',views.teacherListApiViewRetrieveUpdateDelete.as_view(),name='teacherListApiViewRetrieveUpdateDelete'),
    #router
    path('',include(router.urls))
    
    
]
