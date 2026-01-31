from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Configure template and static folders
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'your-secret-key-here'  # Change this to a random secret key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/room')
def room():
    return render_template('room.html')

@app.route('/amenities')
def amenities():
    return render_template('amenities.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # Handle booking form submission
        # You can add your booking logic here
        return redirect(url_for('index'))
    return render_template('booking.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission
        # You can add your login logic here
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle contact form submission
        # You can add your contact logic here
        return redirect(url_for('index'))
    return render_template('contact.html')

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return f"Internal Server Error: {str(e)}", 500

if __name__ == '__main__':
    # Check if templates folder exists
    templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
    if not os.path.exists(templates_dir):
        os.makedirs(templates_dir)
        print(f"Created templates directory at: {templates_dir}")
    
    # Check if static folder exists
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
        print(f"Created static directory at: {static_dir}")
    
    app.run(debug=True)
