# title2isbn

Fetches ISBNs for a list of book titles, using [Google Books API](https://developers.google.com/books/). Ideal for bulk ISBN lookup.

## How to use
- **Command line:** Add any number of book titles in quotes as command-line arguments. Ex.: `py title2isbn.py "the outsiders" "1984"`
- **Bulk:** Drop any amount of line-separated `.txt` files in the directory then run `py title2isbn.py`.

## Example usage
### Command line
Input:
```bash
$ py title2isbn.py "harry potter philosophers stone" "the c programming language 3rd"
```
Output:
```
9781781100219   Harry Potter and the Philosopher's Stone
9781691352326   The C Programming Language, 3rd Edition
```
### Bulk:
Input `list_of_books.txt`
```
silence of the lamb
harry potter prisoner of azkaban
farenheit 451
the great gatsby
```
Output:
```
9781250048097           The Silence of the Lambs
9781781100516           Harry Potter and the Prisoner of Azkaban
9789756902219           Fahrenheit 451
9780743273565           The Great Gatsby
```
### Note
The selected book might not always be an exact match, but is usually the first result.