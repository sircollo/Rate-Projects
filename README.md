# Projects Rater
## Author
[Collins Sirwani](https://github.com/sircollo)

## Description
This is an application that allows a user to post a project he/she has created and get it reviewed by his/her peers. The project utilizes django rest framework API with Projects and Profile endpoints.

### Prerequisites
You need to install the following:
```
  Django - 4.0.4
  Virtual Environment
```

### Installation
```
  -Git clone https://github.com/sircollo/Rate-Projects

  -cd Rate-Projects

  -install virtual env

  -pip install -r requirements.txt

  -python3.8 manage.py runserver

```
## Technologies Used

  * Python3.8
  * Django 4.0.4
  * Bootstrap
  * PostgreSQL
  * CSS
  * Heroku

## Running tests
```
  -python3.8 manage.py test projectsapp
```

## User Story
A user can:

  * View posted projects and their details.
  * Post a project to be rated/reviewed.
  * Rate/ review other users' projects.
  * Search for projects.
  * View projects overall score.
  * View his/her profile page


## BDD
Feature: Test add new user to database

Scenario: A new user can input registration details and login using the details

  Given I am a new user and on the register page

  When I add my user information and click 'Sign Up' button

  Then I am redirected to login page

  Then I input my login details

  Then I click sign in

  Then I can use the application

### Deployment
Read here on how to [Deploy](https://gist.github.com/newtonkiragu/42f2500e56d9c2375a087233587eddd0)


### Preview

[Live Link](https://ratemyprojects.herokuapp.com/)


### License

[MIT License](https://github.com/sircollo/Rate-Projects/blob/master/LICENSE)

Copyright (c) 2022 Collins Sirwani
