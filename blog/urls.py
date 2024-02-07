from django.urls import path

from blog.views import HomePageView, AboutView, NewPostView, UserPostView, PostDetailView, home_page, post_detail, \
    user_profile, logout_view, UserLogoutView, UserProfileView

app_name = 'blog'
urlpatterns = [
    path('', HomePageView.as_view(), name="home-page"),
    # path('', home_page, name="home-page"),
    # path('logout/', logout_view, name="logout"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    path('about/', AboutView.as_view(), name="about"),
    path('new-post/', NewPostView.as_view(), name="new-post"),
    path('user-post/<str:username>', UserPostView.as_view(), name="user-profile"),
    # path('post-detail/<int:pk>', post_detail, name="post-detail"),
    path('post-detail/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    # path('user-post/<str:username>', user_profile, name="user-profile")

]
