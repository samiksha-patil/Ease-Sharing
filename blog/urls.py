from django.urls import path
from . import views
from django.conf.urls import url
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView,UserAnswerListView
urlpatterns = [   
   path('',PostListView.as_view(),name='blog-home'),
   path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
   path('post/new/',PostCreateView.as_view(),name='post-create'),
   path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
   path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
   path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
  # path('post/<int:pk>/answer/',AnswerCreateView.as_view(), name='add_answer_to_post'),
   path('post/<int:pk>/answer/', views.add_answer_to_post, name='add_answer_to_post'),
   path('answer/<str:username>',UserAnswerListView.as_view(),name='user-answer'),
   path('prof/<int:pk>',views.prof,name='user-prof'),
]





