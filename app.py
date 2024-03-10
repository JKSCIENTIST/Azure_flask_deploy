from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <html>
    <head>
        <title>Hello, Azure Web Apps!</title>
        <style>
            body {
                background-color: #f0f0f0; /* Light gray */
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
            }

            .container {
                background-color: #ffffff; /* White */
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello, Azure Web Apps!</h1>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()
