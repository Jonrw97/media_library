# TODO
## PHASE 1

Use Flask and simple direct dbm libary to persist the data

https://miro.com/app/board/uXjVOFF2cpg=/?utm_source=notification&utm_medium=email&utm_campaign=daily-updates&utm_content=go-to-board

- [x] Login Screen
- [x] Create Movies table, Actors table, Users table
- [x] Test data script
- [x] Main Libary View
- [x] Detail view
- [x] Edit view - add (without actors)
- [x] Edit View - edit
- [x] Sync Folder File Lister
- [x] Video Player View (HTML5 video player)
- [x] Make Sure Every Page Checks the user is logged in 
- [x] Base layout
- [x] Use 2 Flask Blueprints
- [x] Edit movie view - to include actors for editing
- [x] edit actor and delete actor
- [x] add actor
- [x] dont install passwords in plain text

## PHASE 2

- [ ] Refactor Flask controller to have no dependencies on db.py i.e. introduce a data access layer
  - [x] Part 1: move all logic into movies_das
  - [x] Part 1: implement all file services in file_media_service
  - [x] Handle exception in media service
  - [x] Implement a common return pattern from the das layer (i.e. result, error, etc) 
  - [ ] Part 2: refactor to use the single methods to handle movie + actor updates in one go - 
        so think about how you would pass the movie and actors in one method call and ensure that they are all 
        committed in one go
- [ ] Use WTForm / with validations - https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/
- [ ] Introduce Flask form validation
- [ ] Handle child objects (actors) - using WTForm 'field enclosures' to create repeated fields
- [ ] Flask tests,  add movie, render libary page, edit view
- [ ] CSRF
- [ ] documents

## PHASE - feature ideas
- [ ] Introduce a services layer
- [ ] From the services layer connect to IMDB to pull down movie and actor information

## PHASE 3

- [ ] Change the relationship between actors and movies so that actors can be in multiple movies
- [ ] add and actors management module to the UI
- [ ] documents

## PHASE 4

- [ ] Deploy to home server by installing python, virtual enviroment, flask and run flask on the server
- [ ] Securing the web application
- [ ] documents

## PHASE 5 - Django?

- [ ] implement python models for entities (movie, actor, user)
- [ ] Use Flask forms with models 
- [ ] Use an ORM
- [ ] documents







## PHASE 6

- [ ] HTML CSS design using flexbox layout
- [ ] add some javasript interactivity TBD
- [ ] documents


## PHASE X

- [ ] Deploy to server
  - [ ] Introduction to GitHub actions to deploy
- [ ] Profile management register user edit user
- [x] dont install passwords in plain text for all users
- [ ] Auto find new files in the sync folder
- [ ] look up file meta data on api
- [ ] upload the cover image file
- [ ] documents
