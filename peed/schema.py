import graphene
from graphene_django.types import DjangoObjectType
from .models import Peed, Category, Tag, ChildCategory
from graphene_file_upload.scalars import Upload


class PeedType(DjangoObjectType):
    class Meta:
        model = Peed


class PeedMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        # thumbnail = Upload(required=True)
        category = graphene.Int(required=True)
        childCategory = graphene.Int(required=True)
        tags = graphene.List(graphene.NonNull(graphene.String))

    peed = graphene.Field(PeedType)

    def mutate(self, info, title, content, thumbnail, category, childCategory, tags):

        peed = Peed.objects.create(
            title=title,
            content=content,
            # thumbnail=thumbnail,
            category=Category.objects.get(id=category),
            childCategory=ChildCategory.objects.get(id=childCategory)
        )

        peed.save()

        for i in tags:
            if Tag.objects.filter(name=i).exists():
                tag = Tag.objects.get(name=i)
                peed.add(tag)
            else:
                tag = Tag.objects.create(name=i)
                tag.save()
                peed.add(tag)

        return PeedMutation(peed=peed)


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
    all_peed = graphene.List(PeedType)

    all_category = graphene.List(CategoryType)

    all_tag = graphene.List(TagType)

    all_childCategory = graphene.List(ChildCategoryType)

    peed = graphene.Field(PeedType, id=graphene.Int())

    def resolve_all_peed(self, context, **kwargs):
        return Peed.objects.all()

    def resolve_peed(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Peed.objects.get(pk=id)

        return None

    def resolve_all_portfolioCategory(self, context, **kwargs):
        return Category.objects.all()

    def resolve_all_tag(self, context, **kwargs):
        return Tag.objects.all()

    def resolve_all_childCategory(self, context, **kwargs):
        return ChildCategory.objects.all()


class Mutation(graphene.ObjectType):
    create_peed = PeedMutation.Field()
