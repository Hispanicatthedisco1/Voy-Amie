## Oct 26, 2023
Today was a really frustrating day. Abe pointed out we still needed to make a component for making friends and displaying a friends list. I quickly jumped on it since I had an idea on how to design this. I did not want to display a list of all existing users to the logged in user as that is a no-no, so I wanted to make it so someone types another user's username and as the person types, a list with usernames that contain those characters starts to populate. The setup for this component was fairly easy as I just had to fetch data for all users and all of the user's already existing friends then create a POST method fetch that takes care of creating that friendship of the selected user. I thought of fetching for existing friends in order to conditionally render users that are not yet friends with the user that is logged in. This will avoid duplicate friendships since we did not set friendships to UNIQUE in our tables. That is where the tricky part came. I started by creating a function that determines whether or not someone is already your friend. Implementing it into the return statement as a ternary was not working. Jordan spent some time troubleshooting with me and Abe. It ended up being that we needed to make it into a normal "if" statement and not a ternary function. It is funny how some methods will works in some instances, but not in others. During this session, Jordan also helped me and Abe with styling buttons. I learned about manipulating the padding and margins of a button!!


## Oct 25, 2023
I am still working on the participants component. SPecifically extracting the user's username and comparing it to the participants list to make sure the only users that are not yet participants be displayed in a friends list (where they can add them as participants) . It has proven very difficult to find the logic and reasoning I will need to filter the friends list from the frontend. I had a meeting with Paul and he suggested I take care of that filtering through the backend. So, I looked into updating the SQL statement for get_all_participants. I was rather proud that I was able to come up with a clever SQL JOIN statement that collected all the necessary data into one list, instead of having to deal with comparing 3 lists of data with each other! This was very revelatory and really set my on the right path! I was finally able to finish this feature and got it to behave the way I wanted it to. Now I have to work on creating a button that only a trip's planner will have access to that will redirect them to this component.


## Oct 24, 2023
Today I took the reigns and started the day by assigning tasks to everyone and keeping track of their progress throughout the day. I also focused on helping Abe with his component as he has been stuck on it for around two days now. His component seemed to be the most complex for sure. We were trying to tackle the hard task of keeping track of votes and creating them. We spent most of the day working on it. We had to end up creating a new DB table for votes and POST, DELETE, and GET endpoints. We busted that out quite quickly. We learned about and implemented the UNIQUE keyword in out table. Assuring that a user only gets one vote bypassing duplicate edge cases. This felt like a very productive day. We ended up getting it all done! I definitely am starting to feel a bit bad at the current styling of our project, but I know we will have time to jush it up next week during stretch goals week.


## Oct 20, 2023

What I worked on: Unittest
BUGS: I am having a hard time passing along the mock user data through the function while testing for a POST endpoint.
I met with Rosheen and we still could not find a solution to the problem. I did well when creating the mock repo and the mock json response. We have yet to find how to pass along the authenticator successfully.


## Oct 19, 2023
Still working on the FE Create Trip component. I have been quite stuck on how to implement a feature that adds a participant while making a trip. Created all the fetch data functions and set states, just seeing now how to manipulate the return statement.


## Oct 18, 2023
Bugs: How to gain access to a friend's username since friendships only contain user_id's.
Solution: Was able to update out get friend router. it now uses two repos (friends and users) and uses the UserOut model when returning data for the user that is 'your' friends (user2_id).
I did not know you could do that!

## Oct 17, 2023


## Oct 09, 2023

The team decided to work over our fall break and meet up twice to keep working on some backend auth. This feature is definitely one of the most tricky and difficult tasks I have had to do all boot camp long. I understand the concept of having to authenticate someone and make sure they are an allowed user, but having to manually take care of authentication is hard work. I miss how helpful Django is in time like these. Today is the first day back from break and I have a better mind set going forward. I was starting to lose hope and did not know how I was going to continue. We still need some help with out back end, but we are doing well in practicing good communication and staying on track so far.


## SEPT 27, 2023

Today, my group and I worked on:
    + creating database tables
    + creating our first endpoint to create a user

We took turns throughout the process with coding, watching, creating the issues and merge requests on gitlab. This finally allowed me to learn interactively. My team and I collaborate well and were able to tackle any of the issues we came across in good time.
We kept having to prune and rebuild our containers and volumes during the part we had to migrate after each table creation.
Before we started the creation of our first endpoint, we took some time to watch the educational video on the subject from last week's exploration. THis really helped us refresh our minds on how to go about creating an endpoint with FastAPI.
I was very excited when I was able to find the solution to a postgres issue we ran into while trying to troubleshoot on Beekeeper! It reminded me that no matter how stuck I am, I can always find the solution so long as I know what to look for.
