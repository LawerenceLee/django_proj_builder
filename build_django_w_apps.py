import os
import shutil


def build_filesys():
    # Save paths for templates, and projects top lvl dir
    start_path = os.getcwd()
    index_path = start_path + "/PREBUILT_TEMPLATES/index.html"
    layout_path = start_path + "/PREBUILT_TEMPLATES/layout.html"
    css_path = start_path + "/PREBUILT_TEMPLATES/style.css"

    # Build Django Project w/ provided project name
    os.system("django-admin startproject {}_main".format(PROJ_NAME))

    # Change Project's top level directory to use '<project_name>_proj' instead
    os.rename(PROJ_NAME+"_main", PROJ_NAME+"_proj")
    # Change into said dir
    os.chdir('{}_proj'.format(PROJ_NAME))

    # Save the path just inside projects top lvl dir
    root_path = os.getcwd()

    # Create a django app with provided app name
    os.system("python manage.py startapp {}".format(APP_NAME))

    # CD into App's dir and create urls..py
    os.chdir(APP_NAME)
    os.system("touch urls.py")
    # Add imports and url for a basic index view
    urls_starter = "from django.conf.urls import url\n\nfrom . import views"
    urls_starter += "\n\nurlpatterns = [\n"
    urls_starter += "    url(r'^$', views.index)\n]"
    os.system('echo "{}" >> urls.py'.format(urls_starter))

    # Append a basic index view function into 'views.py'
    index_view = "from django.contrib import messages"
    index_view += "\ndef index(request):\n    "
    index_view += "return render(request, '{}/index.html')".format(APP_NAME)
    os.system(' echo "{}" >> views.py'.format(index_view))

    # Create templates dir
    os.makedirs("templates/{}".format(APP_NAME))
    os.chdir("templates/{}".format(APP_NAME))
    # Move templates into App
    shutil.copy(index_path, os.getcwd()+"/")
    shutil.copy(layout_path, os.getcwd()+"/")
    # Navigate two dirs up
    os.chdir("../../")

    # Create a static dir and CD into it
    os.makedirs("static/{}".format(APP_NAME))
    os.chdir("static/{}".format(APP_NAME))
    # Create js, img, and css dirs
    os.mkdir("img")
    os.mkdir("js")
    os.mkdir("css")
    # CD into css dir
    os.chdir("css")
    # Move style.css template to css dir
    shutil.copy(css_path, os.getcwd()+"/")

    # Move entire project outside of DJANGO PROJ BUILDER dir
    shutil.move(root_path, "{}/..".format(start_path))


def to_do_list():
    print("\nTO DO LIST:")
    print("\t- Add '{}' to INSTALLED APPS inside {}_main/settings.py\
        ".format(APP_NAME, PROJ_NAME))
    print("\t- Add 'url(r'^/', include('{}.urls'),' to \
        \n\t  urls.py inside {}_main".format(APP_NAME, APP_NAME, PROJ_NAME))
    print("\t- Add the 'include' import to 'from django.conf.urls import url'")
    print("\t- Change the path of the link tag in 'layout.html'")
    print("\t- Change the title in the title tag in 'layout.html'")
    print("\t- Change the path of the extends function in 'index.html'\n")


if __name__ == '__main__':
    os.system('cls' if os.name == "nt" else 'clear')
    thirty_three = "-" * 33
    print("{} DJANGO PROJECT BUILDER WITH APPS {}".format(
        thirty_three, thirty_three))
    PROJ_NAME = input("\nEnter a Project Name: ")
    APP_NAME = input("Enter an App Name: ")
    build_filesys()
    to_do_list()
