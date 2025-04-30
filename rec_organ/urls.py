from django.urls import path
from . import views
from movieapi.views import studentAPIView,studentdetail
from blog.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

urlpatterns = [
    path('abc/', views.home, name='home'), 
    path('User_login/',views.User_login,name='User_login'),
    
    path('Admin_login/',views.Admin_login,name='Admin_login'), 
    path('Register/',views.Register,name='Register'), 
    
    path('logout/',views.logout,name='logout'),
    path('ViewUsers/',views.ViewUsers,name='ViewUsers'),
    path('AcceptStylish/',views.AcceptStylish,name='AcceptStylish'),
    path('AcceptStylishs/',views.AcceptStylishs,name='AcceptStylishs'),
    
    path('updateStylish<int:id>/',views.updorg,name='updateStylish'),
    
    path('ViewSty/',views.ViewSty,name='ViewSty'),
    path('deluser/<int:id>', views.deluser, name='deluser'),
    path('updorg/<int:id>', views.updorg, name='updorg'),
    path('ViewStylish/',views.ViewStylish,name='ViewStylish'),
    path('AcceptRequest/<int:id>',views.AcceptRequest,name='AcceptRequest'),
    path('ViewStylis/',views.ViewStylis,name='ViewStylis'),
    path('accept/<int:id>', views.accept, name='accept'),
    path('View/',views.View,name='View'),
    path('reject/<int:id>', views.reject, name='reject'),
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('media/Files/<int:pk>',PostDeleteView.as_view(),name='post-delete' ),
   
    path('about/', views.about, name='blog-about'),
    path('see_image/<int:id>', views.see_image, name='see_image'),
    path('searchs/',views.searchs,name='searchs' ),


    
    
   
   
    path('admin_CP/',views.admin_CP,name='admin_CP'),
   
 
    
    

    
   
   

   
 
   
 

  
   
    
    
   





    
    path('adminreg/',views.adminreg,name='adminreg'),
   
   
    ]

