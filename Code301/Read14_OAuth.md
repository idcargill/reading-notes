# OAuth

[OAuth](https://www.csoonline.com/article/3216404/what-is-oauth-how-the-open-authorization-framework-works.html)

1. What is OAuth?\
   A standard for authorization protocol for unrelated servers to allow authentication without sharing single logon credentials.

2. Give an example of what using OAuth would look like.\
   A website that allows for multiple forms of log in account.

3. How does OAuth work? What are the steps that it takes to authenticate the user?

- The first site connects to the second, providing the users identity.
- The second site generates a token and secret key.
- The client presents the token to their authorization provider.
- The user or software approve a transaction on the first site.
- The user is given and access token.
- Token is given to the first website.
- The first site gives the token to the second site as proof of authentication.
- The second site grants permission based on the token provided.

4. What is OpenID?\
   An authentication protocol. For humans proving authentication to a computer.

[AuthO Documentation](https://auth0.com/docs/authorization/flows)

1. What is the difference between authorization and authentication?\
   Authentication is for proving identity, authentication is for allowing access/permissions.

2. What is Authorization Code Flow?\
   The code flow from the user to the main app, to the AuthO Tenant, and app server api to validate the authentication of the user token.

3. What is Authorization Code Flow with Proof Key for Code Exchange (PKCE)?\
   An extra layer of protection for public applications by calling on an authorization server to request the access token from the AuthO provider.

4. What is Implicit Flow with Form Post?\
   A less secure public authorization code flow that should only be used with ID tokens.

5. What is Client Credentials Flow?\
   A machine to machine authorization when standard user name / password combinations are not applicable.

6. What is Device Authorization Flow?\
   The use of another user's device to provide authentication. Similar to 2 part authentication, designed for devices with poor input interfaces.

7. What is Resource Owner Password Flow?\
   AuthO Tenant directly asks for user input for password and id. Not recommended unless the site is trusted.

## Things I want to know more about

All of it. How to implement OAuth in front end and how to secure back end apis.
