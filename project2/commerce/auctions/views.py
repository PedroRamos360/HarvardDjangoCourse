from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse

from .models import *
from .forms import *


def index(request):
    q = request.GET.get('q')
    if q:
        category = Category.objects.get(name=q)
        return render(request, "auctions/index.html", {
            'auctions': AuctionList.objects.filter(category=category)
        })
    else:
        return render(request, "auctions/index.html", {
            'auctions': AuctionList.objects.all()
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def auction(request, id):
    auction = AuctionList.objects.get(id=id)
    comments = Comment.objects.filter(auction_list=auction)
    watchlisted = ''
    bids = Bid.objects.filter(auction_list=auction)
    now_bid = None
    for bid in bids:
        if bid.price == auction.price:
            now_bid = bid
    number_of_bids = len(bids)
    user_bid_to_auction = None
    try:
        bids_from_user = bids.filter(user=request.user)
        user_bid_to_auction = bids_from_user[len(bids_from_user) -1]
    except:
        pass
    if request.user.is_authenticated:
        watchlisted = WatchlistItem.objects.filter(user=request.user, auction_list=auction).exists()
    return render(request, 'auctions/auction.html', {
        'auction': auction,
        'min_bid': auction.price + 0.01,
        'watchlisted': watchlisted,
        'comments': comments,
        'bids': bids,
        'now_bid': now_bid,
        'number_of_bids': number_of_bids,
        'user_bid_to_auction': user_bid_to_auction
    })


def categories(request):
    return render(request, 'auctions/categories.html', {
        'categories': Category.objects.all()
    })


@login_required
def watchlist(request):
    if request.method == "POST":
        id = request.POST['id']
        add = request.POST['add']
        auction_list = AuctionList.objects.get(id=id)
        if add == 'True':
            watchlist_item = WatchlistItem(user=request.user, auction_list=auction_list)
            watchlist_item.save()
        else:
            watchlist_item = WatchlistItem.objects.filter(user=request.user, auction_list=auction_list)
            watchlist_item.delete()
    
    watchlist_items = WatchlistItem.objects.filter(user=request.user)

    return render(request, 'auctions/watchlist.html', {
        'watchlist': watchlist_items
    })

@login_required
def your_listings(request):
    yourlist_items = AuctionList.objects.filter(user=request.user)

    return render(request, 'auctions/your_listings.html', {
        'yourlist_items': yourlist_items
    })


@login_required
def create_listing(request):
    if request.method == 'POST':
        form = CreateListing(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            starting_bid = form.cleaned_data['starting_bid']
            description = form.cleaned_data['description']
            image_url = form.cleaned_data['image_url']
            category_id = form.cleaned_data['category']
            category = Category.objects.get(id=category_id)
            new_list = AuctionList(name=name, price=starting_bid, user=request.user, image_url=image_url, description=description, category=category)
            new_list.save()
            return HttpResponseRedirect(f'/auctions/{new_list.id}')

    form = CreateListing()
    return render(request, 'auctions/create_listing.html', {
        'form': form
    })


@login_required
def comment(request):
    if request.method == 'POST':
        id = request.POST['id']
        content = request.POST['content']
        auction_list = AuctionList.objects.get(id=id)
        new_comment = Comment(user=request.user, auction_list=auction_list, content=content)
        new_comment.save()
        return HttpResponseRedirect(f'/auctions/{id}')
    return HttpResponseRedirect('/')


@login_required
def bid(request):
    if request.method == 'POST':
        id = request.POST['id']
        bid = request.POST['bid']
        auction_list = AuctionList.objects.get(id=id)
        new_bid = Bid(user=request.user, auction_list=auction_list, price=bid)
        new_bid.save()
        auction_list.price = bid
        auction_list.save()
        return HttpResponseRedirect(f'/auctions/{id}')
    return HttpResponseRedirect('/')


@login_required
def endauction(request):
    if request.method == 'POST':
        id = request.POST['id']
        bid_user = request.POST['bid_user']
        auction_list = AuctionList.objects.get(id=id)
        auction_list.active = False
        auction_list.save()
        user = request.user
        user.balance = user.balance + auction_list.price
        user.save()
        winner_user = User.objects.get(username=bid_user)
        winner_user.balance = winner_user.balance - auction_list.price
        winner_user.save()
        return HttpResponseRedirect(f'/auctions/{id}')
    return HttpResponseRedirect('/')