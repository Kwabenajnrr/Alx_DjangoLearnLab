from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .models import Post
from .serializers import PostSerializer
from rest_framework import permissions


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Like
from notifications.models import Notification


["generics.get_object_or_404(Post, pk=pk)", "Like.objects.get_or_create(user=request.user, post=post)"]


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)

        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({"error": "Already liked"}, status=400)

        Like.objects.create(user=request.user, post=post)

        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target_id=post.id
        )

        return Response({"message": "Post liked"}, status=200)

    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=404)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({"message": "Post unliked"}, status=200)

    except Like.DoesNotExist:
        return Response({"error": "Like not found"}, status=404)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def feed(request):
    following_users = request.user.following.all()

    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)




@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def feed(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    return Response([{"id": post.id, "content": post.content} for post in posts])


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)

        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({"error": "Already liked"}, status=400)

        Like.objects.create(user=request.user, post=post)


        return Response({"message": "Post liked"}, status=200)

    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=404)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({"message": "Post unliked"}, status=200)

    except Like.DoesNotExist:
        return Response({"error": "Like not found"}, status=404)