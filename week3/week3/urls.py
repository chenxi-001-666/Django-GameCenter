"""
URL configuration for week3 project.
"""
from django.contrib import admin
from django.urls import path, include  # 必须导入 include
from django.contrib.auth import views as auth_views
from games import views  # 统一使用 views 别名
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # 用户认证路由
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='game_list'), name='logout'),
    path('register/', views.register, name='register'), # 确保 views.py 中有名为 register 的函数
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),

    # 游戏业务路由
    path('', views.GameListView.as_view(), name='game_list'), # 首页直接展示游戏列表
    path('games/', views.GameListView.as_view(), name='game_list_alt'), # 备用路径
    path('reviews/', views.AllReviewListView.as_view(), name='all_reviews'),

    # 动态路由：查看特定游戏详情及评论
    path('games/<slug:slug>/reviews/', views.GameReviewListView.as_view(), name='game_specific_reviews'),

    # 提交评论接口 (新增)
    path('games/<slug:slug>/add_review/', views.add_review, name='add_review'),

]

# 仅在开发模式下通过 Django 提供媒体文件（图片）访问
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)