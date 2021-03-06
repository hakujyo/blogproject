import markdown
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView


from .models import Post, Category, Tag
from users.models import User
from comments.forms import CommentForm


#视图类
class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post_list_a'
    paginate_by = 5

#对应的视图函数：
# def index(request):
#     post_list = Post.objects.all()
#     return render(request, 'index.html', context={'post_list': post_list})


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        post = super(PostDetailView, self).get_object(queryset=None)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context

# def detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.increase_views()
#     post.body = markdown.markdown(post.body,
#                                   extensions=[
#                                      'markdown.extensions.extra',
#                                      'markdown.extensions.codehilite',
#                                      'markdown.extensions.toc',
#                                   ])
#     form = CommentForm()
#     # 获取这篇 post 下的全部评论
#     comment_list = post.comment_set.all()
#     # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
#     context = {'post': post,
#                'form': form,
#                'comment_list': comment_list,
#                }
#     return render(request, 'detail.html', context=context)


class ArchivesView(ListView):
    model = Post
    template_name = 'blog_filter.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        auth = self.kwargs.get('pk')
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year,
                                    created_time__month=month, author=auth
                                    )

# def archives(request, year, month):
#     post_list = Post.objects.filter(created_time__year=year,
#                                     created_time__month=month
#                                     )
#     return render(request, 'index.html', context={'post_list': post_list})


class CategoryView(ListView):
    model = Post
    template_name = 'blog_filter.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)

# def category(request, pk):
#     cate = get_object_or_404(Category, pk=pk)
#     post_list = Post.objects.filter(category=cate)
#     return render(request, 'index.html', context={'post_list': post_list})

# class AuthorView(ListView):
#     model = Post
#     template_name = 'index.html'
#     context_object_name = 'post_list'
#
#     def get_queryset(self):
#         auth = get_object_or_404(User, pk=self.kwargs.get('pk'))
#         return super(CategoryView, self).get_queryset().filter(author=auth)


def author(request, pk):
    auth = get_object_or_404(User, pk=pk)
    post_list = Post.objects.filter(author=auth)
    return render(request, 'user-blog.html', context={'post_list': post_list, 'author':auth})


class TagView(ListView):
    model = Post
    template_name = 'blog_filter.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)
