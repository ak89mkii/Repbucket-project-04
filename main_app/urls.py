from django.urls import path
from . import views
from django.contrib.auth.models import User

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('talents/', views.talents_index, name='index'),
    path('quests/', views.quests_index, name='quests'),
    path('accounts/signup/', views.signup, name='signup'),
    # talents
    path('talents/create/', views.TalentCreate.as_view(), name='talents_create'),
    path('talents/<int:pk>/update/', views.TalentUpdate.as_view(), name='talents_update'),
    path('talents/<int:pk>/delete/', views.TalentDelete.as_view(), name='talents_delete'),
    # learns
    path('learns/create/', views.LearnCreate.as_view(), name='learns_create'),
    path('learns/<int:pk>/update/', views.LearnUpdate.as_view(), name='learns_update'),
    path('learns/<int:pk>/delete/', views.LearnDelete.as_view(), name='learns_delete'),
    # quests
    path('quests/create/', views.QuestCreate.as_view(), name='quests_create'),
    path('quests/<int:pk>/update/', views.QuestUpdate.as_view(), name='quests_update'),
    path('quests/<int:pk>/delete/', views.QuestDelete.as_view(), name='quests_delete'),
    # accepts
    path('accepts/create/', views.AcceptCreate.as_view(), name='accepts_create'),
    path('accepts/<int:pk>/update/', views.AcceptUpdate.as_view(), name='accepts_update'),
    path('accepts/<int:pk>/delete/', views.AcceptDelete.as_view(), name='accepts_delete')
]