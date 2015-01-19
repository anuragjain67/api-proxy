from google.appengine.ext import ndb


class APIRequest(ndb.Model):
    """Models an individual Guestbook entry."""
    path = ndb.StringProperty(indexed=True)
    url = ndb.StringProperty(indexed=True)
    method = ndb.StringProperty(indexed=True)
    request_body = ndb.StringProperty(indexed=False)
    query_string = ndb.StringProperty(indexed=True)
    authorization = ndb.StringProperty(indexed=True)
    request_time = ndb.DateTimeProperty(auto_now=True, indexed=True)
    headers = ndb.StringProperty(indexed=True)
    output = ndb.StringProperty(indexed=False)
    host_url = ndb.StringProperty(indexed=True)

    @classmethod
    def query_api(cls):
        return cls.query().order(-cls.request_time)
