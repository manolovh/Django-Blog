from datetime import date
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse

posts_list = [
    {
        "slug": "hike-in-the-mountains",
        "image": "1.jfif",
        "author": "Haralambi",
        "date": date(2023, 1, 12),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like mountain views! I didn't even expect that!",
        "content": """
                Whether you’re a ski tourer or a freerider – anyone who loves spending time in the mountains knows that sometimes

                the most beautiful challenges lie right on your front doorstep. During the #salewahome campaign,

                Salewa called on mountain enthusiasts to share their mountain dreams – and then offered to help them come true.

                The applicants had to come with the required the fitness and audacity, while Salewa supplied the equipment and
                
                mountain guide support.Five projects were selected – five dreams came true.
        """,
    },
    {
        "slug": "programming-is-fun",
        "image": "code.jpg",
        "author": "Haralambi",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """,
    },
    {
        "slug": "into-the-woods",
        "image": "nature.jpg",
        "author": "Haralambi",
        "date": date(2022, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """,
    }
]

def get_date(post):
    return post.get("date")

def index(request):
    sorted_posts = sorted(posts_list, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts,
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": posts_list,
    })

def post_detail(request, slug):
    found_post = next(post for post in posts_list if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": found_post,
    })