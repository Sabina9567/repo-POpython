pages = 100
rows_per_page = 50
symbols_per_row = 25
symbol_size = 4
disk_size = 1.44

disk_size_bytes = disk_size * 1024 * 1024

book_size_bytes = pages * rows_per_page * symbols_per_row * symbol_size

books_on_disk = disk_size_bytes // book_size_bytes

print(f"На дискете можно поместить {books_on_disk} книг.")