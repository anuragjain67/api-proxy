# What is it about ?
If you want to proxy your apis and then want to do some analysis it will help.

1. You need specify the PROXY_URL in the api_proxy.py, or you can use get_proxy_url() function.
2. Point your application client to localhost:8080 or google app url.
3. If you want to return different output to the client then you can use update_output function.
4. go to browser: http://localhost:8080/ it will list all logged urls.


# Local Setup Steps:
1. download google app sdk [https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python]
2. ./google_appengine/dev_appserver.py ./api_proxy/
it will create webserver on http://localhost:8080

# Deploying to Google App Engine
1. Install Google Developer tools, and install Google App Engine for Python (gcloud components update gae-python)
2. Create a new project https://console.developers.google.com/project
3. Modify the name of the project in app.yaml
4. Run gcloud auth login to login to Google
5. Run appcfg.py update . in the project folder to deploy the code to Google App Engine


# Todos
1. Update the UI.
2. Provide the more hook.
3. Write test cases.
4. https verification.

