# notes for useful commands and tips

## HTTP Status Response Codes

- 2xx Success
- 3xx Redirections
- 4xx Client Error
    - 404 Not Found
- 5xx Server Error
    - 500 Internal Server Error

## Restful APIs

    - a base URI https://ex.com/api
    - HTTP methods (GET, POST, PUT, PATCH and DELETE)
    - is stateless, like HTTP
        - stateless: every cycle (HTTP request, Retrieve Data) is completely independent of what happened in the cycle before (no memory). e.g. authentication, every time we need to authenticate ourselves (send authentication signature with request).
    - includes media type to define state transition data elements (JSON)

## Project Details

- Build Login facility in React JS, we are going to store the session (or state) in the react application.
- if not, everytime we make a request, we have to login again and again.