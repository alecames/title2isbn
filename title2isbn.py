import requests
import glob
import sys

# this script grabs the ISBN-13 of a book from the Google Books API
# drop a line separated list of book titles in a .txt file in the same directory as the script, name not important
# alternatively, pass the titles as arguments to the script, encase in quotes and separate with a space

def get_isbn(title):
    r = requests.get("https://www.googleapis.com/books/v1/volumes?q=" + title)
    if r.status_code == 200:
        book = r.json()["items"][0]
        industry_identifiers = book["volumeInfo"]["industryIdentifiers"]
        for identifier in industry_identifiers:
            if identifier["type"] == "ISBN_13":
                isbn = identifier["identifier"]
                title = book["volumeInfo"]["title"]
                return isbn, title
        isbn = industry_identifiers[0]["identifier"]
        title = book["volumeInfo"]["title"]
        return isbn, title
    else: return "N/A", "N/A"

def read_from_file():
    my_files = glob.glob('*.txt')
    for file in my_files:
        print(f"File: {file}")
        with open(file, 'r') as f:
            titles = f.readlines()
        for line in titles:
            entered_title = line.strip()
            print_result(entered_title)
        print()

def read_from_args():
    titles = sys.argv[1:]
    for title in titles:
        print_result(title)

def print_result(title):
    isbn, title = get_isbn(title)
    print(f"{isbn}\t{title}")

print("------ Results ------\nISBN\t\tTitle\n----            -----")
if len(sys.argv) > 1: read_from_args()
else: read_from_file()