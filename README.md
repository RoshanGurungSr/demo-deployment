# demo-deployment
Demo deployment project for the python web API

## Steps to execute the codes
To setup the libraries:
`pip install -r requirements.txt`

To run the server, use this command: 
`flask run --host '0.0.0.0'`

## API Routes
+ `http://0.0.0.0/` : Main landing page
+  `http://0.0.0.0/home/<input>`: POST method which takes the user input and displays on the page
