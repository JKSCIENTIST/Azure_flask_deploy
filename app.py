from flask import Flask

app = Flask(__name__)

@app.route('/')
def display_styled_code():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Styled Code Block</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          background-color: #f2f2f2;
          padding: 20px;
        }

        .code-container {
          background-color: #fff;
          border-radius: 5px;
          padding: 20px;
          box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
          margin-bottom: 20px;
        }

        pre {
          white-space: pre-wrap;
          overflow-x: auto;
        }
      </style>
    </head>
    <body>
      <div class="code-container">
        <pre>
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, Azure Web Apps!'

    if __name__ == '__main__':
        app.run()
        </pre>
      </div>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run()
