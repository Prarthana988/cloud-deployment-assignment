from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Simulating a simple dynamic message / basic storage/config read
    app_name = "GMIU Cloud Deployment Demo"
    cloud_env = os.environ.get('CLOUD_ENV', 'Local Development')

    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>{{ title }}</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f4f4f9; }
            .container { background: white; padding: 30px; border-radius: 8px; display: inline-block; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
            h1 { color: #2c3e50; }
            p { color: #7f8c8d; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{{ title }}</h1>
            <p>Status: <span style="color: green; font-weight: bold;">Running Successfully 🚀</span></p>
            <p>Environment: <strong>{{ env }}</strong></p>
            <hr>
            <p>Student Cloud Assignment Portal Submission</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content, title=app_name, env=cloud_env)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)