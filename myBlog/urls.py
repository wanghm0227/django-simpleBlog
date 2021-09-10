from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(),
         name='article_detail'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('article/<int:pk>/edit/', views.UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove/',
         views.RemovePostView.as_view(), name='remove_post'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('category/<str:category>/',
         views.CategoryPostsView.as_view(), name='category_posts'),
    path('article/<int:post_id>/like/', views.like, name='like'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)