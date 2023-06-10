from django.urls import include, path
from . import views

urlpatterns = [
    path('showmovies/', views.showMovies),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/comments/', views.moviecomment_create),
    path('<int:movie_id>/comments/detail/', views.moviecomment_detail),
    path('<int:movie_id>/comments/detail/<int:comment_id>/', views.moviecomment_comment),
    path('<int:movie_id>/movie_likes/', views.movie_likes),
    path('<int:movie_id>/first_likes/', views.first_likes),
    path("popular_movies/", views.popular_movies),
    path("new_movies/", views.new_movies),
    path("rank_movies/", views.rank_movies),
    path("<int:user_pk>/recommend_movies/", views.movie_recommend_genre),
    path("addmovies/", views.addmovies),

    path('articles/', views.article_list),
    path('userinfo/<int:user_pk>/', views.myarticle_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('comments/user/<int:user_pk>/', views.mycomment_list),
    path('articles/<int:article_pk>/comments/', views.comment_create),
    path('userdelete/', views.delete_token),

]
