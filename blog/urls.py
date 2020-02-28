from django.conf.urls import url,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts',views.postview)

urlpatterns = [
    url(r'^base',views.base.as_view(),name='base'),
    url(r'^$',views.postlist.as_view(),name='postlist'),
    url(r'^register/$',views.registration,name='register'),
    url(r'^login/$',views.user_login,name='user_login'),
    url(r'^logout/$',views.user_logout,name='user_logout'),
    url(r'^drafts/$',views.draftlist.as_view(),name='draftlist'),
    url(r'^new/$',views.postcreate.as_view(),name='newpost'),
    url(r'^post/(?P<pk>\d+)/$',views.postdetail.as_view(),name='postdetail'),
    url(r'^post/(?P<pk>\d+)/update/$',views.postupdate.as_view(),name='updatepost'),
    url(r'^post/(?P<pk>\d+)/delete/$',views.postdelete.as_view(),name='deletepost'),
    url(r'^post/(?P<pk>\d+)/publish/$',views.publishpost,name='publishpost'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment, name='addcomment'),
    url(r'^comment/(?P<pk>\d+)/approve/$',views.approve_comment,name='approvecomment'),
    url(r'^comment/(?P<pk>\d+)/remove/$',views.delete_comment,name='removecomment'),
    url(r'api/$',include(router.urls))

]