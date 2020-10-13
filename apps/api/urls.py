from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from apps.api.views import BlankView, RecordViewset, ArtistViewset, ArtistSearch, CollectionDetail, CollectionViewset, ArtistRecordsNotInCollection

router = routers.DefaultRouter()
router.register('records', RecordViewset, basename='records')
router.register('artists', ArtistViewset, basename='artists')
router.register('collections', CollectionViewset, basename='collections')
# router.register('recipes', RecipeViewset, basename='recipes')

custom_urlpatterns = [
    # url(r'categories/(?P<category_pk>\d+)/recipes/$', CategoryRecipes.as_view(), name='category_recipes'),
    # url(r'categories/(?P<category_pk>\d+)/recipes/(?P<pk>\d+)$', SingleCategoryRecipe.as_view(), name='single_category_recipe'),
    url(r'tryingit/(?P<whatever>\d+)/and/(?P<dumb>\d+)$', BlankView, name="trying"),
    url(r'collections/(?P<pk>\d+)$', CollectionDetail.as_view(), name="collection"),
    path(r'artist_search/<str:search_string>', ArtistSearch.as_view(), name="artist_search"),
    url(r'addable/artist/(?P<artist_pk>\d+)/', ArtistRecordsNotInCollection.as_view(), name="addable_records_by_artist")
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns

