from django.contrib import admin
from django.urls import path, re_path, include
from graphene_file_upload.django import FileUploadGraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^graphql/', csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True))),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
