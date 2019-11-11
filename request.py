"""REQUEST CLI TOOL

Usage:
    request.py
    request.py <url>
    request.py <method> <url> [--header|--body]
    request.py <method> <protocol> <url> [--header|--body]
    request.py <method> <url> <params> [--header|--body]
    request.py <method> <protocol> <url> <params> [--header|--body]
    request.py -h|--help
    request.py -v|--version

Options:
    <url>  Url argument in "example.com" format.
    <method> Optional http method argument.  Default is 'GET'.
    <params> Optional query parameter argument.
    <protocol> Option protocol argument.  Default is 'http'
    --header Print only header of the http response.
    --body Print only body of the http response.
    -h --help  Show this screen.
    -v --version  Show version.



"""

import requests
from uri_builder import Uri
from docopt import docopt


def main():
    arguments = docopt(__doc__, version='1.0')
    if arguments['<method>'] == 'POST':
        post_data()

    url = get_url(arguments)
    response = get_response(url)
    if arguments['--header']:
        print_response_header(response)
    elif arguments['--body']:
        print_response_body(response)
    else:
        print_response_header(response)
        print_response_body(response)



# Builder method for URLs
def build_url(scheme=None, host=None, path=None, params=None, fragment=None):
    url = Uri.new().with_scheme(scheme).with_host(host).with_path(path).to_uri()
    return url.to_string()


def get_url(arguments):
    url = ''
    if arguments['<protocol>']:
        url = build_url(scheme=arguments['<protocol>'], host=arguments['<url>'])
    elif arguments['<url>']:
        url = build_url(scheme='http', host=arguments['<url>'])
    return url


def get_response(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return "Something went wrong with request"
        return response
    except requests.exceptions.ConnectionError:
        print("Invalid URL")


# Return only the headers of http response.
def print_response_header(response):
    headers = response.headers
    for k, v in headers.items():
        print(f'{k}: {v}')
    return


# Return only the body of http response.
def print_response_body(response):
    text = response.text
    print(text)
    return


# Unfinished POST method.  To do:  build json post request with user input.  Return response.
def post_data():
    data = {}
    key = input("Enter field: ")
    value = input("Enter data: ")
    data[key] = value
    print(data[key])





if __name__ == '__main__':
    main()