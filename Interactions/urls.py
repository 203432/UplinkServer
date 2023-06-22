import re
from xml.dom.minidom import Document
from django.urls import re_path, path
from django.conf.urls.static import static
from django.conf import settings
from Uplink import settings

from Interactions.views import CommentsList, CommentListByPost, CommentDetail


urlpatterns = [
    re_path(r'$', CommentsList.as_view()),
    re_path(r'(?P<pk>\d+)$', CommentDetail.as_view()),
    re_path(r'by_post/(?P<post>\d+)$',CommentListByPost.as_view())
]