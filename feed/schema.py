import graphene
from graphene_django.types import DjangoObjectType
from .models import Feed, Category, Tag, ChildCategory
from graphene_file_upload.scalars import Upload


class FeedType(DjangoObjectType):
    class Meta:
        model = Feed


class FeedMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        thumbnail = Upload(required=True)
        category = graphene.Int(required=True)
        childCategory = graphene.Int(required=True)
        tags = graphene.List(graphene.NonNull(graphene.String))

    feed = graphene.Field(FeedType)

    def mutate(self, info, title, content, category, thumbnail, childCategory, tags):

        feed = Feed.objects.create(
            title=title,
            content=content,
            thumbnail=thumbnail,
            category=Category.objects.get(id=category),
            childCategory=ChildCategory.objects.get(id=childCategory)
        )

        feed.save()

        for i in tags:
            if Tag.objects.filter(name=i).exists():
                tag = Tag.objects.get(name=i)
                feed.tag.add(tag)
            else:
                tag = Tag.objects.create(name=i)
                tag.save()
                feed.tag.add(tag)

        return FeedMutation(feed=feed)


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class ChildCategoryType(DjangoObjectType):
    class Meta:
        model = ChildCategory


class Query(graphene.AbstractType):
    all_feed = graphene.List(FeedType)

    all_category = graphene.List(CategoryType)

    all_tag = graphene.List(TagType)

    all_childCategory = graphene.List(ChildCategoryType)

    feed = graphene.Field(FeedType, id=graphene.Int(), term=graphene.String())

    tag = graphene.Field(TagType, term=graphene.String())

    def resolve_all_feed(self, context, **kwargs):
        return Feed.objects.all()

    def resolve_feed(self, info, **kwargs):
        id = kwargs.get('id')
        term = kwargs.get('term')

        if id is not None:
            return Feed.objects.get(pk=id)

        if term is not None:
            return Feed.objects.filter(title__contains=term)

        return None

    def resolve_all_portfolioCategory(self, context, **kwargs):
        return Category.objects.all()

    def resolve_all_tag(self, context, **kwargs):
        return Tag.objects.all()

    def resolve_tag(self, info, **kwargs):
        term = kwargs.get('term')

        if term is not None:
            return Tag.objects.filter(name__contains=term)

        return None

    def resolve_all_childCategory(self, context, **kwargs):
        return ChildCategory.objects.all()



class Mutation(graphene.ObjectType):
    create_feed = FeedMutation.Field()
