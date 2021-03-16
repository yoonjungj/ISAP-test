from django.shortcuts import render

# Create your views here.


def index(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }
    return render(req, "index.html", context=context)
