# http_request.py
import requests

def main():
    url = "https://rickandmortyapi.com/"
    
    # Make the HTTP request
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the HTML response
        print(response.text)
    else:
        print(f"Error: Unable to fetch the page. Status code: {response.status_code}")

if __name__ == "__main__":
    main()
