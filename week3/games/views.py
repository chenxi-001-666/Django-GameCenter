from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .forms import ReviewForm
from .models import Review, Game  # 确保导入了 Game 模型
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # 注册成功后直接登录
            return redirect('game_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def add_review(request, slug):
    game = get_object_or_404(Game, slug=slug)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        if rating and comment:
            # 自动将当前登录用户 (request.user) 存入数据库
            Review.objects.create(
                game=game,
                user=request.user,
                rating=rating,
                comment=comment
            )
    # 提交后跳回该游戏的评论页，并定位到新评论
    return redirect('game_specific_reviews', slug=slug)

class AllReviewListView(ListView):
    model = Review
    template_name = 'games/review_list.html' # 必须与 urls.py 对应
    context_object_name = 'reviews'
    ordering = ['-created_at'] # 最新的评论排在前面

# 2. 查看某个特定游戏的 Review
class GameReviewListView(ListView):
    model = Review
    template_name = 'games/game_specific_reviews.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        # 通过 URL 里的 slug 找到对应的游戏，并过滤其评论
        self.game = get_object_or_404(Game, slug=self.kwargs['slug'])
        return Review.objects.filter(game=self.game)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = self.game
        return context

# 这是你需要添加的类 (报错就是因为少了它)
class GameListView(ListView):
    model = Game
    template_name = 'games/game_list.html'
    context_object_name = 'games'