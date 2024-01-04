# main_script.py
from http_request import main

def run_http_request():
    print("Calling http_request.main from main_script")
    main()

if __name__ == "__main__":
    run_http_request()
