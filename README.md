# run-your-gpt- Instructions for setting up and running the application
<hr>
<h2>Clone the repo</h2>

step 1: use below cammand to clone the repo

<pre>
git clone git clone https://github.com/shashanknaik0/run-your-gpt-backend.git
</pre>


step 2: get into the directory
<pre>
cd run-your-gpt-backend
</pre>

<hr>
<h2>Setup the virtual environment</h2>
use <a href="https://www.w3schools.com/django/django_create_virtual_environment.php">this</a> link to get Instructions to create and activate virtual environment.

<hr>
<h2>Install dependecies</h2>

use below cammand install python dependecies from <code>requirement.txt</code>
<pre>
pip install -r requirements.txt
</pre>

<hr>
<h2>Run the project</h2>

step 1: rum below cammand to migrate the django models.
<pre>
python manage.py makemigrations
</pre>
<pre>
python manage.py migrate
</pre>

step 2: to create superuser run below cammand. (<a href="https://docs.djangoproject.com/en/4.2/intro/tutorial02/#creating-an-admin-user">click me</a> for more info)
<pre>
python manage.py createsuperuser
</pre>

step 3: run the server
<pre>
python manage.py runserver
</pre>

step 4: development server will be running  at http://127.0.0.1:8000 
<pre>
/admin - this is built in functionaity in django admin site.
/signup - (POST) Add a new user to the platform. The user details will include fields like username, email, and password. 
/login - (POST) login the user.
/message/ - (GET) Fetch the message stored in DB.
/message/ - (POST) To add new message to DB.
/message/count - (GET) fetch the message count.
/csrf - (GET) fetch csrf tocken.
</pre>
