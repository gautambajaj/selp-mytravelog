from django.conf.urls import patterns, url
from mytravelog.views import search, album, log, like, comment, follower, leaderboard
from mytravelog.views.live_feed import show_live_feed
from views import home, user, city

__author__ = 'Manas'

urlpatterns = patterns(
    '',
    url(r'^$', home.show_home),
    url(r'^sign_up/$', user.sign_up),
    url(r'^sign_in/$', user.sign_in),
    url(r'^sign_out/$', user.sign_out),
    url(r'^city/autocomplete/$', city.get_autocomplete_suggestions),
    url(r'^city/(?P<city_url_name>\w+)/$', city.show_city),
    url(r'^search/$', search.search_for_cities_and_users),
    url(r'^user/(?P<username>\w+)/$', user.show_user),
    url(r'^album/create/$', album.create_album),
    url(r'^album/update/(?P<album_id>\w+)/$', album.update_album),
    url(r'^album/delete/(?P<album_id>\w+)/$', album.delete_album),
    url(r'^album/(?P<album_id>\w+)/$', album.show_album),
    url(r'^log/create/$', log.create_log),
    url(r'^log/delete/(?P<log_id>\w+)/$', log.delete_log),
    url(r'^log/edit/(?P<log_id>\w+)/$', log.edit_log),
    url(r'^log/(?P<log_id>\w+)/$', log.show_log),
    url(r'^log/get_info_for_map/(?P<username>\w+)/$', log.get_log_info_for_map),
    url(r'^like/create/(?P<log_id>\w+)/$', like.like_log),
    url(r'^like/delete/(?P<log_id>\w+)/$', like.dislike_log),
    url(r'^comment/create/(?P<log_id>\w+)/$', comment.create_log_comment),
    url(r'^comment/delete/(?P<comment_id>\w+)/$', comment.delete_log_comment),
    url(r'^follower/create/(?P<following_user_profile_id>\w+)/$', follower.create_follower),
    url(r'^follower/delete/(?P<following_user_profile_id>\w+)/$', follower.delete_follower),
    url(r'^live_feed/(?P<feed_filter>\w+)/$', show_live_feed),
    url(r'^leaderboard/(?P<model>\w+)/$', leaderboard.show_leaderboard)
)
