import requests

"""A wrapper for accessing book data from the openlibrary API
"""
class OpenLibrary(object):

  def __init__(self):
    super().__init__()

  def get(self, isbn):
    """Fetch book data (title, authors, languages) from the open library API and return it in a
    dict, None if unable to fetch
    :rtype dict
    """
    path = "https://openlibrary.org/api/books?bibkeys=ISBN:{}&jscmd=details&format=json".format(isbn)
    resp = requests.get(path)

    if (resp.ok):
      json = resp.json()

      # If invalid ISBN, we get {} as a response, simply return None
      if not json:
        return None

      bookData = json[list(json)[0]]['details'] # get first key value, as that has all book info
      finalData = dict()
      finalData['title'] = bookData['title']

      # Convert authors array of objects to a single string listing the
      # authors
      authors = ""
      for i, author in enumerate(bookData['authors']):
        if i > 0:
          authors += ", "
        authors += author['name']
      finalData['authors'] = authors

      # Language data is stored like:
      # [{"key": "/languages/rus"}]
      # we want to extract "rus"
      languages = ""
      for i, lang in enumerate(bookData['languages']):
        if i > 0:
          languages += ", "
        languages += lang['key'][11:]
      finalData['languages'] = languages

      return finalData
    return None