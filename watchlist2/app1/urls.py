


from django.urls import path
from .views import Movielist,Serieslist,Details,About,get_high_rated_movies,malayalam_lang,tamil_lang,hindi_lang,wishlist,add_to_list,remove_from_list
from .import views 
from .views import telugu_lang,other_lang,video,SearchResultsView



urlpatterns = [
    path('',Movielist.as_view(), name='list'),
    path('series/', Serieslist.as_view(), name='series'),
    path('deta/<int:pk>', Details.as_view(), name='detail'),
    path('serideta/<int:pk>', About.as_view(), name='seriesdetail'),
    path('hgrated/', views.get_high_rated_movies, name='hgratedm'),
    path('malayalam/',views.malayalam_lang,name='mallu'),
    path('tamil/',views.tamil_lang,name='twood'),
    path('hindi/',views.hindi_lang,name='bwood'),
    path('telugu/',views.telugu_lang,name='tewood'),
    path('other/',views.other_lang,name='owood'),
    path('wishlist/',wishlist,name ='watchlist'),
    path('add_to_list/<int:movie_id>/',views.add_to_list,name = 'add_to_list'),
    path('remove_from_list/<int:movie_id>/',views.remove_from_list,name = 'remove_from_list'),
    path('video/',video,name='video'),
    path('search/',SearchResultsView.as_view(),name='search')

    
]
