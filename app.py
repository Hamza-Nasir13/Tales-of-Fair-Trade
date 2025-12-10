from flask import Flask, render_template, send_file

# 1. Create a Flask application instance.
# The argument __name__ tells Flask where to look for resources.
app = Flask(__name__)

# 2. Define a route (URL) for the application.
# The '/' means this function will handle requests to the homepage (e.g., http://127.0.0.1:5000/)
@app.route('/')
def home():
    """Renders the index.html template."""
    # Flask automatically looks in the 'templates' folder for index.html
    return render_template('index.html')

# The /about route can be kept or removed
@app.route('/about')
def about():
    """Renders a simple text message for the about page."""
    return "This is the About page."

@app.route('/download')
def download_pdf():
    # 1. Define the filename and path (relative to app.py)
    path_to_file = "Tales of Fair Trade.pdf"
    
    # 2. Return the file using send_file
    #    as_attachment=True forces the browser to download the file.
    #    download_name sets the filename the user sees.
    return send_file(
        path_to_file,
        as_attachment=True,
        download_name="Tales of Fair Trade.pdf"
    )

# if __name__ == '__main__':
#     # Ensure you are still running in debug mode for easy development
#     app.run(debug=True)