from django.contrib import admin
from .models import Game, Review

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'developer', 'platform', 'slug') # 确保包含 slug
    prepopulated_fields = {'slug': ('title',)} # 让后台自动根据标题生成 slug

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # 将 'user_name' 改为 'user'
    list_display = ('game', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'game')