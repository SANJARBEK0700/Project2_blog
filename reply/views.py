from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment, Reply,Chat


class ReplyComment(LoginRequiredMixin, View):

    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        return render(request, 'reply_page.html', {'comment': comment})

    def post(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        reply_text = request.POST.get('reply_text')

        if comment.user == request.user:
            messages.error(request, "O'z sharhingizga javob yozishingiz mumkin emas!")
            return redirect('post-detail', slug=comment.post.slug)

        if reply_text:
            Reply.objects.create(
                comment=comment,
                user=request.user,
                text=reply_text
            )
            messages.success(request, "Javobingiz muvaffaqiyatli qo'shildi!")
            return redirect('post-detail', slug=comment.post.slug)

        messages.warning(request, "Javob matnini kiriting!")
        return redirect('reply_comment_page', comment_id=comment_id)



class CommentUpdate(LoginRequiredMixin,View):
    def get(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id, user=request.user)
        return render(request, 'comment_update.html', {'comment': comment})
    def post(self,request, comment_id):
        comment=get_object_or_404(Comment,id=comment_id,user=request.user)
        text=request.POST.get('text')
        if text:
            comment.text=text
            comment.save()
            messages.success(request, "Sharh yangilandi")
        return redirect('post-detail',slug=comment.post.slug)



class CommentDelete(LoginRequiredMixin,View):
    def post(self,request,comment_id):
        comment = get_object_or_404(Comment,id=comment_id,user=request.user)
        comment.delete()
        messages.success(request, "Sharh o‘chirildi")
        return redirect('post-detail', slug=comment.post.slug)



class ChatView(LoginRequiredMixin,View):
    def get(self,request):
        chats=Chat.objects.filter(participants=request.user).order_by('-created_at')

        context={
            'chats':chats
        }

        return render(request,'chat_list.html',context)

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from post.models import Post
from .models import Comment


@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        text = request.POST.get("text")

        if text:
            Comment.objects.create(
                user=request.user,
                post=post,
                text=text
            )

    return redirect('post-detail', slug=slug)




