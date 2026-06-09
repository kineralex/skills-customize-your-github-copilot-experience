# 📘 Assignment: Consume a Public API with Python

## 🎯 Objective

Learn how to use Python to request data from a public API, parse JSON responses, and present the information in a simple, readable way.

## 📝 Tasks

### 🛠️ Make a Request to an API

#### Description
Use the `requests` library to send a GET request to a public API endpoint and print the response.

#### Requirements
Completed program should:

- Import the `requests` library
- Send a request to a public API endpoint such as `https://jsonplaceholder.typicode.com/posts/1`
- Print the response status code and the response body

### 🛠️ Extract Data from JSON

#### Description
Convert the API response into Python data and extract specific values.

#### Requirements
Completed program should:

- Use `response.json()` to parse the response
- Print at least one field such as the title or body
- Display the data in a clean format for the user

### 🛠️ Handle Errors Gracefully

#### Description
Add basic error handling so the program responds nicely if the request fails.

#### Requirements
Completed program should:

- Catch `requests.exceptions.RequestException`
- Print a friendly message when the request fails
- Exit cleanly instead of crashing
