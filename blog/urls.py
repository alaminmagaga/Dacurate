from django.urls import path
from .views import AddPostView1, HomeView,ArticleDetailView,AddPostView,AddPostView1,UpdatePostView,DeletePostView,LikeView,UserEditView,PasswordsChangeView,ShowProfilePageView,EditProfilePageView,CreateProfilePageView,AddCommentView,UserRegisterView,FollowerView,CategoryView,CategoryListView,UpdateQuestionView
from . import views



urlpatterns = [
   
    path('',HomeView.as_view(), name='home'),
    path('register/',UserRegisterView.as_view(),name='register'),
    path('article/<int:pk>', ArticleDetailView.as_view() , name='article-detail'),
    path('add_post/',AddPostView.as_view(),name='add-post'),
    path('add_post1/',AddPostView1.as_view(),name='add-post1'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name='update-post'),
     path('article/update/<int:pk>',UpdateQuestionView.as_view(),name='update-question'),
    path('article/<int:pk>/remove',DeletePostView.as_view(),name='delete-post'),
    path('like/<int:pk>',LikeView,name='like_post'),
    path('follow/<int:pk>',FollowerView,name='follow'),
    path('edit_profile/',UserEditView.as_view(),name='edit-profile'),
    path('password/', PasswordsChangeView.as_view(template_name='change-password.html')),
    path('password_success', views.password_success, name='password-success'),
    path('<int:pk>/profile/',ShowProfilePageView.as_view(), name='show-profile'),
    path('<int:pk>/edit_profile/',EditProfilePageView.as_view(), name='edit-profile-page'),
    path('create_profile_page/',CreateProfilePageView.as_view(), name='create-profile-page'),
    path('article/<int:pk>/comment/',AddCommentView.as_view(),name='comment'),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('category-list',CategoryListView,name='category-list'),
    
]
