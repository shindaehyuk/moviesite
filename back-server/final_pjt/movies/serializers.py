from rest_framework import serializers
from .models import Genre, Movie, Article, Comment

class MovieListSerializer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name')

    # 장르 id 참조
    genre_ids = GenreSerializer(many=True, read_only=True)
    like_users = serializers.PrimaryKeyRelatedField(many=True, read_only=True, required=False)
   
    class Meta:
        model = Movie
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie','user', 'username')


class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Article
        # fields = ('id', 'title', 'content')
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = CommentSerializer(many=True, read_only=True)
    # comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', )