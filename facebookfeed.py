import facebook
import urllib
from urllib.parse import urlparse
import subprocess
import warnings
import ast

class FacebookUser(facebook.GraphAPI):
    def __init__(self):
        facebook.GraphAPI(self.GenAuthToken())
        # self.driver = webdriver.Chrome()


    def GenAuthToken(self):

        warnings.filterwarnings('ignore', category=DeprecationWarning)

        # Parameters of the app and the id of the profile you want to mess with.
        FACEBOOK_APP_ID = '1270792462960074'
        FACEBOOK_APP_SECRET = '9849029974f9c81962bc48790197509a'
        # FACEBOOK_PROFILE_ID = '1350166609'        # Hide deprecation warnings. The facebook module isn't that up-to-date (facebook.GraphAPIError).


        # Trying to get an access token. Very awkward.
        oauth_args = dict(client_id=FACEBOOK_APP_ID, client_secret=FACEBOOK_APP_SECRET, grant_type='client_credentials')
        oauth_curl_cmd = ['curl',
                          'https://graph.facebook.com/oauth/access_token?' + urllib.parse.urlencode(oauth_args)]

        oauth_response = subprocess.Popen(oauth_curl_cmd,
                                          stdout=subprocess.PIPE,
                                          stderr=subprocess.PIPE).communicate()[0]

        try:
            oauth_access_token = urllib.parse.parse_qs(str(oauth_response))["b'access_token"][0].strip("'")

            # print(oauth_access_token)

            scope = 'email,public_profile,user_friends'

            # login_args = dict(client_id=FACEBOOK_APP_ID, redirect_uri="https://www.facebook.com/connect/login_success.html")
            # login_url = 'https://www.facebook.com/v2.8/dialog/oauth?' + urllib.parse.urlencode(login_args)

            login_args = dict(access_token=oauth_access_token, scope=scope)
            login_url = 'https://graph.facebook.com/v2.6/device/login?' + urllib.parse.urlencode(login_args)


            print(login_url)
            #
            login_curl_cmd = ['curl', login_url]

            login_response = \
                ast.literal_eval(
                    str(subprocess.Popen(login_curl_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]).strip("b'"))

            # print(login_response)

            # self.driver.get(str(login_url))
            #
            # self.driver.find_element_by_css_selector("#email").send_keys("jennysalas@me.com")
            # self.driver.find_element_by_css_selector("#pass").send_keys("tigerw33!a")
            # self.driver.find_element_by_css_selector("#u_0_q").click()

            if login_response["error"]:
                self.set = False
                print(login_response["error"]["message"])
                # statement(render_template('error', error=login_response["error"]["message"]))
            else:
                self.set = True

            return oauth_access_token

        except KeyError:
            print('Unable to grab an access token!')
            exit()

    def GetData(self, node, args):
        #node & Args must be passed as type string, must pass at least an empty string

        # concatenate url with the node
        url = "https://graph.facebook.com"+node

        # generate a list with parts to run under curl
        curl_cmd = ["curl", url, urllib.parse.urlencode(args)]

        # return a dictonary (possible dictionaries underneath, need to analyze any possible data types before continuing.
        return ast.literal_eval(
            str(subprocess.Popen(curl_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[
                    0]).strip("b'"))

    def ParseNewsFeed(self, data):
        # Need to figure out hierarchy for newsfeed data before parsing. Must authenticate login to sample the data.

        # First iterate through newsfeed
            # Check post type

            # if post type == string, have alexa reed
            # elif post type == photo, use clarifai to identify image
            # elif post type == video, use clarifai to describe video, ask user if they would like to play audio only
        pass

    def AlexaReadPost(self, string):

        # just use a statement
        pass

    def AlexaDescribePhoto(self, url):
        # use statement with
        pass

    def AlexaDescribeVideo(self, url):
        pass