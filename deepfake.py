from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'fileInput' not in request.files:
        return redirect(request.url)
    file = request.files['fileInput']
    if file.filename == '':
        return redirect(request.url)

    # Process the file for deep fake detection here

    # For demonstration, just redirect to home
    # In practice, you'll process the file and show results
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
