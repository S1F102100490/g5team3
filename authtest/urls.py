from django.urls import path
from . import views

urlpatterns = [
	path('<int:article_id>/', views.detail, name='detail'),
    path('', views.home, name='home'),
    path('priv', views.private_page, name='priv'),
    path('pub', views.public_page, name='pub'),
## 以下monbran
	path('<int:article_id>/', views.detail, name='detail'),
	path('<int:article_id>/delete', views.delete, name='delete'),
	path('<int:article_id>/update', views.update, name='update'),
	path('<int:article_id>/like', views.like, name='like'),
    path('redirect', views.redirect_test, name='redirect_test'),
    
]