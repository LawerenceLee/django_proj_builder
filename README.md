# Django Project Builder
`build_django_w_apps.py`: Builds the skeleton files and directory structure for a basic Django Project, with a single app.
`build_django_app.py`: Builds the skeleton files and directory structure for a basic Django app.

Both Build the following extras:
* template/<app_name>/layout.html
* template/<app_name>/index.html (inherits from layout)
* static/<app_name>/js
* static/<app_name>/img
* static/<app_name>/css/style.css (sets padding and margins to zero, and adds color to message tags error and success)
* views.py is appended with a basic view function for index
* urls.py (includes needed imports, as well as a basic route to the index view)
* prints out url function specific to the app_name given. (Can be easily pasted into urls.py in project's main folder)
* prints out a series of reminders of things to add and amend in your app and project for it to function.



## CODING DOJO Folks
git clone this to your Django Folder

* FYI: It will only generate project's that are adjacent to the django_proj_builder directory.
