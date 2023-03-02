# Flight Deal Notifier with Tequila API by Kiwi and Sheety

### Flight Deal Notifier uses:

- Tequila API by Kiwi - Flight Search and Booking tool with a comprehensive API

- Sheety - A way of turning spreadsheets into API's, with the ability to GET and even POST to the spreadsheet of our choice

Using Sheety, I open my Google Sheet containing the City, IATA Code of the City and my target price of the flight

The IATA Codes which are used to identify airports are then generated and appended to the google sheet if they don't exist

Every City in the sheet is then used as a parameter of the Tequila API, and the cheapest flight is then found, based on the pre-defined parameters

The details of the best flights are saved, and the target price is compared to the price of the flight

If the target price is lower than the ticket price, I get sent an email via SMTP with the details of the flight, and a link to the portal where I can purchase the ticket
