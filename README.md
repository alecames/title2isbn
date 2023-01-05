# title2isbn

Fetches ISBNs for a list of book titles, using [Google Books API](https://developers.google.com/books/). Ideal for bulk ISBN lookup.

## How to use
- Drop a line-separated list of book titles in `titles.txt`
- Run the script with `py title2isbn.py` 

## Example
Input `titles.txt`:
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