# Private_Social_Web

A site just for friends ^_^

 These are some features!
- Invite-only user registration
- All posts are visible to all users
- User authentication with Flask-Login
- SQLite database (easy to run locally!)

## How 2 set up:

Before you begin, you'll need to open your terminal. 

- **On macOS**: 
  - Open the `Terminal` application. You can find it by going to `Applications > Utilities > Terminal`.

- **On Windows**:
  - Open the `Command Prompt` by searching for "cmd" or "Command Prompt" in the Start menu, or you can use `Windows PowerShell`.

Once your terminal is open, follow the steps below to set up the app.


### 1. Clone the repo
Clone the repository to your local machine by running the following command in your terminal and cd into it:

```git clone https://github.com/kt-k10/Private_Social_Web.git```

```cd Private_Social_Web ```

### 2. Create a virtual environment
Create a virtual environment to isolate your project dependencies:

```python -m venv venv ```

Activate the virtual environment:

On macOS/Linux:

```source venv/bin/activate ```

On Windows:

```venv\Scripts\activate ```

### 3. Install dependencies
Once your virtual environment is activated, install the required dependencies by running:

```pip install -r requirements.txt ```

### 4. Create the database
To create the necessary database tables, open a Python shell using Flask:

```flask shell ```

Then, run the following commands to set up the database:

```python from app import db```

```db.create_all()```

```exit()```

### 5. Run the app
Now that everything is set up, you can run the app with:

```flask run ```

The app should now be accessible at [http://localhost:5000](http://127.0.0.1:5000/
). Open this URL in your browser to use the application.

### Tech Stack
- Python

- Flask 

- Flask-Login 

- SQLite

- Jinja2 Templates

### Note: Invite codes

To control access, valid invite codes are stored in a file called invites.txt in the root directory. Each line should contain one invite code. As of when I'm posting this, there is only one invite code and it's not uploaded to github so don't go poking around on here.



