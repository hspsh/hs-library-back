from graphene_django import DjangoObjectType
import graphene

from books.models import Book


from graphene_django import DjangoObjectType
import graphene


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class Query(graphene.ObjectType):
    books = graphene.List(BookType)

    def resolve_books(self, info):
        return Book.objects.all()


schema = graphene.Schema(query=Query)