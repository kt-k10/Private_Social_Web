# Private_Social_Web

A private social media site just for friends ^_^

### These are some features!
-Invite-only user registration
-All posts are visible to all users
-User authentication with Flask-Login
-SQLite database (easy to run locally!)

## How 2 set up:

### 1. Clone the repo
Clone the repository to your local machine by running the following command in your terminal:

```bash git clone https://github.com/kt-k10/Private_Social_Web.git cd Private_Social_Web ```

### 2. Create a virtual environment
Create a virtual environment to isolate your project dependencies:

```bash python3 -m venv venv ```

Activate the virtual environment:

On macOS/Linux:

```bash source venv/bin/activate ```

On Windows:

```bash venv\Scripts\activate ```

### 3. Install dependencies
Once your virtual environment is activated, install the required dependencies by running:

```bash pip install -r requirements.txt ```

### 4. Create the database
To create the necessary database tables, open a Python shell using Flask:

```bash flask shell ```

Then, run the following commands to set up the database:

```python from app import db db.create_all() exit() ```

### 5. Add invite codes
To control access, valid invite codes are stored in a file called invites.txt in the root directory. Each line should contain one invite code. For example:

```text ABC123 FRIENDZONLY TOPSECRET ```

### 6. Run the app
Now that everything is set up, you can run the app with:

```bash flask run ```

The app should now be accessible at http://localhost:5000. Open this URL in your browser to use the application.

### Tech Stack
Python
Flask
Flask-Login
SQLite
Jinja2 Templates



