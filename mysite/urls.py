from django.contrib import admin
from django.urls import path, re_path, include
# from graphene_file_upload.django import FileUploadGraphQLView
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^graphql/', GraphQLView.as_view(graphiql=True)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
