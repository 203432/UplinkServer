from django.urls import re_path


from Post.views import PostList, PostListByOwner



urlpatterns = [
    re_path(r'$',PostList.as_view()),
    re_path(r'by_user/(?P<user>\d+)$', PostListByOwner.as_view()),
]