from django.forms import ModelForm, Textarea, TextInput
from .models import NewsPost, Comment

class PhotoPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス

        Attributes:
            model: モデルのクラス
            fields: フォームで使用するモデルのフィールドを指定
        '''
        model = NewsPost
        fields = ['category', 'title', 'comment', 'image1', 'image2']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
        widgets = {
            'text': Textarea(attrs={'class': 'form-control'}),
            'author': TextInput(attrs={'class': 'form-control'}),
        }