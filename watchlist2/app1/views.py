from _decimal import Decimal
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView,DetailView
from django.db.models import Q 
from django.contrib.auth.decorators import login_required
from .models import Movies,Series,watchlist,moviestowatch
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Movielist(ListView):
    model = Movies
    template_name = 'popmovie.html' 

class Serieslist(ListView):
    model= Series
    template_name = 'Series.html'
    

class Details(LoginRequiredMixin,DetailView):
    model = Movies
    template_name = 'detailview.html'
class About(DetailView):
    model = Series
    template_name = 'seriesdetail.html'
def get_high_rated_movies(request):
    high_rated_movies = Movies.objects.filter(Rating__gt=8.0,Type='Movie')
    
    return render(request, 'topratedmovies.html', {'highratedm': high_rated_movies})

def malayalam_lang(request):
    mal1 = Movies.objects.filter(Language='Malayalam')
    return render(request, 'malayalam.html',{'malluwood':mal1})
def tamil_lang(request):
    tam1 = Movies.objects.filter(Language="Tamil")
    return render(request,'tamil.html',{'tollywood':tam1})
def hindi_lang(request):
    hindi1 = Movies.objects.filter(Language="Hindi")
    return render(request,'hindimovie.html',{'bollywood':hindi1})
def telugu_lang(request):
    telugu1 = Movies.objects.filter(Language= "Telugu")
    return render(request,'telugumovie.html',{'teluwood':telugu1})
def other_lang(request):
    other1 = Movies.objects.filter(Q(Language = 'English',Type="Movie")|Q(Language = "Japan")|Q(Language="Korean")|Q(Language="Kannada"))
    return render(request,"otherlang.html",{'otherwood':other1})


@login_required
def wishlist(request):
    wishlist_qs = watchlist.objects.filter(user=request.user)
    if wishlist_qs.exists():
        wishlist_obj = wishlist_qs.first()
        wishlist_items = moviestowatch.objects.filter(wishlist=wishlist_obj)
    else:
        wishlist_obj = None
        wishlist_items = []
    context = {
        'wishlist': wishlist_obj,
        'wishlist_items': wishlist_items
    }
    return render(request, 'watchlist/watchlist.html', context)


@login_required
def add_to_list(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    wishlist_qs = watchlist.objects.filter(user=request.user)
    if wishlist_qs.exists():
        wishlist_obj = wishlist_qs.first()
    else:
        wishlist_obj = watchlist.objects.create(user=request.user, total_price=Decimal('0.00'))
    cart_item, created = moviestowatch.objects.get_or_create(movie=movie, cart=wishlist_obj)
    
    return redirect('watchlist')

def remove_from_list(request,movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    wishlist_qs = watchlist.objects.filter(user=request.user)
    if wishlist_qs.exists():
        wishlist_obj = wishlist_qs.first()
        wishlist_item_qs = moviestowatch.objects.filter(movie=movie,wishlist=wishlist_obj)
        if wishlist_item_qs.exists():
            cart_item = wishlist_item_qs.first()
            cart_item.delete()
        return redirect('watchlist')

def video(request):
    obj = Movies.objects.all()
    return render (request,'video.html',{'obj':obj})



class SearchResultsView(ListView):
    template_name = 'searchview.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            
            movies_results = Movies.objects.filter(
                Q(title__icontains=query) |
                Q(Director__icontains=query) |
                Q(Actor__icontains=query) |
                Q(Language__icontains=query) |
                Q(Type__icontains=query)
            )
            series_results = Series.objects.filter(
                Q(Name__icontains=query) |
                Q(Director__icontains=query) |
                Q(Actors__icontains=query) 
            )
            search_results = list(movies_results) + list(series_results)
            return search_results


        return []




    