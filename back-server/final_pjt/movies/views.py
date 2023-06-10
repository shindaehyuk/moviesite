from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Count
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, get_list_or_404
import requests, random

from .models import Article, Comment, Movie, Genre

from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, MovieListSerializer
from .serializers import MovieListSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated



from django.contrib.auth import get_user_model
User = get_user_model()

# 회원탈퇴
@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete_token(request):
    person = get_object_or_404(User, username=request.data['username'])
    person.delete()
    context = {
        'delete_message': '성공적으로 탈퇴하셨습니다.'
    }
    return Response(context)

# 전체게시글 조회 및 게시글 생성
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#내가 쓴 게시글 리스트
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myarticle_list(request, user_pk):
    if request.method == 'GET':
        articles = Article.objects.filter(user_id=user_pk)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)


# 게시글 디테일보기
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    
@api_view(['POST'])
def comment_create(request, movie_id):
    # article = Article.objects.get(pk=article_pk)
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 영화 전체 데이터 가져오기
@api_view(['GET'])
def showMovies(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


# 영화 디테일 가져오기
@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'GET':
        serializer = MovieListSerializer(movie)
        print(serializer.data)
        return Response(serializer.data)
    
    # elif request.method == 'DELETE':
    #     movie.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # elif request.method == 'PUT':
    #     serializer = MovieListSerializer(movie, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)


# 영화 디테일에서 댓글 작성하기
@api_view(['POST'])
def moviecomment_create(request, movie_id):
    print(request)
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = CommentSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# 영화 댓글 가져오기
@api_view(['GET'])
def moviecomment_detail(request, movie_id):
    comments = Comment.objects.filter(movie_id=movie_id)
    if request.method == 'GET':  
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(['DELETE', 'PUT'])
def moviecomment_comment(request, movie_id, comment_id):
    comments = Comment.objects.filter(id=comment_id)

    if request.method == 'DELETE':
        comments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comments, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def mycomment_list(request, user_pk):
    comments = Comment.objects.filter(user_id=user_pk)
    if request.method == 'GET':  
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def addmovies(request):
    movies_data = request.data['movies']
    movie_data_list = []
    
    for movie_data in movies_data:
        genre_ids = movie_data.pop('genre_ids', [])
        serializer = MovieListSerializer(data=movie_data)
        
        if serializer.is_valid():
            movie = serializer.save()
            movie.genre_ids.set(genre_ids)
            movie_data_list.append(serializer.validated_data)

    return JsonResponse(movie_data_list, safe=False, status=200)

@api_view(['GET'])
def first_likes(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.rating_total = movie.like_users.count()
    return JsonResponse({'total_likes': movie.rating_total})


# 영화 좋아요 
@api_view(['GET','POST'])
def movie_likes(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        movie.rating_total = movie.like_users.count()
        print(request.user.pk)
        if request.user.is_authenticated:
            print('로그인되어있음')
            liked = movie.like_users.filter(pk=request.user.pk).exists()

            return JsonResponse({'liked': liked, 'total_likes': movie.rating_total})
        print('로그인 안되어있음')
        return JsonResponse({'liked': False, 'total_likes': movie.rating_total})
        

    elif request.method == 'POST':
        print(request.user.pk)
        if request.user.is_authenticated:
            if movie.like_users.filter(pk=request.user.pk).exists():
                # 사용자가 이미 영화를 좋아요했으므로 좋아요를 취소합니다.
                print('좋아요취소')
                movie.like_users.remove(request.user)
                liked = False
            else:
                # 사용자가 영화를 좋아요하지 않았으므로 좋아요를 합니다.
                print('좋아요누름')
                movie.like_users.add(request.user)
                liked = True
            
            # 영화의 전체 좋아요 수를 업데이트합니다.
            movie.rating_total = movie.like_users.count()
            movie.save()
            
            return JsonResponse({'liked': liked, 'total_likes': movie.rating_total})
        
        return JsonResponse({'error': '인증이 필요합니다.'}, status=401)

# 최신영화 인기순
def popular_movies(request):
    popular_movies = Movie.objects.filter(vote_count__gte=5000,release_date__year__gte=2018).order_by('-popularity','-release_date' )[:25]
    
    movie_data = []
    for movie in popular_movies:
        movie_data.append({
            'id': movie.id,
            'title': movie.title,
            'release_date': movie.release_date,
            'popularity': movie.popularity,
            'poster_path' : movie.poster_path,
            'vote_average' : movie.vote_average,
            'overview' : movie.overview
        })

    return JsonResponse({'popular_movies': movie_data})

def new_movies(request):
    new_movies = Movie.objects.filter(release_date__year__gte=2023, release_date__month__gte=1).order_by('-popularity','-release_date' )[:25]

    movie_data = []
    for movie in new_movies:
        movie_data.append({
            'id': movie.id,
            'title': movie.title,
            'release_date': movie.release_date,
            'popularity': movie.popularity,
            'poster_path' : movie.poster_path,
            'vote_average' : movie.vote_average,
            'overview' : movie.overview
        })

    return JsonResponse({'new_movies': movie_data})

#평점순
def rank_movies(request):
    rank_movies = Movie.objects.filter(vote_count__gte=1000,release_date__year__gte=1970).order_by('-vote_average')[:25]

    movie_data = []
    for movie in rank_movies:
        movie_data.append({
            'id': movie.id,
            'title': movie.title,
            'release_date': movie.release_date,
            'popularity': movie.popularity,
            'poster_path' : movie.poster_path,
            'vote_average' : movie.vote_average,
            'overview' : movie.overview
        })

    return JsonResponse({'rank_movies': movie_data})


# User가 좋아요 누른 영화와 같은 장르 영화 추천
@csrf_exempt
def movie_recommend_genre(request, user_pk):
    if request.method == 'GET':
        
        user_movies = Movie.objects.filter(like_users__id=user_pk)  
        user_genres = []

        for movie in user_movies:
            genre_ids = movie.genre_ids.all().values_list('id', flat=True)  
            user_genres.extend(list(genre_ids))  

        recommended_movies = Movie.objects.filter(genre_ids__in=user_genres).exclude(like_users__id=user_pk).distinct()
        recommended_movies = random.sample(list(recommended_movies), min(12, len(recommended_movies)))
        
        top_movies = Movie.objects.annotate(like_count=Count('like_users')).order_by('-like_count')[:20]       

        # 추천된 영화 목록을 JSON 형태로 반환
        response_data = {
            'movies': [],
            'user_movies' : [],
            'top_movies' : []
        }

        for movie in recommended_movies:
            response_data['movies'].append({
                'id': movie.id,
                'title': movie.title,
                'release_date': movie.release_date.strftime('%Y-%m-%d'),
                'popularity': movie.popularity,
                'vote_count': movie.vote_count,
                'vote_average': movie.vote_average,
                'overview': movie.overview,
                'poster_path': movie.poster_path
            })
        
        for movie in user_movies :
            response_data['user_movies'].append({
                'id': movie.id,
                'title': movie.title,
                'release_date': movie.release_date.strftime('%Y-%m-%d'),
                'popularity': movie.popularity,
                'vote_count': movie.vote_count,
                'vote_average': movie.vote_average,
                'overview': movie.overview,
                'poster_path': movie.poster_path
            })

        for movie in top_movies:
            response_data['top_movies'].append({
                'id': movie.id,
                'title': movie.title,
                'release_date': movie.release_date,
                'popularity': movie.popularity,
                'poster_path' : movie.poster_path,
                'vote_average' : movie.vote_average,
                'overview' : movie.overview
            })

        return JsonResponse(response_data)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
