import doctest

class File:
    def __init__(self, filename: str, contents: str = "", is_open: bool = False):
        """
        Инициализирует файл.

        :param filename: Имя файла.
        :param contents: Содержимое файла (по умолчанию пустое).
        :param is_open: Файл открыт или закрыт (по умолчанию закрыт).

        Примеры:
        >>> file1 = File("my_file.txt")
        >>> file1.filename
        'my_file.txt'
        """

        if not isinstance(filename, str):
            raise TypeError("Имя файла должно быть строкой.")
        self.filename = filename
        self.contents = contents
        self.is_open = is_open

    def open_file(self) -> None:
        """
        Открывает файл.

        :raises Exception: Если файл уже открыт.

        >>> file1 = File("my_file.txt")
        >>> file1.open_file()
        >>> file1.is_open
        True
        """
        if self.is_open:
            raise Exception("Файл уже открыт.")
        self.is_open = True

    def save_file(self, new_contents: str) -> None:
        """
        Сохраняет содержимое в файл.

        :param new_contents: Новое содержимое для файла.
        :raises Exception: Если файл не открыт.

        >>> file1 = File("my_file.txt")
        >>> file1.open_file()
        >>> file1.save_file("New content")
        >>> file1.contents
        'New content'
        """
        if not self.is_open:
            raise Exception("Файл не открыт.")
        self.contents = new_contents

    def close_file(self) -> None:
        """
        Закрывает файл.

        :raises Exception: Если файл уже закрыт.

        >>> file1 = File("my_file.txt")
        >>> file1.open_file()
        >>> file1.close_file()
        >>> file1.is_open
        False
        """
        if self.is_open:
            self.is_open = False
        else:
            raise Exception("Файл уже закрыт.")



if __name__ == "__main__":
    doctest.testmod()