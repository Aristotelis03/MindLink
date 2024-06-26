# MindLink #


- - - -
Video Presentation : https://www.youtube.com/watch?v=2uZtcTg92OQ

MindLink is a microblogging-focused social networking platform that empowers users to share their thoughts and ideas. The page is a web application created for social networking.

## Implementation: ##

* In front-end I decided to keep it simple, so I used HTML, CSS, JavaScript, and Bootstrap in some cases
* For back-end, I picked the Django framework that uses Python
* For the Database, I used PostgreSQL

## How MindLink works? ##

To join MindLink, one simply needs to create an account and log in. Once inside, users can freely share their thoughts, post pictures, engage with others by liking and commenting on posts, and curate a personalized collection by saving favorite content. Relationships blossom as users connect with each other through the simple act of following. MindLink isn't just a platform—it's a space where ideas, images, and connections flourish for anyone who joins.

## Apps ##

### Account ###


The Account app is vital for generating user models in the database. It utilizes the AbstractUser class to create a model named CustomUsers, inheriting from Django's built-in User model. Despite its compact size, the Account app, lacking views or templates, is essential for fundamental user management within the project.


Code example

* Models
``` python
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class CustomUser(AbstractUser):

    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True, default='pictures/default_profile_picture/profile_picture.png')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    followers = models.ManyToManyField('self',  through='user_relations.Relations', symmetrical=False, related_name='following_users')
    favorites_post = models.ManyToManyField('post.Post', related_name='favorited_by')


        # Use unique related_name values to avoid clashes
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_groups')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_permissions')


    def __str__(self):
        return self.username

```

### Authentication ###

Authentication handles user login and registration pages, featuring a dedicated forms file for input validation. This app is vital for user management, contributing to the project's overall security and user experience.

Code example



### Homepage ###


This app manages the content presentation on the site's homepage. Its view is responsible for rendering all comments within the page and passing essential variables to its associated templates. Unlike other apps, Homepage doesn't have its own model. However, its templates are frequently invoked by other templates to ensure a consistent and uniform appearance across all pages.


### Paragraph ###

Code example
views
views.py
templates
Template.html




### User_relations ###

In User_relations the model for the follow and the unfollow functionalities and the view for the corresponding buttons are conducted.

Code example
views
views.py
templates
Template.html

### Posts ###

The Post app plays an important role in managing various post-related functions, such as post creation, comment handling, and like interactions. Beyond these essential functionalities, it also assumes the responsibility of seamlessly presenting these posts within the project interface. Furthermore, the Post app takes charge of crafting the requisite models for efficient database management, ensuring a cohesive and streamlined experience for users.



Code example
views
views.py
templates
Template.html

### User_managment ###


The User_management app oversees tasks related to user-specific functionality, including rendering the user's profile page and the page where a user's favorite posts are stored.

Code example
views
views.py
templates
Template.html

### Search ###

The Search app provides search functionalities on the website. It takes user input and queries the database to find posts, users, or hashtags containing the input value. Additionally, it is responsible for returning the search results to the relevant template.

### Paragraph ###

Code example
* Views
``` python
from re import search
from hashtags.models import Hashtag
from accounts.models import CustomUser
from post.models import Post
from django.shortcuts import get_object_or_404, render


def users_results_view(request, search_input):
    users_results = CustomUser.objects.filter(username__icontains=search_input)
    hashtags_results = Hashtag.objects.filter(name__icontains=search_input)
    posts_results = Post.objects.filter(content__icontains=search_input)
    context = {
        'search_input' : search_input,
        'users_results' : users_results,
        'hashtags_results' : hashtags_results,
        'posts' : posts_results,
    }


    if not users_results:
        context['no_users_found'] = True


    if not hashtags_results:
        context['no_hashtag_found'] = True

    if not posts_results:
        context['no_posts_found'] = True

    return render(request, 'search.html', context)
```

* Templates
``` html
{% extends "base.html" %}
{% load static %}

{% block search_style %}
<link rel="stylesheet" type="text/css" href="{% static 'search/search_style.css' %}">
{% endblock %}
{% block title %} Search : {{search_input}} {% endblock %}
{% block content %}
    <div class="search_tabs">
        <button class="tablinks" onclick="resultsSection(event, 'posts_results')" id="defaultOpen">Posts</button>
        <button class="tablinks" onclick="resultsSection(event, 'users_results')">Users</button>
        <button class="tablinks" onclick="resultsSection(event, 'hashtags_results')">Hashtags</button>
    </div>
    <div class="users_results tabcontent" id="users_results">
         {% if no_users_found %}
        <p>No users found.</p>
        {% elif users_results %}
            {% for username in users_results %}
            <div class="box">
                <div class="grid-container-users">
                    <img src="{{username.profile_image.url}}" class="grid-item profile-picture" alt="profile_picture" width="40" height="40">
                    <span class="grid-item post-username">
                        <a href="{% url 'user_profile_view' username %}" style="font-weight:bold;">
                            {{ username }}
                        </a>
                    </span>
                </div>

            </div>

            {% endfor %}
        {% endif %}
    </div>


    <div class="hashtags_results tabcontent" id="hashtags_results">
        {% if no_hashtag_found %}
        <p>No hashtags found.</p>
        {% elif hashtags_results %}
            {% for hashtag in hashtags_results %}
            <div class="box">
                <a href="{% url 'hashtag_posts' hashtag.name %} ">#{{ hashtag }}</a>

            </div>
            {% endfor %}
        {% endif %}
    </div>

    <div class="posts_results tabcontent" id="posts_results">
        {% if no_posts_found %}
            <p>No posts found.</p>
            {% elif posts %}
                <div class="post_section">
                    {% include "posts_section.html" %}
                </div>
        {% endif %}

    </div>

    <script>
        function resultsSection(evt, section) {
            // Declare all variables
            var i, tabcontent, tablinks;

            // Get all elements with class="tabcontent" and hide them
            tabcontent = document.getElementsByClassName("tabcontent");
            for (i = 0; i < tabcontent.length; i++) {
            tabcontent[i].style.display = "none";
            }

            // Get all elements with class="tablinks" and remove the class "active"
            tablinks = document.getElementsByClassName("tablinks");
            for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
            }

            // Show the current tab, and add an "active" class to the button that opened the tab
            document.getElementById(section).style.display = "block";
            evt.currentTarget.className += " active";

        }
        document.getElementById("defaultOpen").click();
      </script>
{% endblock %}

```
### Hashtags ###


The Hashtags app is tasked with creating the Hashtag model and rendering a page that includes all posts associated with a specific hashtag.


Code example
views
views.py
templates
template.html



 ## Details ##

The project can't be considered a completed social networking platform yet, it's more like a prototype in this state, but it's a full functioning web application and i am planning to keep working on it after the submission.



