# API

## API Design

[API Design]('https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design')

1. What does REST stand for?\
   Representational State Transfer

2. REST APIs are designed around a \_\_\_\_.\
   HTTP

3. What is an identifer of a resource? Give an example.\
   A [URI]('https://en.wikipedia.org/wiki/Uniform_Resource_Identifier') is a uniform resource identifier.

> https://catfact.ninja/fact

4. What are the most common HTTP verbs?\

- GET
- POST
- PUT
- DELETE
- PATCH

5. What should the URIs be based on?\
   The parent service entitiy. This will create a hub that other requests can be branched from.

6. Give an example of a good URI.\

   > https://api.chucknorris.io/jokes/random

7. What does it mean to have a ‘chatty’ web API? Is this a good or a bad thing?\
   Chatty web api's are linked to too many resources and bog down request traffic. This is bad. Keep api's simple and return only what is needed and requested.

8. What status code does a successful GET request return?\
   200

9. What status code does an unsuccessful GET request return?\
   404

10. What status code does a successful POST request return?\
    201

11. What status code does a successful DELETE request return?\
    404

## Regex

[regexr.com]('https://regexr.com/')

How would you match your name using RegEx?

> Regex: Ian Cargill case insensitive:\
> /(ian).(c\w+l{2})/gi

## Things I want to know more about

- API keys and security controls.
- Modular route managment
