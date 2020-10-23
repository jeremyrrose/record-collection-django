# Record Collection API (Django)

Adapted for Django from [jeremyrrose](https://github.com/jeremyrrose)'s [Record Collection Learning Lab](https://github.com/jeremyrrose/record-collection). Deployed at http://record-collection-django.herokuapp.com/

## User Story

Your uncle heard that you're a computer genius -- and he wants you to build him an app to catalog his awesome record collection. He'd really like to be able to check his stacks while he's at the record store and add any new purchases to his virtual library from his phone.

Here's what he wants the app to be able to do:

* Display all the artists whose records he has
* Display all the records he owns for each artist
* Add new records for artists in his collection
* Add new records by searching artists in the database
* Add new artists and records if they are not in the database

## Key Models

```python
# User:
username = models.CharField(db_index=True, max_length=255, unique=True)
email = models.EmailField(db_index=True, unique=True)
first_name = models.CharField(max_length=255, null=True, blank=True)
last_name = models.CharField(max_length=255, null=True, blank=True)
is_active = models.BooleanField(default=True)
is_staff = models.BooleanField(default=True)
created_at = models.DateTimeField(auto_now_add=True)
```

```python
# Collection:  # Belongs to User
owner = models.OneToOneField(User, on_delete=models.CASCADE)
records = models.ManyToManyField(Record)
public = models.BooleanField(default=False)
artists = property(fget=get_artists)  # derived from records in collection; no Collection/Artist relationship
```

```python
# Artist:
name = models.CharField(max_length=255, unique=True)
hot_100_hits = models.IntegerField()
```

```python
# Record:
title = models.CharField(max_length=255)
artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='records')
release_year = models.IntegerField()
cover_image = models.URLField(max_length=455)
```

## Key Endpoints

```python
# Auth:
urlpatterns = [
   url(r'^users/register/$', RegistrationAPIView.as_view(), name='register'),
   url(r'^users/login/$', LoginAPIView.as_view(), name='login'),
   url(r'^users/autologin/$', AutoLoginView.as_view(), name='autologin')
]
```

```python
# API:  # all below: GET (no auth), POST (logged-in), PUT/DELETE (staff)
router.register('records', RecordViewset, basename='records')
router.register('artists', ArtistViewset, basename='artists')
router.register('collections', CollectionViewset, basename='collections')

custom_urlpatterns = [
    url(r'collections/(?P<pk>\d+)$', CollectionDetail.as_view(), name="collection"),  # no auth required at present! be careful.
    path(r'artist_search/<str:search_string>', ArtistSearch.as_view(), name="artist_search"),  # GET
    url(r'addable/artist/(?P<artist_pk>\d+)/', ArtistRecordsNotInCollection.as_view(), name="addable_records_by_artist")  # GET (auth required)
]
```
