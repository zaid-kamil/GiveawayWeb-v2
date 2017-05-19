import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from comments.forms import CommentForm
from comments.models import Comment
from products.forms import AddProduct, CreateGiveaway
from products.models import Product, Giveaway, GiveawayEntry


@login_required  # (login_url='/login/')
def addProducts(request):
    form = AddProduct(request.POST or None, request.FILES or None, initial={'creator': request.user.id})
    # saving form
    form.creator = request.user.id
    if form.is_valid():
        instance = form.save(commit=False)
        print(instance)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(request.path)

    context = {
        'form': form,
    }
    return render(request, "add_product.html", context)


@login_required  # (login_url='/login/')
def addGiveaway(request):
    products = Product.objects.all()

    form = CreateGiveaway(request.POST or None, request.FILES or None, initial={'user': request.user.id})
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(request.path)

    context = {
        'form': form,
    }
    return render(request, "add_giveaway.html", context)


def viewGiveaway(request):
    list = Giveaway.objects.all()
    page = request.GET.get('page', 1)  # Show 25 contacts per page
    paginator = Paginator(list, 4)

    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        list = paginator.page(10)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        list = paginator.page(paginator.num_pages)
    return render(request, "giveaway.html", {"list": list})


def viewProduct(request):
    return render(request, "product.html", {})


@login_required  # (login_url='/login/')
def viewGiveawayDetail(request, id):
    item = get_object_or_404(Giveaway, id=id)
    comments = Comment.objects.filter(giveaway_id=id)
    # logic for saving form
    if request.user.is_authenticated:
        entry = GiveawayEntry.objects.get(user=request.user.id, giveaway=id)
        if not entry:
            GiveawayEntry.objects.create(user=request.user.id, giveaway=id, total_points=0)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment_data = form.cleaned_data.get("content")
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        Giveaway.objects.all(pk=item.pk).update(comments=item.comments + 1)
        return HttpResponseRedirect(item.get_absolute_url())
    context = {
        "item": item,
        "comments": comments,
        "comment_form": form,
    }

    return render(request, "giveaway_details.html", context)


@login_required()
def viewProductDetail(request, id):
    item = get_object_or_404(Product, id=id)
    context = {'item': item}
    return render(request, "product.html", item)


@login_required  # (login_url='/login/')
def update_entry(request, id, s):
    user_id = request.user.id
    share = s
    entry = GiveawayEntry._default_manager.get(user=user_id, giveaway=id)
    if entry:
        if share == 'facebook':
            GiveawayEntry.objects.filter(user=user_id, giveaway=id).update(facebook_share_count=entry.facebook_share_count + 1,total_points=entry.total_points + 1)
        if share == 'twitter':
            GiveawayEntry.objects.filter(user=user_id, giveaway=id).update(twitter_share_count=entry.twitter_share_count + 1,
                                                                total_points=entry.total_points + 1)
        if share == 'google':
            GiveawayEntry.objects.filter(user=user_id, giveaway=id).update(google_plus_share_count=entry.google_plus_share_count + 1,
                                                                total_points=entry.total_points + 1)
        if share == 'stumble':
            GiveawayEntry.objects.filter(user=user_id, giveaway=id).update(stumble_share_count=entry.stumble_share_count + 1,
                                                                total_points=entry.total_points + 1)
        if share == 'linked':
            GiveawayEntry.objects.filter(user=user_id, giveaway=id).update(linked_share_count=entry.linked_share_count + 1,
                                                                total_points=entry.total_points + 1)

        response = {"point": entry.total_points,
                    "facebook": entry.facebook_share_count,
                    "google": entry.google_plus_share_count,
                    "stumble": entry.stumble_share_count,
                    "linked": entry.linked_share_count,
                    "success": "updated your share points",
                    "twitter": entry.twitter_share_count}
        return HttpResponse(json.dumps(response), content_type='application/json')
    else:
        response = {"error": "failed to update share status"}
    return HttpResponse(json.dumps(response), content_type='application/json')
