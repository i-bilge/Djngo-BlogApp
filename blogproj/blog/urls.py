from django.urls import path
from .views import HomePage, PostList, PostDetail, PostCreate, PostUpdate, PostDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('posts/', PostList.as_view(), name='posts'),
    path('post-create/', PostCreate.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetail.as_view(), name= 'posts-detail'),
    path('post-update/<int:pk>/', PostUpdate.as_view(), name= 'posts-update'),
    path('post-delete/<int:pk>/', PostDelete.as_view(), name= 'posts-delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
]