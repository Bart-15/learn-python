import bs4
import requests
import os


def book_title_scrapper():
  '''
  This function get all of the Book title with 4 to 5 star rating and generate a result.txt
  '''

  # Create a url without page number
  basic_url = 'https://books.toscrape.com/catalogue/page-{}.html'

  high_rated_titles = []

  print('-' * 50 + '\n')
  print('Generating result file, please wait...')
  print('-' * 50 + '\n' )

  # check the result file if exists
  if os.path.exists('result.txt'):
    os.remove('result.txt')

  for page in range(1, 51):
    # Create soup on each page

    url_page = basic_url.format(page)
    result = requests.get(url_page)

    soup = bs4.BeautifulSoup(result.text, 'html.parser')

    # Select data of books
    books = soup.select('.product_pod')

    # Iterate books
    for book in books:
      
      if len(book.select('.star-rating.Four')) != 0 or len(book.select('.star-rating.Five')):

        # store title in varable 
        book_title = book.select('a')[1]['title']

        high_rated_titles.append(book_title)

        with open('result.txt', 'a', encoding='utf-8') as file:
          file.write(f'{book_title}\n')

  print('Finished!!')
book_title_scrapper()

