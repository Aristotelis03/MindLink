# Create your views here.
def friends(request):
    if request.user.is_authenticated:
              
        # Display all the followers 
        followers = request.user.followers.all()
        # Display all the users you follow
        following = request.user.following_users.all()
        # Shows followers that you follow back
        followers_back = followers.intersection(following)[:5]

        return {'followers_back': followers_back}
    return {'followers_back': None}
