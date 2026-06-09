import requests

API_URL = "https://jsonplaceholder.typicode.com/posts/1"


def fetch_post():
    # TODO: Send a GET request to the API URL
    pass


def print_post_summary(data):
    # TODO: Extract and print the title and body from the response data
    pass


if __name__ == "__main__":
    data = fetch_post()
    print_post_summary(data)
