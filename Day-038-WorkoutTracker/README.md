# Workout Tracker with Nutritionix and Sheety

This workout tracker uses:
- Nutritionix - A nutrition database which uses OpenAI's Chat GPT-3's Natural Language Processing in order to process a workout prompt I feed it. For example, "I ran 3 miles in 30 minutes and cycled 15 miles in 20 minutes".

- Sheety - A way of turning spreadsheets into API's, with the ability to GET and even POST to the spreadsheet of our choice.

After recieving a workout description, using NLP, Nutritionix returns a json table with the details of the workout.

Rearranging the data into a managable format and sending a POST request via sheety allows me to update a Google sheet with the workouts.

Nutritionix is also smart enough to separate workouts when seeing the keyword 'and', allowing us to created many rows of workout data in a single prompt it receives. 

One of the most useful programs I have made to date.

Try it out!