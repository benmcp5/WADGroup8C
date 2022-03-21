import os
import importlib
from django.urls import reverse
from django.test import TestCase
from django.conf import settings

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}CSG TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

class ProjectStructureTests(TestCase):
    """
    Simple tests to probe the file structure of your project so far.
    We also include a test to check whether you have added ClubScoutGlasgow to your list of INSTALLED_APPS.
    """
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.ClubScoutGlasgow_app_dir = os.path.join(self.project_base_dir, 'ClubScoutGlasgow')

    def test_project_created(self):
        """
        Tests whether the WADGroup8C_project configuration directory is present and correct.
        """
        directory_exists = os.path.isdir(os.path.join(self.project_base_dir, 'WADGroup8C_project'))
        urls_module_exists = os.path.isfile(os.path.join(self.project_base_dir, 'WADGroup8C_project', 'urls.py'))

        self.assertTrue(directory_exists, f"{FAILURE_HEADER}Your WADGroup8C_project configuration directory doesn't seem to exist. Did you use the correct name?{FAILURE_FOOTER}")
        self.assertTrue(urls_module_exists, f"{FAILURE_HEADER}Your project's urls.py module does not exist. Did you use the startproject command?{FAILURE_FOOTER}")

    def test_ClubScoutGlasgow_app_created(self):
        """
        Determines whether the ClubScoutGlasgow app has been created.
        """
        directory_exists = os.path.isdir(self.ClubScoutGlasgow_app_dir)
        is_python_package = os.path.isfile(os.path.join(self.ClubScoutGlasgow_app_dir, '__init__.py'))
        views_module_exists = os.path.isfile(os.path.join(self.ClubScoutGlasgow_app_dir, 'views.py'))

        self.assertTrue(directory_exists, f"{FAILURE_HEADER}The ClubScoutGlasgow app directory does not exist. Did you use the startapp command?{FAILURE_FOOTER}")
        self.assertTrue(is_python_package, f"{FAILURE_HEADER}The ClubScoutGlasgow directory is missing files. Did you use the startapp command?{FAILURE_FOOTER}")
        self.assertTrue(views_module_exists, f"{FAILURE_HEADER}The ClubScoutGlasgow directory is missing files. Did you use the startapp command?{FAILURE_FOOTER}")

    def test_ClubScoutGlasgow_has_urls_module(self):
        """
        Did you create a separate urls.py module for ClubScoutGlasgow?
        """
        module_exists = os.path.isfile(os.path.join(self.ClubScoutGlasgow_app_dir, 'urls.py'))
        self.assertTrue(module_exists, f"{FAILURE_HEADER}The ClubScoutGlasgow app's urls.py module is missing. Read over the instructions carefully, and try again. You need TWO urls.py modules.{FAILURE_FOOTER}")

    def test_is_ClubScoutGlasgow_app_configured(self):
        """
        Did you add the new ClubScoutGlasgow app to your INSTALLED_APPS list?
        """
        is_app_configured = 'ClubScoutGlasgow' in settings.INSTALLED_APPS

        self.assertTrue(is_app_configured, f"{FAILURE_HEADER}The ClubScoutGlasgow app is missing from your setting's INSTALLED_APPS list.{FAILURE_FOOTER}")

class HomePageTests(TestCase):
    """
    Testing the basics of your index view and URL mapping.
    Also runs tests to check the response from the server.
    """
    def setUp(self):
        self.views_module = importlib.import_module('ClubScoutGlasgow.views')
        self.views_module_listing = dir(self.views_module)

        self.project_urls_module = importlib.import_module('WADGroup8C_project.urls')

    def test_view_exists(self):
        """
        Does the home() view exist in ClubScoutGlasgow's views.py module?
        """
        name_exists = 'index' in self.views_module_listing
        is_callable = callable(self.views_module.home)

        self.assertTrue(name_exists, f"{FAILURE_HEADER}The home() view for ClubScoutGlasgow does not exist.{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}Check that you have created the index() view correctly. It doesn't seem to be a function!{FAILURE_FOOTER}")

    def test_mappings_exists(self):
        """
        Are the two required URL mappings present and correct?
        One should be in the project's urls.py, the second in ClubScoutGlasgow's urls.py.
        We have the 'index' view named twice -- it should resolve to '/ClubScoutGlasgow/'.
        """
        home_mapping_exists = False

        # This is overridden. We need to manually check it exists.
        for mapping in self.project_urls_module.urlpatterns:
            if hasattr(mapping, 'name'):
                if mapping.name == 'home':
                    home_mapping_exists = True

        self.assertTrue(home_mapping_exists, f"{FAILURE_HEADER}The home URL mapping could not be found. Check your PROJECT'S urls.py module.{FAILURE_FOOTER}")
        self.assertEquals(reverse('ClubScoutGlasgow:index'), '/ClubScoutGlasgow/', f"{FAILURE_HEADER}The home URL lookup failed. Check ClubScoutGlasgow's urls.py module. You're missing something in there.{FAILURE_FOOTER}")

    def test_response(self):
        """
        Does the response from the server contain the required string?
        """
        response = self.client.get(reverse('ClubScoutGlasgow:home'))

        self.assertEqual(response.status_code, 200, f"{FAILURE_HEADER}Requesting the home page failed. Check your URLs and view.{FAILURE_FOOTER}")

    def test_for_about_hyperlink(self):
        """
        Does the response contain the about hyperlink required in the exercise?
        Checks for both single and double quotes in the attribute. Both are acceptable.
        """
        response = self.client.get(reverse('ClubScoutGlasgow:home'))

        single_quotes_check = '<a href=\'/ClubScoutGlasgow/about/\'>About</a>' in response.content.decode() or '<a href=\'/ClubScoutGlasgow/about\'>About</a>' in response.content.decode()
        double_quotes_check = '<a href="/ClubScoutGlasgow/about/">About</a>' in response.content.decode() or '<a href="/ClubScoutGlasgow/about">About</a>' in response.content.decode()

        self.assertTrue(single_quotes_check or double_quotes_check, f"{FAILURE_HEADER}We couldn't find the hyperlink to the /ClubScoutGlasgow/about/ URL in your index page. Check that it appears EXACTLY as in the book.{FAILURE_FOOTER}")

class AboutPageTests(TestCase):
    """
    Tests to check the about view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """
    def setUp(self):
        self.views_module = importlib.import_module('ClubScoutGlasgow.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the about() view exist in ClubScoutGlasgow's views.py module?
        """
        name_exists = 'about' in self.views_module_listing
        is_callable = callable(self.views_module.about)

        self.assertTrue(name_exists, f"{FAILURE_HEADER}We couldn't find the view for your about view! It should be called about().{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}Check you have defined your about() view correctly. We can't execute it.{FAILURE_FOOTER}")

    def test_mapping_exists(self):
        """
        Checks whether the about view has the correct URL mapping.
        """
        self.assertEquals(reverse('ClubScoutGlasgow:about'), '/ClubScoutGlasgow/about/', f"{FAILURE_HEADER}Your about URL mapping is either missing or mistyped.{FAILURE_FOOTER}")

    def test_response(self):

        response = self.client.get(reverse('ClubScoutGlasgow:about'))

        self.assertEqual(response.status_code, 200, f"{FAILURE_HEADER}When requesting the about view, the server did not respond correctly. Is everything correct in your URL mappings and the view?{FAILURE_FOOTER}")


class TemplatesStructureTests(TestCase):
    """
    Have you set templates, static files and media files up correctly, as per the book?
    """
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.templates_dir = os.path.join(self.project_base_dir, 'templates')
        self.ClubScoutGlasgow_templates_dir = os.path.join(self.templates_dir, 'ClubScoutGlasgow')

    def test_templates_directory_exists(self):
        """
        Does the templates/ directory exist?
        """
        directory_exists = os.path.isdir(self.templates_dir)
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}Your project's templates directory does not exist.{FAILURE_FOOTER}")

    def test_ClubScoutGlasgow_templates_directory_exists(self):
        """
        Does the templates/ClubScoutGlasgow/ directory exist?
        """
        directory_exists = os.path.isdir(self.ClubScoutGlasgow_templates_dir)
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}The ClubScoutGlasgow templates directory does not exist.{FAILURE_FOOTER}")

    def test_template_dir_setting(self):
        """
        Does the TEMPLATE_DIR setting exist, and does it point to the right directory?
        """
        variable_exists = 'TEMPLATE_DIR' in dir(settings)
        self.assertTrue(variable_exists, f"{FAILURE_HEADER}Your settings.py module does not have the variable TEMPLATE_DIR defined!{FAILURE_FOOTER}")

        template_dir_value = os.path.normpath(settings.TEMPLATE_DIR)
        template_dir_computed = os.path.normpath(self.templates_dir)
        self.assertEqual(template_dir_value, template_dir_computed, f"{FAILURE_HEADER}Your TEMPLATE_DIR setting does not point to the expected path. Check your configuration, and try again.{FAILURE_FOOTER}")

    def test_template_lookup_path(self):
        """
        Does the TEMPLATE_DIR value appear within the lookup paths for templates?
        """
        lookup_list = settings.TEMPLATES[0]['DIRS']
        found_path = False

        for entry in lookup_list:
            entry_normalised = os.path.normpath(entry)

            if entry_normalised == os.path.normpath(settings.TEMPLATE_DIR):
                found_path = True

        self.assertTrue(found_path, f"{FAILURE_HEADER}Your project's templates directory is not listed in the TEMPLATES>DIRS lookup list. Check your settings.py module.{FAILURE_FOOTER}")

    def test_templates_exist(self):
        """
        Do the index.html and about.html templates exist in the correct place?
        """
        home_path = os.path.join(self.ClubScoutGlasgow_templates_dir, 'index.html')
        about_path = os.path.join(self.ClubScoutGlasgow_templates_dir, 'about.html')
        base_path = os.path.join(self.ClubScoutGlasgow_templates_dir, 'base.html')
        club_path = os.path.join(self.ClubScoutGlasgow_templates_dir, 'club.html')
        login_path = os.path.join(self.ClubScoutGlasgow_templates_dir, 'login.html')
        clubs_path = os.path.join(self.ClubScoutGlasgow_templates_dir, 'clubs.html')
        signup_path = os.path.join(self.ClubScoutGlasgow_templates_dir, 'signup.html')

        self.assertTrue(os.path.isfile(home_path), f"{FAILURE_HEADER}Your home.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(about_path), f"{FAILURE_HEADER}Your about.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(base_path), f"{FAILURE_HEADER}Your base.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(club_path), f"{FAILURE_HEADER}Your club.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(login_path), f"{FAILURE_HEADER}Your login.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(clubs_path), f"{FAILURE_HEADER}Your clubs.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(signup_path), f"{FAILURE_HEADER}Your signup.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")



class Chapter4StaticMediaTests(TestCase):
    """
    A series of tests to check whether static files and media files have been setup and used correctly.
    Also tests for the two required files -- ClubScoutGlasgow.jpg and cat.jpg.
    """
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.static_dir = os.path.join(self.project_base_dir, 'static')
        self.media_dir = os.path.join(self.project_base_dir, 'media')

    def test_does_static_directory_exist(self):
        """
        Tests whether the static directory exists in the correct location -- and the images subdirectory.
        Also checks for the presence of ClubScoutGlasgow.jpg in the images subdirectory.
        """
        does_static_dir_exist = os.path.isdir(self.static_dir)
        does_images_static_dir_exist = os.path.isdir(os.path.join(self.static_dir, 'images'))
        does_myIcon_jpg_exist = os.path.isfile(os.path.join(self.static_dir, 'images', 'myIcon.png'))
        does_hive_jpg_exist = os.path.isfile(os.path.join(self.static_dir, 'images/ClubImages', 'hive1.jpg'))

        self.assertTrue(does_static_dir_exist, f"{FAILURE_HEADER}The static directory was not found in the expected location. Check the instructions in the book, and try again.{FAILURE_FOOTER}")
        self.assertTrue(does_images_static_dir_exist, f"{FAILURE_HEADER}The images subdirectory was not found in your static directory.{FAILURE_FOOTER}")
        self.assertTrue(does_hive1_jpg_exist, f"{FAILURE_HEADER}We couldn't locate the hive1.jpg image in the /static/images/ClubImages directory. If you think you've included the file, make sure to check the file extension. Sometimes, a JPG can have the extension .jpeg. Be careful! It must be .jpg for this test.{FAILURE_FOOTER}")
        self.assertTrue(does_myIcon_jpg_exist, f"{FAILURE_HEADER}We couldn't locate the myIcon.ong image in the /static/images/ directory. If you think you've included the file, make sure to check the file extension. It must be .png for this test.{FAILURE_FOOTER}")

    def test_does_media_directory_exist(self):
        """
        Tests whether the media directory exists in the correct location.
        Also checks for the presence of cat.jpg.
        """
        does_media_dir_exist = os.path.isdir(self.media_dir)
        does_cat_jpg_exist = os.path.isfile(os.path.join(self.media_dir, 'cat.jpg'))

        self.assertTrue(does_media_dir_exist, f"{FAILURE_HEADER}We couldn't find the /media/ directory in the expected location. Make sure it is in your project directory (at the same level as the manage.py module).{FAILURE_FOOTER}")
        self.assertTrue(does_cat_jpg_exist, f"{FAILURE_HEADER}We couldn't find the cat.jpg image in /media/. Check the file extension; this is a common pitfall. It should .jpg. Not .png, .gif, or .jpeg!{FAILURE_FOOTER}")

    def test_static_and_media_configuration(self):
        """
        Performs a number of tests on your Django project's settings in relation to static files and user upload-able files..
        """
        static_dir_exists = 'STATIC_DIR' in dir(settings)
        self.assertTrue(static_dir_exists, f"{FAILURE_HEADER}Your settings.py module does not have the variable STATIC_DIR defined.{FAILURE_FOOTER}")

        expected_path = os.path.normpath(self.static_dir)
        static_path = os.path.normpath(settings.STATIC_DIR)
        self.assertEqual(expected_path, static_path, f"{FAILURE_HEADER}The value of STATIC_DIR does not equal the expected path. It should point to your project root, with 'static' appended to the end of that.{FAILURE_FOOTER}")

        staticfiles_dirs_exists = 'STATICFILES_DIRS' in dir(settings)
        self.assertTrue(staticfiles_dirs_exists, f"{FAILURE_HEADER}The required setting STATICFILES_DIRS is not present in your project's settings.py module. Check your settings carefully. So many students have mistyped this one.{FAILURE_FOOTER}")
        self.assertEqual([static_path], settings.STATICFILES_DIRS, f"{FAILURE_HEADER}Your STATICFILES_DIRS setting does not match what is expected. Check your implementation against the instructions provided.{FAILURE_FOOTER}")

        staticfiles_dirs_exists = 'STATIC_URL' in dir(settings)
        self.assertTrue(staticfiles_dirs_exists, f"{FAILURE_HEADER}The STATIC_URL variable has not been defined in settings.py.{FAILURE_FOOTER}")
        self.assertEqual('/static/', settings.STATIC_URL, f"{FAILURE_HEADER}STATIC_URL does not meet the expected value of /static/. Make sure you have a slash at the end!{FAILURE_FOOTER}")

        media_dir_exists = 'MEDIA_DIR' in dir(settings)
        self.assertTrue(media_dir_exists, f"{FAILURE_HEADER}The MEDIA_DIR variable in settings.py has not been defined.{FAILURE_FOOTER}")

        expected_path = os.path.normpath(self.media_dir)
        media_path = os.path.normpath(settings.MEDIA_DIR)
        self.assertEqual(expected_path, media_path, f"{FAILURE_HEADER}The MEDIA_DIR setting does not point to the correct path. Remember, it should have an absolute reference to WADGroup8C_project/media/.{FAILURE_FOOTER}")

        media_root_exists = 'MEDIA_ROOT' in dir(settings)
        self.assertTrue(media_root_exists, f"{FAILURE_HEADER}The MEDIA_ROOT setting has not been defined.{FAILURE_FOOTER}")

        media_root_path = os.path.normpath(settings.MEDIA_ROOT)
        self.assertEqual(media_path, media_root_path, f"{FAILURE_HEADER}The value of MEDIA_ROOT does not equal the value of MEDIA_DIR.{FAILURE_FOOTER}")

        media_url_exists = 'MEDIA_URL' in dir(settings)
        self.assertTrue(media_url_exists, f"{FAILURE_HEADER}The setting MEDIA_URL has not been defined in settings.py.{FAILURE_FOOTER}")

        media_url_value = settings.MEDIA_URL
        self.assertEqual('/media/', media_url_value, f"{FAILURE_HEADER}Your value of the MEDIA_URL setting does not equal /media/. Check your settings!{FAILURE_FOOTER}")

    def test_context_processor_addition(self):
        """
        Checks to see whether the media context_processor has been added to your project's settings module.
        """
        context_processors_list = settings.TEMPLATES[0]['OPTIONS']['context_processors']
        self.assertTrue('django.template.context_processors.media' in context_processors_list, f"{FAILURE_HEADER}The 'django.template.context_processors.media' context processor was not included. Check your settings.py module.{FAILURE_FOOTER}")
