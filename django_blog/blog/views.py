from django.shortcuts import render, get_object_or_404
from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import *

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-id']
    ordering = ['-post_date']
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        categ_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["categ_menu"] = categ_menu
        return context
    
    '''
    def paging(request):
        posts = Post.objects.all()
        pag_obj = Paginator(posts, 3)
        pages = request.GET.get('page')
        try:
            pag_posts =pag_obj.page(pages)
        except PageNotAnInteger:
            pag_posts =pag_obj.page(1)
        except EmptyPage:
            pag_posts =pag_obj.page(pag_obj.num_pages)
        
        return render(request, 'home.html', {'pag_obj': pag_posts})        
    '''

def SearchedView(request):
    if request.method == 'GET':
        search_query = request.GET.get('search')
        results = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query) |
                    Q(author__first_name__icontains=search_query) | Q(author__last_name__icontains=search_query) | 
                    Q(category__icontains=search_query))
        return render(request, 'search_blog.html', {'results': results})
    else:
        return render(request, 'search_blog.html', {})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))

def CategoryListView(request):
    categ_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'categ_menu_list': categ_menu_list})


def CategoryView(request, categs):
    category_posts = Post.objects.filter(category=categs.replace('-',' '))
    return render(request, 'categories.html', {'categs':categs.title().replace('-',' '), 'category_posts':category_posts})

class ArticleDetailView(DetailView):
    model=Post
    template_name = 'article_details.html'
    
    def get_context_data(self, *args, **kwargs):
        categ_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
   
        context["categ_menu"] = categ_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_blog.html'
    # fields = '__all__'
    # fields = ('title', 'body')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    # fields = '__all__'
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')

class CommentView(UpdateView):
    model = Comment
    form_class = CommentEditForm
    template_name = 'comment.html'

    def get_object(self, queryset=None):
        queryset = queryset or self.get_queryset()
        pk1 = self.kwargs.get('pk1')
        pk2 = self.kwargs.get('pk2')
        if pk1 is not None and pk2 is not None:
            return queryset.get(post_id=pk1, id=pk2)
        else:
            # Handle the case where one or both primary keys are missing
            # For example, raise a 404 error or redirect to another page
            return None
    
class DeleteCommentView(DeleteView):
    model = Comment
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_blog.html'
    # fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')

#def SearchPostView(request):
  #  return render(request, 'search_blog.html', {'categs':categs.title().replace('-',' '), 'category_posts':category_posts})

