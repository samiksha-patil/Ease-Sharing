from django.shortcuts import render, get_object_or_404,redirect
from .models import Post,Answer
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .forms import  AnswerForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
     posts=Post.objects.all()
          
     return render(request,'blog/home.html',{
        'posts' :posts
     })
class PostListView(ListView):
    model= Post
    template_name='blog/home.html'
    context_object_name = 'posts'
    ordering=['-date_posted']
    paginate_by=2

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(Q(subject__icontains=query)|Q(question__icontains=query)|Q(author__username__icontains=query))
            

        else:
            object_list = self.model.objects.all()
            

        
        return object_list

class PostDetailView(DetailView):
    model= Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model= Post
    fields=[ 'subject','question']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model= Post
    fields=[ 'subject','question']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model= Post
   
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UserPostListView(ListView):
    model= Post
    template_name='blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by=2   
    def get_queryset(self):
        user = get_object_or_404(User , username=self.kwargs.get('username')) 
        return Post.objects.filter(author=user).order_by('-date_posted')

#def add_answer_to_post(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    if request.method == "POST":
#        form = AnswerForm(request.POST)
#        answer.author= user
#        if form.is_valid():
#            answer = form.save(commit=False)
#            answer.post = post
#            answer.save()
            
#            return redirect('post-detail', pk=post.pk,**kwargs)
#    else:
#        form = AnswerForm()
#    return render(request, 'blog/add_answer_to_post.html', {'form': form})

class AnswerCreateView(LoginRequiredMixin,CreateView):
    model= Answer
    fields=['answer']
    template_name='blog/add_answer_to_post.html'
    
    def form_valid(self,form):
        post=self.get_object()
        form.instance.post = self.request.post
        form.instance.user=self.request.user
        return super(AnswerCreateView,self).form_valid(form)

def add_answer_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form=AnswerForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.post = post
            form.instance.author=request.user
            form.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = AnswerForm()
    return render(request, 'blog/add_answer_to_post.html', {'form': form})

            

class UserAnswerListView(ListView):
    model= Answer
    template_name='blog/user_answer.html'
    context_object_name = 'answers'
    paginate_by=2
    def get_queryset(self):
        user = get_object_or_404(User , username=self.kwargs.get('username')) 
        return Answer.objects.filter(author=user).order_by('-created_date')

@login_required
def prof(request,pk):
    totalposts= Post.objects.all()
    totalanswers= Answer.objects.all()
    user=User.objects.filter(pk=pk)
    posts=Post.objects.filter(author__id=pk)
    answers=Answer.objects.filter(author__id=pk)
    context={
        'totalposts':totalposts,
        'totalanswers':totalanswers,
        'user':user,
        'posts':posts,
        'answers':answers
    }
    return render(request, 'blog/prof.html', context)   