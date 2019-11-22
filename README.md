# Welcome to the Flask portion of our subreddit suggester web app. 
#### Authors: David Nagy, Stefano Ruiz
#### Credits: Matthew Sessions, Johana Luna

### Summary
Our flask app is designed to take in a sample Reddit post provided by the user in [the front-end](https://github.com/BuildWeek-PostHere-Subreddit/FE) (i.e the app's landing page), run it through [the
machine learning model](https://github.com/BuildWeek-PostHere-Subreddit/MachineLearning) (created by Johana Luna and Matthew Sessions), gather data about the subreddits the model outputs in accordance to an abstracted similarity score, and send that data back to the front-end.

### Functionality
The app.py file contains the code necessary to run the app, including:
* The app's four routes: the root, the route that the front-end accesses, a testing route,
and a route built in preparation for expanding the app to include predictions based on an inputted username
* Functions calls to get the information that is entered by the user either in the front-end or the Flask app itself
* Returning a .JSON object with the suggested subreddits along with their descriptions and summary statistics

In addition, we have a functions.py file that contains the major reusable code for the app; a models.py file
that contains code to make dummy models for testing purposes; and a unittest file that confirms the accuracy
of our jsonConversion file. 
