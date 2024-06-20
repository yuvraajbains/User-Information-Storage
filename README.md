# User-Information-Storage
This is the code and general information about how and what a user enters into a form on a public server which then transmits the information back into a google sheet.


Steps Required to Set Up:

# First Step

Set up the Google Sheets API- 

1. Create a new project in the Google Cloud Console and then proceed to select enable Sheets API so you are able to properly attach the sheet to the code which will be done later.
2. Gather the credentials for the API and download the JSON file
3. Share the Google Sheet with the service account email inside the JSON file to link both servers


# Second Step

*Reminder here you are able to use any web server environment but I decided to use Flask as I was already familiar with it

To install flask onto your CPU go to command prompt and paste:

pip install flask google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

- This will give your computer access to everything you need to complete this project

# Third Step

Go inside a coding environment in this case I used VSCODE which I find easy to use

Create two separate files:
- A Flask Application
- A HTML + CSS Application

These will allow your Google Sheet to communicate back and fourth with people entering information on the HTML form with the information displaying back in the Google Sheet they selected. This implementation is feasable but only for the local computer that the code and everything was created on. This is why the implementation of the next step is very key if you would like to take this a step further. 

# Fourth Step

Introducing Ngrok...

Ngrok will expose your local Flask Server securely so that anyone is able to enter information into the form and you will recieve it back to the Google Sheet. 

Go to ngrok.com and download ngrok. I watched a very good youtube video by ProgrammingKnowledge on how to download it.

Once everything is properly downloaded all you need to do is match the server link inside the app.py file with the Ngrok server you will establish.

# Conclusion

At this point everything is properly setup and the web page is live for anyone with access to the Ngrok link which you can find in the command prompt that you established. 

I hope something inovative was learned :)

# Suplementary features

I have significantly improved the visual aspect of the code introducing other features that can be used with HTML such as "hover"

Additionally I added a form submission counter so that when you make the form live it will continuously count how many people submitted the form. Be aware the counter resets when you take Ngrok offline which would make sense as you are practically removing your page off the internet. 

- Feature to track submissions is stored in the back-end area using Flask which is already connected to my Google Sheet API so it makes sense as to why the new code has been added to the app.py file.
