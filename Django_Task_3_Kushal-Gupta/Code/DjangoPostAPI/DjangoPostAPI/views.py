from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post
import json

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        try:

            data = json.loads(request.body)
            title = data.get('title')
            content = data.get('content')
            
            if not title or not content:
                return JsonResponse({'error': 'Both title and content are required.'}, status=400)

            post = Post.objects.create(title=title, content=content)
            
            post_count = Post.objects.count()

            return JsonResponse({
                'count': post_count,
                'post': {
                    'id': post.id,
                    'title': post.title,
                    'content': post.content
                }
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format. Please check your request body.'}, status=400)

    return JsonResponse({'error': 'Only POST method is allowed for creating posts.'}, status=405)
