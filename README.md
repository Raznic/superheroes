Super Hero API
--------------

### Table of Contents

* [Purpose](#purpose)
* [Getting Started](#getting-started)
* [Swagger](#swagger)
  * [Authentication](#authentication)
* [Keycloak](#keycloak)
  * [Importing Clients](#importing-clients)
* [Testing](#testing)

### Purpose

This is a RESTful API written in Django + Django REST Framework for managing super heroes. It is meant to showcase 
several different concepts with the aforementioned frameworks, including:

* Storing information using database models.
* Validating and de-serializing request data.
* Serializing objects into JSON data.
* Filtering lists of resources based on request query parameters.
* Defining fixtures for seeding development/test data.
* Writing basic unit/integration tests.
* Using a third-party identity provider for authentication.
* Enforcing permissions to restrict what actions users may take.
* Documenting a RESTful API using Swagger.
* Versioning an API to allow for future breaking changes.


### Getting Started

The following steps detail how to get this project running in your own environment.

1. Clone the project and switch to the root project directory.
2. Install package requirements.
   ```bash
   $ pip install -r requirements.txt
   ```
3. Use Docker Compose to spin up additional services required for using the project. This includes a Keycloak server 
for managing identities.
   ```bash
   $ docker-compose up -d
   ```
4. Import any required clients. See [Importing Clients](#importing-clients) for more details.
5. Run the server:
   ```bash
   $ python manage.py runserver
   ```
6. Open a browser and navigate to http://localhost:8000/api/v1/swagger/.


### Swagger

Swagger is a tool for documenting and testing RESTful APIs. Any unauthenticated user should be able to view all of 
the available endpoints in Swagger, as well as the request/response models. Most GET requests do not require any kind
 of authentication. All POST/PUT/PATCH/DELETE and some GET requests, however, do require users to be authenticated.
 
 #### Authentication
 
Follow these steps to authenticate Swagger requests:
 
1. Click the **Authorize** button at the top of the Swagger UI.
2. Check the box next to the `profile:email` scope.
3. Click **Authorize**.
4. Click **Close**.


### Keycloak

This project uses a Keycloak server for managing user identities and performing authentication.

#### Importing Clients

1. Open a browser and navigate to the Keycloak server (http://localhost:8080). Log in using the default credentials.
   ```
   username: Batman
   password: 1DarkKnight
   ```
2. An OpenID Connect client has already been configured for Keycloak, but needs to be imported.
3. Click the **Clients** menu item in the left-hand panel.
4. Click the **Create** button in the upper-right of the Clients page.
5. Click the **Select file** button next to Import to locate the client JSON config.
6. Select the **super-hero-swagger.json** file in the root of the project folder.
7. Click **Save**.


### Testing

Use the following command to run test cases for the project.
```bash
$ python manage.py test
```
