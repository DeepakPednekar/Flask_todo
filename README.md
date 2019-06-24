## This is backend code for TODO app

- this is a rest api using Flask framework in python
- we can learn how to use blueprints, jwt token, sqlalchemy, migrations and so on


## How to use this api
- You need to get token from /auth where you need to pass username and password
- Then you need to add this token value in HTTP Authorization header (see example below)
  for all requested urls
- example suppose you want to fetch all users for test. This is not real life example.

    > Note:- don't let users to fetch another users. This is for now.
      assuming you are using Linux system where curl client is installed. 
      If you want to learn about curl please see https://curl.haxx.se/docs/

    request :- ```curl -H 'Content-Type:application/json' localhost:5000/auth -d '{"username":<yourvalue>, "password":<secret>}'```
    
    respones:- 
    On success you'll get
    
        HTTP/1.1 200 OK
        Content-Type: application/json

        {
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwiaWF0IjoxNDQ0OTE3NjQwLCJuYmYiOjE0NDQ5MTc2NDAsImV4cCI6MTQ0NDkxNzk0MH0.KPmI6WSjRjlpzecPvs3q_T3cJQvAgJvaQAPtk1abC_E"
        }

    __now your request__

    request :- ```curl -H 'Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwiaWF0IjoxNDQ0OTE3NjQwLCJuYmYiOjE0NDQ5MTc2NDAsImV4cCI6MTQ0NDkxNzk0MH0.KPmI6WSjRjlpzecPvs3q_T3cJQvAgJvaQAPtk1abC_E' localhost:5000/user```

    response :- you will get json response with users
