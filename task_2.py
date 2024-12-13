import doctest

class Book:
    def __init__(self, title: str, author: str, pages: int, is_open: bool = False):
        """
        Инициализирует книгу.

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц в книге.
        :param is_open: Является ли книга открытой (по умолчанию закрыта)

        Примеры:
        >>> book = Book("Harry Potter", "J.K. Rowling", 224)
        >>> book.title
        'Harry Potter'
        """
        if not isinstance(title, str) or not title:
            raise TypeError("Название книги должно быть ненулевой строкой.")
        if not isinstance(author, str) or not author:
            raise TypeError("Автор книги должен быть ненулевой строкой.")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self.title = title
        self.author = author
        self.pages = pages
        self.is_open = is_open

    def open_book(self) -> None:
        """
        Открывает книгу.
        Пример:
        >>> book = Book("Harry Potter", "J.K. Rowling", 224)
        >>> book.open_book()
        >>> book.is_open
        True
        """
        self.is_open = True

    def close_book(self) -> None:
        """
        Закрывает книгу.
        Пример:

        >>> book = Book("Harry Potter", "J.K. Rowling", 224, True)
        >>> book.close_book()
        >>> book.is_open
        False
        """
        self.is_open = False


if __name__ == "__main__":
    doctest.testmod()