Step 1: Set Up Postman
Collection Creation: Created a new collection in Postman named "Book API" to organize our requests.

Step 2: Configure Requests
GET Request:
Created a GET request in the "Book API" collection to retrieve all books.
Set the URL to  http://127.0.0.1:8000//books/ and sent the request to test retrieval operations.

POST Request:
Set up a POST request to add a new book.
Configured the request body with book data in JSON format and set the URL to  http://127.0.0.1:8000//books/.
Sent the request to create a new book entry.

PUT Request:
Created a PUT request to update an existing book.
Included the book ID in the URL ( http://127.0.0.1:8000//books/1/) and updated details in the JSON body.
Sent the request to modify the book details.

DELETE Request:
Configured a DELETE request to remove a book using its ID.
Set the URL to  http://127.0.0.1:8000//books/2/ and sent the request to delete the book.

Step 3: Verify Responses
Response Checking: For each request type, checked the responses in Postman to ensure correct status codes and data
returned or modified as expected.