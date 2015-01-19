# To import libraries need to include below two lines
import sys
sys.path.insert(0, 'libs')

import json
import requests
import os
import jinja2
import webapp2
import models as proxy_models


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

PROXY_URL = "http://localhost:9000"

def send_to_server(proxy_url, request_to_send):
    path_qs = request_to_send.path_qs
    url = proxy_url + path_qs
    headers = request_to_send.headers
    headers.update({'Authorization': request_to_send.authorization})
    r = requests.request(
                     method=request_to_send.method,
                     url=url,
                     data=request_to_send.body,
                     headers=headers
                   )
    return r


class APIProxy(webapp2.RequestHandler):

    def get(self):
        if self.request.path != '/' and self.request.path != '/favicon.ico':
            self.common_call()
        else:
            # This else condition return for rendering the UI page.
            api_requests = proxy_models.APIRequest.query_api()
            template_values = {
                'api_requests': api_requests,
            }
            template = JINJA_ENVIRONMENT.get_template('index.html')
            self.response.write(template.render(template_values))

    def get_proxy_url(self):
        # Define the proxy url.
        return PROXY_URL

    def update_output(self, response):
        # If you want to modify the output which is returned by proxy server then 
        # use this.
        pass

    def common_call(self):
        proxy_url = self.get_proxy_url()
        r = send_to_server(proxy_url, self.request.copy())
        self.save_api_request(self.request, r.content, proxy_url)
        self.response.write(self.update_output(r))

    def post(self):
        self.common_call()

    def put(self):
        self.common_call()

    def head(self):
        self.common_call()

    def options(self):
        self.common_call()

    def delete(self):
        self.common_call()

    def trace(self):
        self.common_call()

    def save_api_request(self, request, output, host_url):
        api_request = proxy_models.APIRequest(
                   path=request.path, url=request.url,
                   method=request.method, request_body=request.body,
                   query_string=request.query_string,
                   headers=str(request.headers),
                   output=str(output),
                   authorization=str(request.authorization),
                   host_url=str(host_url)
                   )
        api_request.put()

# Routing
proxy_app = webapp2.WSGIApplication([(r'.*', APIProxy), ], debug=True)
