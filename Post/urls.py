from django.urls import re_path,path


from Post.views import PostList, PostListByOwner, PostDetailAPIView, PostDetail, UpdateLikesAPIView



urlpatterns = [
    re_path(r'$',PostList.as_view()),
    re_path(r'(?P<pk>\d+)$', PostDetail.as_view()),
    re_path(r'by_user/(?P<user>\d+)$', PostListByOwner.as_view()),
    path('<int:pk>/update-likes/', UpdateLikesAPIView.as_view()),
    path('by_text/<text>', PostDetailAPIView.as_view()),
]