## Project 5 API 
## 1. Purpose of the project: 
- the purpose of the project is to create a endpoint for a social voting website

## 2. User stories:
- as a user i want to create/update/delete a post
- as a user i want to comment on other posts as well as mine
- as a user i want to like a post so i can easly follow the ones i like
- as a user i want to vote on a post
- as a user i want to follow other users
- as a user i want to create/ update my account

## 3. Features: 
- Completed Endpoint API
- the endpoint will recive / create/get/update/delete from the front end as requested
- auth is used as well with tokens for more security
- Comments
    - users can comment/edit on each post
- followrs
    - users can follow other users, might be for there common interests
- like
    - users can like a post like a favourite website
    - easy to find your liked posts
- posts
    - posts can be created/updated and deleted
    - posts are for comparing if a product is like its advert
- vote
    - users can vote on a post being alike the advert or not alike
- profiles
    - user can have a name and profile image

## 4. Future features
- there can be more improvemtns on the code so this would be a good start
- more apps can be added as the site becomes more, such as most liked of the day

## 5. Typography and color scheme

## 7. Technology
- Frameworks
    - Django is the main framework [Django](https://www.djangoproject.com/)
    - Django-Rest is the main framework [Django-rest](https://www.django-rest-framework.org/)
    - Bootstrap for the HTML and CSS [Bootstrap](https://getbootstrap.com/)
- storage
    - cloudinary for media storage [cloudinary](https://cloudinary.com/)
- Database
    - elephantsql for the database [elephantsql](https://customer.elephantsql.com/)

## 8. testing
- Agile 
    - basic functions setup, then more complexion added, like auth
    - more functions that can be updated/created by users 

- code validation
    - CSS validation [CSS](https://jigsaw.w3.org/css-validator/validator)
    - HTML validation [HTML](https://validator.w3.org/)
    - Python validation using [Python](https://pythontutor.com/python-debugger.html#mode=edit)
    - Spellchecker [Online Spellchecker](https://www.online-spellcheck.com/)

- automation testing
    - 


- test cases (user story based)
    - Profile
        - Create
        - Update
    - Vote
        - Create
        - Delete 
    - Post
        - Create
        - Update
        - Delete
    - Commnet
        - Create
        - Update
        - Update 
    - Like
        - Create
        - Delete
    - Follow
        - Create
        - Delete 

- supported screens and browsers
    - Chrome
    - Edge
    - Chrome mobile / samsung

## 9. Deployment
   - Heroku
    - Deployment from heroku >> create app > setup enviroment vairables > deploy project > link to github repository
   
- gitpod to github
   - Deployment from gitpod was done by adding changes to the python3 command line.
   - git add .
   - git commit -m "changes in here"
   - git push
   - to run the server from gitpod type python3 manage.py runserver

## 10. Credits

- This project took many ideas and code layout as i needed the same functonaltiy from the django rest famework mini project
