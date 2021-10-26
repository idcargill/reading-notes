# CRUD

[HTTP CRUD Codes](https://www.moesif.com/blog/technical/api-design/Which-HTTP-Status-Code-To-Use-For-Every-CRUD-App/)

1. In your own words, describe what each group of status code represents:\
   100’s = Informational. Request has been received but something else might be required.\
   200’s = Successful http transaction completed.\
   300’s = Redirection codes, if a target URL has moved\
   400’s = Client Error: There is an error in the http request from the client.\
   500’s = Server Error: The server was unable to complete the request.\

2. What is a status code 202?\
   An asynchronous processing request has been received, but may not be finished.

3. What is a status code 308?\
   A permanent redirect.

4. What code would you use if an update didn’t return data to a client?\
   204

5. What code would you use if a resource used to exist but no longer does?\
   410

6. What is the ‘Forbidden’ status code?\
   The client does not have permission to perform the requested actions.

[Node API -WebDev](https://www.youtube.com/channel/UCFbNIlppjAuEX4znoulh0Cw)

1. Why do we need to pull our MongoDB database string out of our server and put it into our .env?\
   To protect the connection location for our database once deployed.

2. What is middleware?\
   Middle ware is software the runs on the server after a request and before a response is sent.

3. What does app.use(express.json()) do?\
   Allows express to accept JSON file formats.

4. What does the /:id mean in a route?\
   The id is a route parameter sent in the request.

5. What is the difference between PUT and PATCH?\
   PUT updates all information, PATCH updates only the information passed.

6. How do you make a default value in a schema?\
   Set a default value in the model definition.

7. What does a 500 error status code mean?\
   Server Error.

8. What is the difference between a status 200 and a status 201?\

- 200 A request was successful
- 201 A new object was created successfully.

## Things I want to know more about

- API security
