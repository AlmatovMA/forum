from xml.etree.ElementInclude import include
from django.urls import path, include
from service import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    #path('', include('django.contrib.auth.urls')),
    path('register', views.RegisterForm.as_view(), name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = "login.html"), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = "logout.html"), name = 'logout'),
    path("", views.PostView.as_view(), name='index'),
    path("create_post", views.CreatePost.as_view(), name='create_post'),
    path("update_post/<int:pk>/", views.updatePost.as_view(), name='update_post'),
    path("delate_post/<int:pk>/", views.DeletePost.as_view(), name='delete_post'),
    path("post/<int:pk>/", views.detale_post.as_view(), name='post_detail'),
    path("post/<int:pk>/", views.AddComment.as_view() , name='add_comment'),
    path("abaut", views.abaut , name='abaut'),
    
]