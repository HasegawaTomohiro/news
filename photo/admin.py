from django.contrib import admin
# CustomUserをインポート
from .models import Category, NewsPost, Comment

# 投稿詳細管理画面にコメントも追加
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ('author', 'text', 'approved_comment')
    
class CategoryAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス

    '''
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

class PhotoPostAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス

    '''
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title', 'get_comment_count')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

    inlines = (CommentInline,)

    # コメント数を測定して、記事一覧画面に反映
    def get_comment_count(self, obj):
        return obj.comments.count()

    get_comment_count.short_description = 'Comment Count'
# Django管理サイトにCategory,CategoryAdminを登録する
admin.site.register(Category, CategoryAdmin)

# Django管理サイトにPhotoPost、PhotoPostAdminを登録する
admin.site.register(NewsPost, PhotoPostAdmin)