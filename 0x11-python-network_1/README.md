# Python - Network #1

## Objectives

In the end, you will learn how to:

* How to fetch internet resources with the Python package urllib
* How to decode urllib body response
* How to use the Python package requests #requestsiswaysimplerthanurllib
* How to make HTTP GET request
* How to make HTTP POST/PUT/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service

## Tasks
1. **[What's my status? #0](./0-hbtn_status.py)**
    - Write a Python script that fetches https://alx-intranet.hbtn.io/status

2. **[Response header value #0](./1-hbtn_header.py)**
    - Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.

3. **[POST an email #0](./2-post_email.py)**
    - Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`).

4. **[Error code #0](./3-error_code.py)**
    - Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).

5. **[What's my status? #1](./4-hbtn_status.py)**
    - Write a Python script that fetches https://alx-intranet.hbtn.io/status

6. **[Response header value #1](./5-hbtn_header.py)**
    - Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header.
 
7. **[POST an email #1](./6-post_email.py)**
    - Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
 
8. **[Error code #1](./7-error_code.py)**
    - Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

9. **[Search API](./8-json_api.py)**
    - Write a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.

10. **[My GitHub!](./10-my_github.py)**
    - Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id.

11. **[Time for an interview!](./100-github_commits.py)**
    - The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:

            `Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
            You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
            Print all commits by: ``<sha>: <author name>`` (one by line)`
    
    - Write a Python script that takes 2 arguments in order to solve this challenge.
