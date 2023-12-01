# Book-Display
Here is a README.md you can use for your Streamlit book information app:

```md
# Streamlit Book Info App 

This is a simple book dashboard app built with Streamlit to fetch and display book data using the Google Books API.

## Usage
```
1. Sign up for a Google Books API key
```
https://developers.google.com/books/docs/overview
```
2. Clone this repo

```bash
git clone https://github.com/Vyb-07/Book-Display.git
```

3. Install requirements

```bash
pip install -r requirements.txt  
```

4. Add your Google Books API key to the app code

```python
google_books_api_key = "YOUR_API_KEY"
```

5. Run the app
```bash
streamlit run book_app.py
```

6. Enter a book title in the sidebar to fetch its info

## Features

- Fetch book data from Google Books API including:

  - Title
  - Authors
  - Publisher
  - Published date
  - Preview link
  - Cover image

- User friendly input via Streamlit sidebar
- Error handling for invalid titles

## TODO

- Add book rating, description, genres etc.
- Expand to fetch book reviews
- Allow searching by author name

## Credits

This app uses the [Google Books](https://developers.google.com/books/) API to fetch book data.
```

Let me know if you would like any changes to this README!
