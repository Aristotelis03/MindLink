
from hashtags.models import Hashtag

# Create your views here.
def trending_hashtags(request):
    trending_hashtags = Hashtag.objects.filter(post__isnull=False).distinct().order_by('-post__created_at')[:5]

  # Adjust this based on your criteria for "trending"
    return {'trending_hashtags': trending_hashtags}
