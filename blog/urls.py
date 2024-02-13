from django.urls import path

from blog.forms import PostUpdateForm
from blog.views import HomePageView, AboutView, NewPostView, UserPostView, PostDetailView, home_page, post_detail, \
    user_profile, logout_view, login_view, register_view, post_create, post_update, post_delete, UserLoginView, \
    UserRegisterView, UserLogoutView, UpdatePostView, PostDeleteView

app_name = 'blog'
urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('about/', AboutView.as_view(), name='about-page'),
    path('login/', UserLoginView.as_view(), name='login-page'),
    path('register/', UserRegisterView.as_view(), name='register-page'),
    path('logout/', UserLogoutView.as_view(), name='logout-page'),
    path('new-post/', NewPostView.as_view(), name='new-post'),
    path('post-detail/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post-update/<int:pk>', UpdatePostView.as_view(), name='post-update'),
    path('post-delete/<int:pk>', PostDeleteView.as_view(), name='post-delete'),
    path('user-post/<str:username>', UserPostView.as_view(), name='user-profile')
]
