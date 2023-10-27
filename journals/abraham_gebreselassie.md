## Date 10-26-2023

### Today I worked on:

### I worked resolving the 404 error we had on deployed website, that issue was resolved through adding a script in the .gitlab-ci.yml file. Worked on authorization for the trip detail page, in that only a planner or participant of that trip can view the page.

**AH-HA!💡**

**🎉 Celebrations 🎉**

### Bugs encountered 🐛🐞🐜 :

### 404 error

🪲

### I worked on the 404 issue

**\~Solution~**

### and the issue was an issue with gitlab pages as it had to do with the fact it is a static page, but we are creating SPAs and so we added the script "echo "/\* /index.html 200" > build/\_redirects" which rewrites the urls to return the index.html and 200 status code by putting the redirects file in our deployed directory and this fixed the issue with the 404 errors.

### References Used Today:

###

### Any Blockers:

### No blockers today

### Tomorrow I'm working on:

### I will ensuring the deployed site is working as intended and fix any bugs we discover in our deployed website.

### References for Tomorrow:

## Date 10-25-2023

### Today I worked on:

### I worked on changing the activity status to finalized based on vote count being greater or equal to 50% of the total amount of participants. I was successful in doing this. I worked on our deployed website and encountered a bug in that when a 'post' happened I was creating was giving a CORS error and a resource error that we were trying to access http resource while on a https website.

**AH-HA!💡**

**🎉 Celebrations 🎉**

### Bugs encountered 🐛🐞🐜 :

### CORS bug, 404 error

🪲

### I worked on our deployed website and encountered a bug in that when a 'post' happened I was creating was giving a CORS error and a resource error that we were trying to access http resource while on a https website. The other bug with 404 errors on pages we were still getting the content that was intended.

**\~Solution~**

### The issue was the same issue that others had dealt with and the solution was to remove trailing slashes in our api calls on the frontend as this was causing the issue and once those slashes were removed the issue was resolved.

### References Used Today:

###

### Any Blockers:

### No blockers today

### Tomorrow I'm working on:

### I will ensuring the deployed site is working as intended by fixing the 404 error we are getting on the deployed website.

### References for Tomorrow:

## Date 10-24-2023

### Today I worked on:

### We started working on creating endpoints for the votes table and also creating the votes table. I created the 'delete' and 'get' endpoints for votes so that a user can delete a vote and also get all votes.

**AH-HA!💡**

**🎉 Celebrations 🎉**

### Bugs encountered 🐛🐞🐜 :

### I had a bug in which i was trouble with not allowing a user to vote twice.

🪲

### No bugs today

**\~Solution~**

### I ended up just removing the button if they had already voted on a activity, which involved checking the list of votes on acitivies a user has placed and if the activity was there it would disable the button.

### References Used Today:

###

### Any Blockers:

### No blockers today

### Tomorrow I'm working on:

### I will ensuring the deployed site is working as intended.

### References for Tomorrow:

## Date 10-23-2023

### Today I worked on:

### I worked on unit test for the trips routers/queries so that we can ensure that the router to get_all trips is working as intended. I also started to work on changing the status of an activity based on the vote count.

**AH-HA!💡**

**🎉 Celebrations 🎉**

### Bugs encountered 🐛🐞🐜 :

### Yes, I did have a bug

🪲

### We realized that we wanted to record you voted and prevent them from voting again, but we realized it is not possible to record and save that information on the frontend.

**\~Solution~**

### A potential solution would be to record a vote on the backend and check against that in the front end where if a user has already voted on an activity it won't allow them to vote again.

### References Used Today:

###

### Any Blockers:

### Yes, with the preventing a second vote and changing the status of an activity to finalized.

### Tomorrow I'm working on:

### I will be working on allowing a user to go to a particular trip.

### References for Tomorrow:

## Date 10-19-2023

### Today I worked on:

### Today, I worked on incorporating useParams into my tripdetail page so that a user can navigate between different trips they have created. I also added the api-unit-test-job to the GitLab pipeline so that a unit test is being applied and ran with every change we've made to the repo.

**AH-HA!💡**

**🎉 Celebrations 🎉**

### Bugs encountered 🐛🐞🐜 :

### No bugs today, as I dealt with the ones I was was having previously.

🪲

###

**\~Solution~**

###

### References Used Today:

### The references I used today were the useParams docs and stackOverflow for finding the ways to use useParams in the application.

### Any Blockers:

### No blockers at the moment.

### Tomorrow I'm working on:

### I will be working on writing unit tests for the trips backend to get all trips.

### References for Tomorrow:

## Date 10-18-2023

### Today I worked on:

### I worked on deployment of our frontend and backend application so that our application can be viewed and used on gitlab pages. It went relatively smoothly as the page was viewable on https://vacationeers.gitlab.io/voy-amie/ . I also worked on creating the able to view activities created.

**AH-HA!💡**

**🎉 Celebrations 🎉**

### Bugs encountered 🐛🐞🐜 :

###

🪲

### No bugs today

**\~Solution~**

###

### References Used Today:

###

### Any Blockers:

### No blockers today

### Tomorrow I'm working on:

### I will be working on allowing a user to go to a particular trip.

### References for Tomorrow:

## Date 10-17-2023

### Today I worked on:

### Continuing work on the trip detail page, I was able to create a form that allows a user to create a comment and I also created table to display the comments that everyone has made on a trip.

**AH-HA!💡**

**🎉 Celebrations 🎉**

### Bugs encountered 🐛🐞🐜 :

###

🪲

### No bugs today

**\~Solution~**

###

### References Used Today:

###

### Any Blockers:

### No blockers today

### Tomorrow I'm working on:

### I will be working on creating the table to allow users to view activities that were previously created.

### References for Tomorrow:

## Date 10-16-2023

### Today I worked on:

### I started working on my front-end component which is the trip detail page, which will show the details of a particular trip such as activities, comments, and adding both comments and activities.

**AH-HA!💡**

**🎉 Celebrations 🎉**

### Bugs encountered 🐛🐞🐜 :

###

🪲

### No bugs today

**\~Solution~**

###

### References Used Today:

###

### Any Blockers:

### No blockers today

### Tomorrow I'm working on:

### I was able to create the form to allow the creation of an activity.

### References for Tomorrow:

## Date 10-13-2023

### Today I worked on:

### Today we attempted to get started on the front-end of the project, We are able to create a signupform.

**AH-HA!💡**

**🎉 Celebrations 🎉**

### Bugs encountered 🐛🐞🐜 :

### Unfortunately, we were unable to submit the form due to an error where we are unable to get the token once we are signup a user. The info we pass through the front-end to the back-end is working fine, but this issue persists.

🪲

###

**\~Solution~**

### No solution, we will attempt to work on it over the weekend, but have escalated the issue to an instructor.

### References Used Today:

### The references we used was the fast api front-end auth in learn and the JWTdown for React documentation.

### Any Blockers:

### Blocker we have is we are unable to get the token once a user signups for an account.

### Tomorrow I'm working on:

### We will attempt to correct the issue and get the token once a user is signed up for an account.

### References for Tomorrow:

## Date 10-12-2023

### Today I worked on:

### Today I created the 'delete' endpoint for '/trips{trip_id}' to allow the deletion of a trip, also created the friends table to track the friends a user has. Also, created the 'post' endpoint for 'friends' to create a friendship, and also the 'get' endpoint for friends which allows to get all friends filtered by the user currently logged in.

**AH-HA!💡**

**🎉 Celebrations 🎉**

### Bugs encountered 🐛🐞🐜 :

### No bugs today, which was nice as it allowed me to work effectively today.

🪲

###

**\~Solution~**

###

### References Used Today:

### The references we used was the fast api video in learn

### Any Blockers:

### No blockers today

### Tomorrow I'm working on:

### Myself and my group will get to start the frontend aspect of the project as we have nearly completed all of the endpoints that we believe we will need.

### References for Tomorrow:

## Date 10-11-2023

### Today I worked on:

### Today I updated the activities table to include ON DELETE CASCADE for trip so that when a trip is deleted the activity associated with also be deleted as well. I also created a delete endpoint for trips so that we can delete a trip in the backend and also frontend

**AH-HA!💡**

**🎉 Celebrations 🎉**

### Bugs encountered 🐛🐞🐜 :

###

🪲

### No bugs today.

**\~Solution~**

###

### References Used Today:

### The references we used was the fast api video in learn

### Any Blockers:

### No blockers today

### Tomorrow I'm working on:

### I will be creating more endpoints for trips

### References for Tomorrow:

## Date 10-10-2023

### Today I worked on:

### Today I worked on creating the backend endpoint for the 'trips' endpoints. I was able to create the 'put' endpoint for 'trips/{trip_id}' to update a trip in the backend using fastAPI docs. I was also able to create the backend endpoint for 'get' method to get all trips for the url 'trips/', I was able to be filter the trips based on the user so that way I only get the trip associated with a user.

**AH-HA!💡**

**🎉 Celebrations 🎉**

### Bugs encountered 🐛🐞🐜 :

### No bugs today, which was nice as it allowed me to work effectively today.

🪲

###

**\~Solution~**

###

### References Used Today:

### The references we used was the fast api video in learn

### Any Blockers:

### No blockers today

### Tomorrow I'm working on:

### I will working on the 'delete' method for the trips endpoint, and possible start working on the friends endpoint to develop a friends-list amongst users.

### References for Tomorrow:

## Date 10-09-2023

### Today I worked on:

### Today I worked on creating the backend endpoint for the 'trips' endpoints. I was able to create the 'post' endpoint for 'trips/' to create a trip in the backend using fastAPI docs. I was also able to create the backend endpoint for 'get' method to get a specific trip for the url 'trips/{trip_id}'.

**AH-HA!💡**

**🎉 Celebrations 🎉**

### Bugs encountered 🐛🐞🐜 :

### No bugs today, which was nice as it allowed me to work effectively today.

🪲

###

**\~Solution~**

###

### References Used Today:

### The references we used was the fast api video in learn

### Any Blockers:

### No blockers today

### Tomorrow I'm working on:

### I will working on the 'put' method to edit a trip, and a 'get' method to get all trips a user has created.

### References for Tomorrow:

## Date 09-29-2023

### Today I worked on:

### Today we attempted to handle backend authentication as a group doing mob programming. At the end of the day we were able to complete authentication on the backend as a group and will be working on protecting the endpoints we have created.

**AH-HA!💡**

**🎉 Celebrations 🎉**

### Bugs encountered 🐛🐞🐜 :

### No bugs, just were having trouble with implementing auth

🪲

###

**\~Solution~**

### We had to change our schema to include the hashed password in our UsersOut to work with the authenticator from JWTDown and once we did that we were able to receive the token and backend authentication was completed.

### References Used Today:

### The references we used was the fast api video in learn

### Any Blockers:

### No blockers today

### Tomorrow I'm working on:

### We will be on break, but we will be working on creating protected endpoints for all of the created ones we have.

### References for Tomorrow:

## Date 09-28-2023

### Today I worked on:

### Today we worked on creating the endpoints for authentication, with login, signup, and logout.

**AH-HA!💡**

**🎉 Celebrations 🎉**

## We were able to have authentication with our application and we were able to create a token. We have our first couple of endpoints implemented in our application.

### Bugs encountered 🐛🐞🐜 :

### We were having issues with keeping tracking of all the changing occurring between the password and hash-password and that was creating issues with creating a user.

🪲

###

**\~Solution~**

### We ended up updating the user table from password to hashed_password to use the get_hashed_password to create a hashed_password and not store user passwords.

### References Used Today:

### The references we used was the fast api video and the jwtdown video in learn, also the jwtdown fastapi documentation.

### Any Blockers:

### No blockers today

### Tomorrow I'm working on:

### Once we are back on break we will be working on the rest of our api endpoints.

### References for Tomorrow:

## Date 09-27-2023

### Today I worked on:

### Today we worked on creating all of the tables we plan on using in our applications, and created those tables in our table_migrations.py file. We also started our working on creating the endpoint to create a user, specifically "/users" Post method.

**AH-HA!💡**

**🎉 Celebrations 🎉**

### Bugs encountered 🐛🐞🐜 :

### So we had to delete the containers and volume every time we made a change to a table or added a new table to the table_migrations.py.

🪲

### The only bug we encountered was the fact that we couldn't use python -m migrations up in our fastapi container as there was a conflict with the migration history.

**\~Solution~**

### So we had to delete the containers and volume every time we made a change to a table or added a new table to the table_migrations.py.

### References Used Today:

### The references we used was the fast api video in learn

### Any Blockers:

### No blockers today

### Tomorrow I'm working on:

### We will be working on finishing the user endpoints and hopefully set up authentication tomorrow.

### References for Tomorrow:
