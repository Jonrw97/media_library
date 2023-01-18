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

- [x] Refactor Flask controller to have no dependencies on db.py i.e. introduce a data access layer
  - [x] Part 1: move all logic into movies_das
  - [x] Part 1: implement all file services in file_media_service
  - [x] Handle exception in media service
  - [x] Implement a common return pattern from the das layer (i.e. result, error, etc)
  - [x] Part 2: refactor to use the single methods to handle movie + actor updates in one go -
        so think about how you would pass the movie and actors in one method call and ensure that they are all
        committed in one go
- [x] Use WTForm / with validations - https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/
- [x] Handle child objects (actors) - using WTForm 'field enclosures' to create repeated fields

- [ ] CSRF
- [ ] documents

## PHASE

- [x] introduce bootstrap for new layout
- [x] video hosting
- [x] create landing page with html 5 video player and poster
- [x] use bootstrap and a bootstrap theme
- [x] add property video location
- [x] contact form with Captcha

## PHASE

- [x] link to the admin screen(list videos and edit details)
- [x] add new fields to movie (released at, description, location, movie type(public, private) )
- [x] upload video to (Binary Large OBject) storage !Richard's AWS Account!
- [x] fitler the fields by movie type(personal: title, released at, description, location other: all fields)
- [x] landing show one featured video and order others by date filmed
- [x] video upload change to url
- [ ] add enum for hosting type
- [x] add flag coloum for publishing
- [ ] Flask tests, setup a movie with a fixture, render the edit page, update the movie title check title correct
- [ ] Flask test, go to the edit page for the same movie, leave title blank save check validation error
- [ ] acces admin edit page without being logged in
- [ ] run tests auto on push(ci/cd)
- [x] use postgres instead of sqlite

## PHASE Tags And Searching with ORM

- [ ] add models to support tags
- [ ] update ui to attached a tag to a predefined list
- [ ] create search function to show tags on a click show all relevant videos
- [ ] create a search function which searches within the fields of movies

## PHASE random ideas for Jons portfolio

- [ ] multiple resolutions of videos
- [ ] own video player controls
- [ ] mailchimp mailing list notify new videos

## PHASE

- [ ] Change the relationship between actors and movies so that actors can be in multiple movies
- [ ] add and actors management module to the UI
- [ ] documents

## PHASE - Django?

- [ ] implement python models for entities (movie, actor, user)
- [ ] Use Flask forms with models
- [ ] Use an ORM
- [ ] Introduce migration(Alter tables add coloums)
- [ ] documents

## PHASE X

- [ ] Deploy to server
  - [ ] Introduction to GitHub actions to deploy
- [ ] Profile management register user edit user
- [x] dont install passwords in plain text for all users
- [ ] Auto find new files in the sync folder
- [ ] look up file meta data on api
- [ ] upload the cover image file
- [ ] Deploy to home server by installing python, virtual enviroment, flask and run flask on the server
- [ ] Introduce a services layer
- [ ] From the services layer connect to IMDB to pull down movie and actor information
- [ ] Populate media libary
- [ ] documents

## PHASE Z

- [ ]Build own video controls with javascript and css
- [ ]Profile themes with bootstrap
