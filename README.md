Project URLS:

  Backend Deployment:
    https://jun-8-pt-voyamieapi.mod3projects.com/docs#/

  Frontend Deployment:
    https://vacationeers.gitlab.io/voy-amie

  Gitlab:
    https://gitlab.com/vacationeers/voy-amie


Members:

  Abraham Gebreselassie: Trips Page, Trips API, Friends API
  Hector Elias: Create Trip Form Page, Make Participant Page, Add Friends Page, Comments API
  Juan Chavez: Trip Final Page, Country API, Participants API,
  Miguel Ortiz: Profile Page, Activities API, Participants API


Description:

  Have you ever tried organizing a trip with a friend or multiple friends? If you have, then you will understand the headache that comes with trying to get everything organized and planned. Luckily Voy-Amie is here to assist you; Users of Voy-Amie can create a trip, add friends and vote to decide what activities to partake in.

  When a user creates a trip, they have the ability to give it a name, select the destination and select the time and dates. After, the creator of the trip can add friends to be able to begin coordinating. Users can then begin to suggest trip activities to partake in, this would include the activity title, location of the activity as well as the date and the time.

  Once the trip has been created and activities have been suggested, users that are part of the trip have the ability to vote on the activities, with a simple majority a trip is approved and sent to the final itinerary that displays all the finalized activities that can be sorted by date.


How to Run on Local Device:

  1. Open your terminal and CD into your desired directory
  2. Clone repository grab link and type the following command into your terminal "Git clone https://gitlab.com/vacationeers/voy-amie.git"
  3. CD into Voy-Amie
  4. Install Docker through the following Commands
      docker volume create postgres-data
      docker volume create beta-data
      docker-compose build
      docker-compose up
  5. With Docker up and running, in your browser go to http://localhost:8000/docs to view the FastAPI backend endpoints
  6. With Docker up and running, in your browser go to http://localhost:3000 to view the project, navigate using the navbar

Design:

  Voy-Amie's Backend is build on FastAPI and a PostreSQL Database, the Front end consists of React and JSX for stylization.
## Design
![1.PNG](1.PNG)
![cruds](cruds.png)
![API's.PNG](API's.PNG)
![Models.PNG](Models.PNG)
![pages.PNG](Pages.PNG)
## Service Microservice


Voy-Amie Overview:
  The following Files and Folders are available within the Voy-Amie project.

    -Requirements.txt:
      A file that tells the Dockerfile what it needs to install on boot.

    -Main.py:
      Connects the FastAPI system to our routers.

    -Dockerfile:
      Allows the docker system to load and run all required information as well as run the systems through appropriate ports.

    -Migrations:
      Within this folder lies 002_table_migrations.py that allows us to determine and store all of our objects and tables into the database.

    -Queries:
      This file is the location of the pydantic models for our objects. A file is dedicated to each of our objects.

    -Routers:
      Allows us to route the paths of our objects we want to create to communicate with the database.
      Router files and Queries files work together to make sure information is being stored and sent back and forth when called.

## Frontend Description

  - Create Trip:
    In this page, the logged in user is able to input data into a form to create a trip. The data they input is Trip Name, the Destination's City and Country (a dropdown selection), and Start and End dates for the trip. Once filled out, the user clicks on the submission button and is guided back to their profile page. They will be able to see the trip they just created in the Trips List with its information.

  - Make Participant:
    This page is only accessible to a trip's planner. The planner will be able to see a button in the Trip's Detail page that upon click will direct them to the page where they will be shown a list of their friends and a list of existing trip participants. The friends list will only show friends that are not yet participants to the current trip with a button on each friend row that upon clicking will make them a participant. This functionality will dynamically remove them from the friends list, then add them to the Participants list below. A similar functionality happens when the button next ot a participant's name is clicked. It removes them as a participant and they are again displayed on the friends list.

  - Add Friends Page:
    This feature's page is accessible by clicking the 'Add Friend' button on any logged in user's profile page. This directs them to the page that displays a search bar. The user is to type in the username of a fellow existing user that they want to befriend. The dynamic search bar starts to populate a list of users whose username includes what the current user is typing within the search bar.
