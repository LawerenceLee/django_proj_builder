import os
import shutil


def clear():
    os.system('cls' if os.name == "nt" else 'clear')


def build_filesys():
    start_path = os.getcwd()
    index_path = start_path + "/PREBUILT_TEMPLATES/index.html"
    layout_path = start_path + "/PREBUILT_TEMPLATES/layout.html"
    css_path = start_path + "/PREBUILT_TEMPLATES/style.css"
    os.system("django-admin startproject {}_main".format(PROJ_NAME))
    os.rename(PROJ_NAME+"_main", PROJ_NAME+"_proj")
    os.chdir('{}_proj'.format(PROJ_NAME))
    root_path = os.getcwd()
    os.mkdir("apps")

    os.chdir("apps")
    os.system("touch __init__.py")
    os.system("python ../manage.py startapp {}".format(APP_NAME))

    os.chdir(APP_NAME)
    os.system("touch urls.py")
    urls_starter = "from django.conf.urls import url\n\nfrom . import views"
    urls_starter += "\n\nurlpatterns = [\n"
    urls_starter += "    url(r'^$', views.index)\n]"
    os.system('echo "{}" >> urls.py'.format(urls_starter))
    os.makedirs("templates/{}".format(APP_NAME))

    index_view = "\ndef index(request):\n    "
    index_view += "return render(request, '{}/index.html')".format(APP_NAME)
    os.system(' echo "{}" >> views.py'.format(index_view))

    os.mkdir("static")
    os.chdir("static")
    os.makedirs("{}/css".format(APP_NAME))
    os.chdir("{}".format(APP_NAME))
    os.makedirs("img".format(APP_NAME))
    os.makedirs("js".format(APP_NAME))
    os.chdir("../../")

    os.chdir("templates/{}".format(APP_NAME))
    shutil.copy(index_path, os.getcwd()+"/")
    shutil.copy(layout_path, os.getcwd()+"/")

    os.chdir("../../static/{}/css".format(APP_NAME))
    shutil.copy(css_path, os.getcwd()+"/")

    shutil.move(root_path, "{}/..".format(start_path))


def to_do_list():
    print("\nTO DO LIST:")
    print("\t- Add 'apps.{}' to INSTALLED APPS inside {}_main/settings.py\
        ".format(APP_NAME, PROJ_NAME))
    print("\t- Add 'url(r'^'/', include('apps.{}.urls'),' to \
        \n\t  urls.py inside {}_main".format(APP_NAME, APP_NAME, PROJ_NAME))
    print("\t- Add the 'include' import to 'from django.conf.urls import url'")
    print("\t- Change the path of the link tag in 'layout.html'")
    print("\t- Change the title in the title tag in 'layout.html'")
    print("\t- Change the path of the extends function in 'index.html'\n")


if __name__ == '__main__':
    clear()
    thirty_three = "-" * 33
    print("{} DJANGO PROJECT BUILDER WITH APPS {}".format(
        thirty_three, thirty_three))
    PROJ_NAME = raw_input("Enter a Project Name: ")
    APP_NAME = raw_input("Enter an App Name: ")
    build_filesys()
    to_do_list()
