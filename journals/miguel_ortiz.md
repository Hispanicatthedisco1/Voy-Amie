### 9/27/2023

- Yesterday we finally started working on the project! I think there were some nervousness about it since a few mistakes were made but all were fixed before the end of the day. We mob programmed to update the docker-compose.yaml file based on the project setup from Learn and what is relative to our project. We chose to work with PostgreSQL and setup Beekeeper to test put db. Created our first MR.
- Had our first standup and I presented what we did yesterday as mentioned above. Today we plan to mob program while we create our table migrations and if we have time we will start working on first endpoints (creating an user, login and logout).
- We actually took turns today creating the tables and we all individually created an issue and MR respectively to the tables we created. We also took turns in testing the new code and approving the merge requests. In total we did 5 MR today, 4 related to tables and 1 for the creating an user as a group.


### 9/28/2023

- Continued to screen share as a group we are working to share the gains and struggles of having JWT auth for the backend. Based on the FastAPI videos and the JWTdown link, we were able to sign in and logout successfuly with a 200 response. As a team we are happy we got this completed before the week long break.
- We had talks about possibly meeting up for a day or two during the break to continue working on the project. 

### 10/3/2023 (Break)

- So we've met for an hour and a half and decided to tackle small portions of the backend but are necessary. We added code in the queries and router directories to display the token when someone logs in.
- Created code to fetch one user by its username. If the user doesn't exist, it gives a "null" response. 
- It might not be much what was worked on but as a group and personally we're happy about the progress. 

### Week of 10/9/2023

- Team updates: 
  -As a group, we have decided it's okay to start working on our individual enpoints. The backend endpoints we're working on individually: 
    - Abe: Trips, Hector: Comments, Juan: Countries, and me (Miguel): Activities. 
    - We also teamed up on how we are going to review and approve MR. Hector and Abe will review each other's code for MR.
    - Juan and I will team up and review each other's code. 
    - After completing some of the backend endpoints for our respective pages, we will have to add a few more tables: friend's and participants. We will divide the work for those tables. Abe and Juan created each different table, respectively. Then Abe and Hector will work on the backend code for friends. 
    - Juan and I are working on the backend code for participants. 


- Personal updates: 
    - I decided to work on the activities backend endpoints and I started with the POST method. Managed to get it reviewed and merged (10/9/2023). 
    - Got the GET ALL method created for activities, it's working as intended, created a MR request for it and got it approved after it was reviewed (10/10/2023). 
    - Was able to get another GET method for activities completed, but this one is for an individual activity (10/10/2023). 
    - Decided to work next on the PUT method for activities. After having it successfully work in the backend, created another MR for it to be reviewed (10/11/2023). 
    - Managed to get another method completed before the end of the day. Got the DELETE method for activities working and MR was approved. (10/11/2023)
    - Realized I didn't have an endpoint protected and decided to create an issue and branch to complete it. I don't expect it to take too long. Got it protected! (10/12/2023)
    - Created the POST method for trip participants. It was reviewd and merged (10/12/2023). I approved Juan's DELETE method for trip participants.
    - Completed the GET ALL method for trip participants (10/13/2023).

### Week of 10/16/2023
- Team updates: 
  - We are ready to start working on the frontend and we plan to do some mob programming for signup and login forms. We are using playground authentication as reference for this files. 
  - We have decided as a team who is working on the frontend. Since each frontend page has different backend components, we aren't necessarily working on the same backend endpoints we personally created.  
  - Abraham has offered to work on deployment since he's a bit ahead from the rest of the group and it was recommended it was worked on before the weekend begins. Other teams are having issues, so hoping we don't (or in this particular moment Abe) doesnt have the same issues as the other teams. While other teams have been working on this for multiple days, Abe was able to do it successfully in one day!!


- Personal updates: 
  - So far all the MR we have completed as a team, the pipelines haven't passed. To avoid too many errors to fix later when the project gets bigger, I asked the team if I can clean up the backend so the lint test passes. Created an issue for this, after multiple attempts, and geting closer each time, finally got the pipelines to pass. (10/16/2023)
  - Decided to tackle the unit test for activities since the checkpoint for this weeks asks/requires that at least one unit test is completed and that it passes. After getting a unit test testing the PUT method for activities, created a MR. (10/17/2023)
  - Created an issue to create a skeleton version of the frontend page so then build up from there. (10/17/2023)


### Week of 10/23/2023

LAST WEEK FOR THE PROJECT!!!!

- Team updates:
  - As of 10/23/2023 we all have completed all of our uni tests and they all pass!!! 
  - Thru advice, it was recommended that we create new table votes and updated a few of other tables. 
  - As a team, we're adding a lot of features and at times having a hard time. Because it's the last week, we're not letting too much time an unresolved problem to go by because we want to make sure we have everything complete by Friday.
  - The team is doing great, a bit stressful, but the job is being completed one step at a time.


- Personal updates: 
    - Added code in the signup form to do a POST for the profile page and have it only associated to the apecified user. Finally got the pages to work after developing some issues and had to create a HMU in the process to get it resolved. (10/25/2023)
    - Started working on the logout button/link for the frontend since the only way to logout was thru the backend. Had a few issues and created a HMU. Apparentaly I needed to move the <Nav > tag under <AuthProvider> to render the logout button and to delete the token in the process. Completed on 10/25/2023 but due to being late for me, worked on the MR Thursday morning. 
    - It was suggested by Abe to have a link on the trip's name of the trip's list on the profile page to redirect you to the trip page based  on the trip_id. (10/26/2023)
    -  NOT GOOD! While testing the frontend, realized something funky was happening. When I update the bio, it places the contents in a different field. Only logging out and logging back in does it show the updated results. Trying to get help but I didn't have this issues two days ago. Can still present but functionality I want everything to work well because my team deserves better.
    - Rosheen was able to help me and the issue was the query. When updating, I had RETURNING * and it should have been RETURNING <typed variable>
    - Will try to do a fetch call of GET to re-render the updated profile page.
    - Hoping for the best!