from flask import Flask
import requests

app = Flask(__name__)

# Define a route to display the content from Pastebin
@app.route('/')
def pastebin_content():
    # Replace 'PASTEBIN_LINK' with the actual Pastebin link
    pastebin_link = 'https://pastebin.com/raw/PCiaPsTa'
    
    # Make an HTTP GET request to the Pastebin link
    response = requests.get(pastebin_link)
    
    # Check if the request was successful
    if response.status_code == 200:
        content = response.text
        return content
    else:
        return "Failed to retrieve content from Pastebin"

if __name__ == '__main__':
    app.run(debug=True)
