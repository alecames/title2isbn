import requests

# this script grabs the ISBN-13 of a book from the Google Books API
# drop a line separated list of book titles in books.txt and run the script

def get_isbn(title):
    r = requests.get("https://www.googleapis.com/books/v1/volumes?q=" + title)
    if r.status_code == 200:
        book = r.json()["items"][0]
        industry_identifiers = book["volumeInfo"]["industryIdentifiers"]
        for identifier in industry_identifiers:
            if identifier["type"] == "ISBN_13":
                isbn = identifier["identifier"]
                title = book["volumeInfo"]["title"]  # get the title from the database
                return isbn, title
        isbn = industry_identifiers[0]["identifier"]
        title = book["volumeInfo"]["title"]  # get the title from the database
        return isbn, title
    else: return "N/A", "N/A"

with open("titles.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    entered_title = line.strip()
    isbn, title = get_isbn(entered_title)
    print(f"{isbn}\t\t{title}")
