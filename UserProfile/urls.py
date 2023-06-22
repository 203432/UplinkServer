import re
from xml.dom.minidom import Document
from django.urls import re_path, path
from django.conf.urls.static import static
from django.conf import settings
from Uplink import settings

from UserProfile.views import TablaProfileList, TablaProfileDetail, ProfileUser, UserDetailAPIView


urlpatterns = [
    re_path(r'$', TablaProfileList.as_view()),
    path('user/<username>', UserDetailAPIView.as_view()),
    re_path(r'^(?P<pk>\d+)$', TablaProfileDetail.as_view()),
    re_path(r'^data/(?P<pk>\d+)/$',ProfileUser.as_view()),
]