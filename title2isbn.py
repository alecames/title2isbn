import requests

# this script grabs the ISBN-13 of a book from the Google Books API
# drop a line separated list of book titles in book_titles.txt and run the script, include edition if necessary

def get_isbn(title):
	r = requests.get("https://www.googleapis.com/books/v1/volumes?q=" + title)
	if r.status_code == 200:
		book = r.json()["items"][0]
		industry_identifiers = book["volumeInfo"]["industryIdentifiers"]
		for identifier in industry_identifiers:
			if identifier["type"] == "ISBN_13":
				isbn = identifier["identifier"]
				return isbn
		isbn = industry_identifiers[0]["identifier"]
		return isbn
	else: return "N/A"

with open("book_titles.txt", "r") as f:
	lines = f.readlines()

for line in lines:
	title = line.strip()
	isbn = get_isbn(title)
	print(f"{isbn}\t\t{title}")
