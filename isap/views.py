from django.shortcuts import render

# Create your views here.


def base(req):
    # post_latest = Post.objects.order_by("-createDate")[:6]
    context = {
        # "post_latest": post_latest
    }
    return render(req, "base.html", context=context)

