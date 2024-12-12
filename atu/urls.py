from django.urls import path
from.import views

urlpatterns = [
    path('' , views.home),
    path('book_list/' , views.book_list ,name="book_list"),
    path('posts/' , views.post_list),
    path("add_book/" ,views.add_book),
    path('book/<int:pk>/' , views.book_detail , name="book_detail"),
    path('book_update/<int:pk>', views.book_update , name = 'book_update'),
    path('book_delete/<int:pk>', views.book_delete , name = 'book_delete')
]