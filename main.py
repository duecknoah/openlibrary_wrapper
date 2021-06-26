from lru import LRUCache
from openlibrary import OpenLibrary

if __name__ == '__main__':
  # Fetch 3 books, print out the length and the contents of the cache each time
  # Use get operations as well
  # Fetch more books

  # The capacity of our cache here is 2, meaning if we fetch 3 books, only
  # the two most recent books will be in the cache while the 1st book will be removed.
  cache = LRUCache(2)
  openL = OpenLibrary()

  print("Attempting to add 3 elements to cache ...\n")
  for isbn in ('9780140328721', '9780517542026', '9781594864889'):
    book = openL.get(isbn)
    cache.set(isbn, book)
    print("cache: {}\nLength: {}".format(cache, len(cache)))

  # If we fetch an element from the cache, it should become in the front of the order:
  print("\nFetching oldest element from cache ...")
  print(cache.getOrder())
  print("Fetched: {}".format(cache.get('9780517542026')))
  print(cache.getOrder())

  # Fetching an invalid ISBN will simply return None (the book doesn't exist)
  print("\nFetching an invalid ISBN (1234567891011) will simply return None (the book doesn't exist)")
  print(openL.get('1234567891011'))