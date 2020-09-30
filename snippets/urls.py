from django.urls import path, include
from snippets import views
from rest_framework import renderers
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
#
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

urlpatterns = [
    path('', include(router.urls))
]
# urlpatterns = format_suffix_patterns([
    # path('', views.api_root),
    #
    # path('users/',
    #      # views.UserList.as_view(),
    #      user_list,
    #      name='user-list'),
    #
    # path('users/<int:pk>/',
    #      # views.UserDetail.as_view(),
    #      user_detail,
    #      name='user-detail'),
    #
    # path('snippets/',
    #      # views.SnippetList.as_view(),
    #      snippet_list,
    #      name='snippet-list'),
    #
    # path('snippets/<int:pk>/',
    #      # views.SnippetDetail.as_view(),
    #      snippet_detail,
    #      name='snippet-detail'),
    #
    # path('snippets/<int:pk>/highlight/',
    #      # views.SnippetHighlight.as_view(),
    #      snippet_highlight,
    #      name='snippet-highlight')
# ])

# urlpatterns = (urlpatterns)
