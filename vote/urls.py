from django.urls import path
from vote import views

urlpatterns = [
    path('votealike/', views.VoteAlikeList.as_view()),
    path('votealike/<int:pk>', views.VoteAlikeDetail.as_view()),
    path('votenotalike/', views.VoteNotAlikeList.as_view()),
    path('votenotalike/<int:pk>', views.VoteNotAlikeDetail.as_view()),
]