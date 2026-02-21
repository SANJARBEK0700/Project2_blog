from django.urls import path
from .views import add_comment, ReplyComment, CommentUpdate, CommentDelete
app_name = 'reply'
urlpatterns = [
    path('comment/add/<slug:slug>/', add_comment, name='add-comment'),
    path('reply/<int:comment_id>/', ReplyComment.as_view(), name='reply_comment_page'),
    path('comment/update/<int:comment_id>/', CommentUpdate.as_view(), name='comment_update'),
    path('comment/delete/<int:comment_id>/', CommentDelete.as_view(), name='comment_delete'),
]