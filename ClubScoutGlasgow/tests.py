import os
import importlib
import warnings
from django.urls import reverse
from django.test import TestCase
from django.conf import settings
from ClubScoutGlasgow.models import Club, UserProfile, Review
from django.contrib.auth.models import User

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
        directory_exists = os.path.isdir(os.path.join(self.project_base_dir, 'WADGroup8C'))
        urls_module_exists = os.path.isfile(os.path.join(self.project_base_dir, 'WADGroup8C', 'urls.py'))

        self.assertTrue(directory_exists, f"{FAILURE_HEADER}Your WADGroup8C configuration directory doesn't seem to exist. Did you use the correct name?{FAILURE_FOOTER}")
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

        self.project_urls_module = importlib.import_module('WADGroup8C.urls')

    def test_view_exists(self):
        """
        Does the home() view exist in ClubScoutGlasgow's views.py module?
        """
        name_exists = 'home' in self.views_module_listing
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
        self.assertEquals(reverse('ClubScoutGlasgow:home'), '/ClubScoutGlasgow/home/', f"{FAILURE_HEADER}The home URL lookup failed. Check ClubScoutGlasgow's urls.py module. You're missing something in there.{FAILURE_FOOTER}")

    def test_response(self):
        """
        Does the response from the server contain the required string?
        """
        response = self.client.get(reverse('ClubScoutGlasgow:home'))

        self.assertEqual(response.status_code, 200, f"{FAILURE_HEADER}Requesting the home page failed. Check your URLs and view.{FAILURE_FOOTER}")



class ClubsPageTests(TestCase):
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
        name_exists = 'clubs' in self.views_module_listing
        is_callable = callable(self.views_module.clubs)

        self.assertTrue(name_exists, f"{FAILURE_HEADER}We couldn't find the view for your clubs view!{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}Check you have defined clubs view correctly. We can't execute it.{FAILURE_FOOTER}")

    def test_mapping_exists(self):
        """
        Checks whether the about view has the correct URL mapping.
        """
        self.assertEquals(reverse('ClubScoutGlasgow:clubs'), '/ClubScoutGlasgow/clubs/', f"{FAILURE_HEADER}Your about URL mapping is either missing or mistyped.{FAILURE_FOOTER}")

    def test_response(self):

        response = self.client.get(reverse('ClubScoutGlasgow:clubs'))

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
        Do the templates exist in the correct place?
        """
        home_path = os.path.join(self.ClubScoutGlasgow_templates_dir, 'home.html')
        base_path = os.path.join(self.ClubScoutGlasgow_templates_dir, 'base.html')
        club_path = os.path.join(self.ClubScoutGlasgow_templates_dir, 'club.html')
        login_path = os.path.join(self.ClubScoutGlasgow_templates_dir, 'login.html')
        clubs_path = os.path.join(self.ClubScoutGlasgow_templates_dir, 'clubs.html')
        search_path = os.path.join(self.ClubScoutGlasgow_templates_dir, 'search.html')
        signup_path = os.path.join(self.ClubScoutGlasgow_templates_dir, 'signup.html')
        add_club_path = os.path.join(self.ClubScoutGlasgow_templates_dir, 'add_club.html')
        write_review_path = os.path.join(self.ClubScoutGlasgow_templates_dir, 'write_review.html')



        self.assertTrue(os.path.isfile(home_path), f"{FAILURE_HEADER}Your home.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(base_path), f"{FAILURE_HEADER}Your base.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(club_path), f"{FAILURE_HEADER}Your club.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(login_path), f"{FAILURE_HEADER}Your login.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(clubs_path), f"{FAILURE_HEADER}Your clubs.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(signup_path), f"{FAILURE_HEADER}Your signup.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(search_path), f"{FAILURE_HEADER}Your signup.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(add_club_path), f"{FAILURE_HEADER}Your signup.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(write_review_path), f"{FAILURE_HEADER}Your signup.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")

class StaticMediaTests(TestCase):
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
        Also checks for the presence of myIcon.png in the images subdirectory.
        """
        does_static_dir_exist = os.path.isdir(self.static_dir)
        does_images_static_dir_exist = os.path.isdir(os.path.join(self.static_dir, 'images'))
        does_myIcon_png_exist = os.path.isfile(os.path.join(self.static_dir, 'images', 'myIcon.png'))
        does_css_static_dir_exist = os.path.isdir(os.path.join(self.static_dir, 'css'))
        does_js_static_dir_exist = os.path.isdir(os.path.join(self.static_dir, 'javascript'))
        does_instagram_icon_png_exist = os.path.isfile(os.path.join(self.static_dir, 'images', 'instagram-icon.png'))
        does_bootstrap_css_exist = os.path.isfile(os.path.join(self.static_dir, 'css', 'bootstrap.min.css'))
        does_carousel_css_exist = os.path.isfile(os.path.join(self.static_dir, 'css', 'carousel.css'))
        does_dashboard_css_exist = os.path.isfile(os.path.join(self.static_dir, 'css', 'dashboard.css'))
        does_CSG_js_exist = os.path.isfile(os.path.join(self.static_dir, 'javascript', 'CSG.js'))

        self.assertTrue(does_static_dir_exist, f"{FAILURE_HEADER}The static directory was not found in the expected location. Check the instructions in the book, and try again.{FAILURE_FOOTER}")
        self.assertTrue(does_images_static_dir_exist, f"{FAILURE_HEADER}The images subdirectory was not found in your static directory.{FAILURE_FOOTER}")
        self.assertTrue(does_css_static_dir_exist, f"{FAILURE_HEADER}The css subdirectory was not found in your static directory.{FAILURE_FOOTER}")
        self.assertTrue(does_js_static_dir_exist, f"{FAILURE_HEADER}The javascript subdirectory was not found in your static directory.{FAILURE_FOOTER}")
        self.assertTrue(does_instagram_icon_png_exist, f"{FAILURE_HEADER}The javascript subdirectory was not found in your static directory.{FAILURE_FOOTER}")
        self.assertTrue(does_myIcon_png_exist, f"{FAILURE_HEADER}We couldn't locate the myIcon.png image in the /static/images/  {FAILURE_FOOTER}")
        self.assertTrue(does_instagram_icon_png_exist, f"{FAILURE_HEADER}We couldn't locate the instagram-icon.png image in the /static/images/  {FAILURE_FOOTER}")
        self.assertTrue(does_bootstrap_css_exist, f"{FAILURE_HEADER}We couldn't locate the bootstrap.min.css in the /static/css/  {FAILURE_FOOTER}")
        self.assertTrue(does_dashboard_css_exist, f"{FAILURE_HEADER}We couldn't locate the dashboard.css in the /static/css/  {FAILURE_FOOTER}")
        self.assertTrue(does_CSG_js_exist, f"{FAILURE_HEADER}We couldn't locate the CSG.js file in the /static/javascript/  {FAILURE_FOOTER}")


    def test_does_media_directory_exist(self):
        """
        Tests whether the media directory exists in the correct location.
        Also checks for the presence of cat.jpg.
        """
        does_media_dir_exist = os.path.isdir(self.media_dir)
        does_firewater1_jpg_exist = os.path.isfile(os.path.join(self.media_dir,'images/ClubImages', 'firewater1.jpg'))
        does_firewater2_jpeg_exist = os.path.isfile(os.path.join(self.media_dir,'images/ClubImages', 'firewater2.jpeg'))
        
        self.assertTrue(does_media_dir_exist, f"{FAILURE_HEADER}We couldn't find the /media/ directory in the expected location. Make sure it is in your project directory (at the same level as the manage.py module).{FAILURE_FOOTER}")
        self.assertTrue(does_firewater1_jpg_exist, f"{FAILURE_HEADER}We couldn't find the firewater1.jpg image in /media/images/Clubimages/. Check the file extension; this is a common pitfall. {FAILURE_FOOTER}")
        self.assertTrue(does_firewater2_jpeg_exist, f"{FAILURE_HEADER}We couldn't find the firewater1.jpg image in /media/images/Clubimages/. Check the file extension; this is a common pitfall. {FAILURE_FOOTER}")

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
        self.assertEqual(expected_path, media_path, f"{FAILURE_HEADER}The MEDIA_DIR setting does not point to the correct path. Remember, it should have an absolute reference to WADGroup8C/media/.{FAILURE_FOOTER}")

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



class DatabaseConfigurationTests(TestCase):
    """
    Is your database configured as the book states?
    These tests should pass if you haven't tinkered with the database configuration.
    N.B. Some of the configuration values we could check are overridden by the testing framework -- so we leave them.
    """
    def setUp(self):
        pass
    
    def does_gitignore_include_database(self, path):
        """
        Takes the path to a .gitignore file, and checks to see whether the db.sqlite3 database is present in that file.
        """
        f = open(path, 'r')
        
        for line in f:
            line = line.strip()
            
            if line.startswith('db.sqlite3'):
                return True
        
        f.close()
        return False
    
    def test_databases_variable_exists(self):
        """
        Does the DATABASES settings variable exist, and does it have a default configuration?
        """
        self.assertTrue(settings.DATABASES, f"{FAILURE_HEADER}Your project's settings module does not have a DATABASES variable, which is required. Check the start of Chapter 5.{FAILURE_FOOTER}")
        self.assertTrue('default' in settings.DATABASES, f"{FAILURE_HEADER}You do not have a 'default' database configuration in your project's DATABASES configuration variable. Check the start of Chapter 5.{FAILURE_FOOTER}")
    
    def test_gitignore_for_database(self):
        """
        If you are using a Git repository and have set up a .gitignore, checks to see whether the database is present in that file.
        """
        git_base_dir = os.popen('git rev-parse --show-toplevel').read().strip()
        
        if git_base_dir.startswith('fatal'):
            warnings.warn("You don't appear to be using a Git repository for your codebase. Although not strictly required, it's *highly recommended*. Skipping this test.")
        else:
            gitignore_path = os.path.join(git_base_dir, '.gitignore')
            
            if os.path.exists(gitignore_path):
                self.assertTrue(self.does_gitignore_include_database(gitignore_path), f"{FAILURE_HEADER}Your .gitignore file does not include 'db.sqlite3' -- you should exclude the database binary file from all commits to your Git repository.{FAILURE_FOOTER}")
            else:
                warnings.warn("You don't appear to have a .gitignore file in place in your repository. We ask that you consider this! Read the Don't git push your Database paragraph in Chapter 5.")


class ModelTests(TestCase):
    """
    Are the models set up correctly, and do all the required attributes (post exercises) exist?
    """
    def setUp(self):
        club_fw= Club.objects.get_or_create(name='Firewater', entryPrice = 6,location="341 Sauchiehall St, Glasgow G2 3HW", 
                                            openingHours="19:00-03:00", instagram ="https://www.instagram.com/firewater_glasgow/?hl=en", facebook = "https://www.facebook.com/firewaterglasgowofficial", 
                                            website = "https://www.facebook.com/firewaterglasgowofficial", 
                                            mapSrc = "https://maps.google.com/maps?q=firewater&t=&z=13&ie=UTF8&iwloc=&output=embed", 
                                            about = "fun", noOfRooms =2) 
        
        user1 = User.objects.create_user("john")
        userprof_j = UserProfile.objects.get_or_create(user = user1, email = 'john@john.com', age = 19 )


        fw = Club.objects.get_or_create(name='Firewater')[0]
        john  = UserProfile.objects.get_or_create(user = user1)[0]
        
        Review.objects.get_or_create(club=fw,
                                   reviewer=john,
                                   typeOfCrowd='loud',
                                   popularNight='Tuesday',
                                   avgQueueTime = 10,
                                   staffFriendliness = 3,
                                   qualityOfSafety = 3,
                                   overallRating = 3,
                                   additionalComments = 'meh')
    
    def test_club_model(self):
        """
        Runs a series of tests on the Club model.
        Do the correct attributes exist?
        """
        club_fw = Club.objects.get(name='Firewater')
        self.assertEqual(club_fw.entryPrice, 6, f"{FAILURE_HEADER}Tests on the Club model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
        self.assertEqual(club_fw.location, "341 Sauchiehall St, Glasgow G2 3HW", f"{FAILURE_HEADER}Tests on the Club model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
        self.assertEqual(club_fw.noOfRooms, 2, f"{FAILURE_HEADER}Tests on the Club model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
        self.assertEqual(club_fw.openingHours, "19:00-03:00", f"{FAILURE_HEADER}Tests on the Club model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
        self.assertEqual(club_fw.averageOverallRating, 0, f"{FAILURE_HEADER}Tests on the Club model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
        self.assertEqual(club_fw.instagram, "https://www.instagram.com/firewater_glasgow/?hl=en", f"{FAILURE_HEADER}Tests on the Club model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
        self.assertEqual(club_fw.website, "https://www.facebook.com/firewaterglasgowofficial", f"{FAILURE_HEADER}Tests on the Club model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")       
        self.assertEqual(club_fw.facebook, "https://www.facebook.com/firewaterglasgowofficial", f"{FAILURE_HEADER}Tests on the Club model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
        self.assertEqual(club_fw.mapSrc, "https://maps.google.com/maps?q=firewater&t=&z=13&ie=UTF8&iwloc=&output=embed", f"{FAILURE_HEADER}Tests on the Club model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
        self.assertEqual(club_fw.about, "fun", f"{FAILURE_HEADER}Tests on the Club model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
    
    def test_Review_model(self):
        """
        Runs some tests on the Review model.
        Do the correct attributes exist?
        """
        user = User.objects.get_or_create('john')[0]
        john  = UserProfile.objects.get_or_create(user = user)[0]

        fw = Club.objects.get_or_create(name='Firewater')[0]
        review = Review.objects.get_or_create(club = fw, reviewer = john)

            
        self.assertEqual(review.reviewer, john, f"{FAILURE_HEADER}Tests on the Review model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}{review}")
        self.assertEqual(review.typeOfCrowd, 'loud', f"{FAILURE_HEADER}Tests on the Review model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
        self.assertEqual(review.popularNight, 'Tuesday', f"{FAILURE_HEADER}Tests on the Review model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
        self.assertEqual(review.avgQueueTime, 10, f"{FAILURE_HEADER}Tests on the Review model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
        self.assertEqual(review.staffFriendliness, 3, f"{FAILURE_HEADER}Tests on the Review model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
        self.assertEqual(review.qualityOfSafety, 3, f"{FAILURE_HEADER}Tests on the Review model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
        self.assertEqual(review.overallRating, 3, f"{FAILURE_HEADER}Tests on the Review model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
        self.assertEqual(review.additionalComments, 'meh', f"{FAILURE_HEADER}Tests on the Review model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
        self.assertEqual(review.reviewLikes, 0, f"{FAILURE_HEADER}Tests on the Review model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
        self.assertEqual(review.club, fw, f"{FAILURE_HEADER}Tests on the Review model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")

    def test_UserProfile_model(self):

        user = User.objects.get_or_create('john')[0]
        john  = UserProfile.objects.get_or_create(user = user)[0]
        userprof = UserProfile.objects.get(user=user)
        
        
        self.assertEqual(userprof.user, user, f"{FAILURE_HEADER}Tests on the User model - user failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
        self.assertEqual(userprof.age, 19, f"{FAILURE_HEADER}Tests on the User model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
        self.assertEqual(userprof.email, 'john@john.com', f"{FAILURE_HEADER}Tests on the User model failed. Check you have all required attributes and try again.{FAILURE_FOOTER}")
    


class AdminInterfaceTests(TestCase):
    """
    A series of tests that examines the authentication functionality (for superuser creation and logging in), and admin interface changes.
    Have all the admin interface tweaks been applied, and have the two models been added to the admin app?
    """
    def setUp(self):
        """
        Create a superuser account for use in testing.
        Logs the superuser in, too!
        """
        User.objects.create_superuser('testAdmin', 'email@email.com', 'adminPassword123')
        self.client.login(username='testAdmin', password='adminPassword123')
        
        club_fw= Club.objects.get_or_create(name='Firewater', entryPrice = 6,location="341 Sauchiehall St, Glasgow G2 3HW", 
                                    openingHours="19:00-03:00", 
                                    instagram ="https://www.instagram.com/firewater_glasgow/?hl=en", facebook = "https://www.facebook.com/firewaterglasgowofficial", 
                                    website = "https://www.facebook.com/firewaterglasgowofficial", 
                                    mapSrc = "https://maps.google.com/maps?q=firewater&t=&z=13&ie=UTF8&iwloc=&output=embed", 
                                    about = "fun", 
                                    noOfRooms =2)

        user1 = User.objects.create_user("john")
        userprof_j = UserProfile.objects.get_or_create(user = user1, email = 'john@john.com', age = 19 )[0]
        fw = Club.objects.get_or_create(name='Firewater')[0]
        Review.objects.get_or_create(club=fw,
                                   reviewer=userprof_j,
                                   typeOfCrowd='loud',
                                   popularNight='Tuesday',
                                   avgQueueTime = 10,
                                   staffFriendliness = 3,
                                   qualityOfSafety = 3,
                                   overallRating = 3,
                                   additionalComments = 'meh')
        
    def test_admin_interface_accessible(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200, f"{FAILURE_HEADER}The admin interface is not accessible. Check that you didn't delete the 'admin/' URL pattern in your project's urls.py module.{FAILURE_FOOTER}")
    
    def test_models_present(self):
        """
        Checks whether the two models are present within the admin interface homepage -- and whether Rango is listed there at all.
        """
        response = self.client.get('/admin/')
        response_body = response.content.decode()
                
        # Check each model is present.
        self.assertTrue('Club' in response_body, f"{FAILURE_HEADER}The club model was not found in the admin interface.{FAILURE_FOOTER}")
        self.assertTrue('Review' in response_body, f"{FAILURE_HEADER}The Review model was not found in the admin interface. {FAILURE_FOOTER}")
        self.assertTrue('User profiles' in response_body, f"{FAILURE_HEADER}The UserProfile model was not found in the admin interface.{FAILURE_FOOTER}")

    def test_Review_display_changes(self):
        """
        Checks to see whether the Review model has had the required changes applied for presentation in the admin interface.
        """
        response = self.client.get('/admin/ClubScoutGlasgow/review/')
        response_body = response.content.decode()
        
        # Headers -- are they all present?
        self.assertTrue('<div class="text"><a href="?o=1">ReviewID</a></div>' in response_body, f"{FAILURE_HEADER}The 'reviewID' column could not be found in the admin interface for the Review model -- if it is present, is it in the correct order?{FAILURE_FOOTER}")
        self.assertTrue('<div class="text"><a href="?o=2">Reviewer</a></div>' in response_body, f"{FAILURE_HEADER}The 'club' column could not be found in the admin interface for the Review model -- if it is present, is it in the correct order?{FAILURE_FOOTER}")
        self.assertTrue('<div class="text"><a href="?o=3">Club</a></div>' in response_body, f"{FAILURE_HEADER}The 'Url' (stylised that way!) column could not be found in the admin interface for the Review model -- if it is present, is it in the correct order?{FAILURE_FOOTER}")
        self.assertTrue('<div class="text"><a href="?o=4">ReviewDate</a></div>' in response_body, f"{FAILURE_HEADER}The 'Url' (stylised that way!) column could not be found in the admin interface for the Review model -- if it is present, is it in the correct order?{FAILURE_FOOTER}")

    

class PopulationScriptTests(TestCase):
    """
    Tests whether the population script puts the expected data into a test database.
    All values that are explicitly mentioned in the book are tested.
    Expects that the population script has the populate() function, as per the book!
    """
    def setUp(self):
        """
        Imports and runs the population script, calling the populate() method.
        """
        try:
            import population_script
        except ImportError:
            raise ImportError(f"{FAILURE_HEADER}Could not import the population_script. Check it's in the right location (the first tango_with_django_project directory).{FAILURE_FOOTER}")
        
        if 'populate' not in dir(population_script):
            raise NameError(f"{FAILURE_HEADER}The populate() function does not exist in the population_script module. This is required.{FAILURE_FOOTER}")

        # Call the population script -- any exceptions raised here do not have fancy error messages to help readers.
        population_script.populate()
    
    def test_clubs(self):

        clubs = Club.objects.filter()
        clubs_len = len(clubs)
        clubs_strs = map(str, clubs)

        self.assertEqual(clubs_len, 5, f"{FAILURE_HEADER}Expecting 5 clubs to be created from the population_script module; found {clubs_len}.{FAILURE_FOOTER}")
        self.assertTrue('Firewater' in clubs_strs, f"{FAILURE_HEADER}The club 'Firewater' was expected but not created by population_script.{FAILURE_FOOTER}")
        self.assertTrue('SWG3' in clubs_strs, f"{FAILURE_HEADER}The club 'SWG3' was expected but not created by population_script.{FAILURE_FOOTER}")
        self.assertTrue('Sub Club' in clubs_strs, f"{FAILURE_HEADER}The club 'Sub Club' was expected but not created by population_script.{FAILURE_FOOTER}")
    
    def test_Reviews(self):
  
        reviews = Review.objects.filter()
        reviews_len = len(reviews)
        
        self.assertEqual(reviews_len, 4, f"{FAILURE_HEADER}Expecting 4 reviews to be created from the population_script module; found {reviews_len}.{FAILURE_FOOTER}")
  

class ClubsPageTests(TestCase):

    def test_ensure_clubs_appear_on_clubs_page(self):
        response = self.client.get('/ClubScoutGlasgow/clubs/')
        self.assertTrue('<h4><a href ="/ClubScoutGlasgow/club/firewater>Firewater</a></h4>' in response_body, f"{FAILURE_HEADER}The Firewatercould not be found in the clubs Page{FAILURE_FOOTER}")
        self.assertTrue('<h4><a href ="/ClubScoutGlasgow/club/hive>hive</a></h4>' in response_body, f"{FAILURE_HEADER}The Hive could not be found in the clubs Page{FAILURE_FOOTER}")
        self.assertTrue('<h4><a href ="/ClubScoutGlasgow/club/swg3>SWG3</a></h4>' in response_body, f"{FAILURE_HEADER}The SWG3 could not be found in the clubs Page{FAILURE_FOOTER}")
        self.assertTrue('<h4><a href ="/ClubScoutGlasgow/club/sub-club>Sub Club</a></h4>' in response_body, f"{FAILURE_HEADER}The Sub Club could not be found in the clubs Page{FAILURE_FOOTER}")
        self.assertTrue('<h4><a href ="/ClubScoutGlasgow/club/the-garage>The Garage</a></h4>' in response_body, f"{FAILURE_HEADER}The The Garage could not be found in the clubs Page{FAILURE_FOOTER}")

