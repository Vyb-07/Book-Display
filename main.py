import streamlit as st
import requests

# Set page title
st.title("Book Information Dashboard")

# Sidebar for user input
st.sidebar.header("User Input")
book_title = st.sidebar.text_input("Enter Book Title", "The Great Gatsby")

# Fetch book data from Google Books API
if book_title:
    google_books_api_key = "AIzaSyAsDmXcRRcZTKUNnn-WDoGqIzsZDFPI7iQ"  # Replace with your Google Books API key
    books_url = f"https://www.googleapis.com/books/v1/volumes?q={book_title}&key={google_books_api_key}"
    response = requests.get(books_url)

    if response.status_code == 200:
        book_data = response.json()

        # Display book information
        st.subheader(f"Book Information for '{book_title}'")

        for item in book_data.get("items", []):
            volume_info = item.get("volumeInfo", {})
            st.write(f"Title: {volume_info.get('title', 'N/A')}")
            st.write(f"Authors: {', '.join(volume_info.get('authors', ['N/A']))}")
            st.write(f"Publisher: {volume_info.get('publisher', 'N/A')}")
            st.write(f"Published Date: {volume_info.get('publishedDate', 'N/A')}")
            st.write(f"link: {volume_info.get('previewLink', 'N/A')}")
            st.image(volume_info.get('imageLinks', {}).get('thumbnail', ''), caption="Book Cover", use_column_width=True)

    else:
        st.error(f"Failed to fetch book data. Status code: {response.status_code}")
else:
    st.warning("Enter a book title in the sidebar.")

