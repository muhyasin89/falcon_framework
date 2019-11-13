import falcon

class MainResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        starter = {
            'quote': (
                "Welcome this is just starter project it will scale by time"
            ),
            'author': 'muhyasin'
        }

        resp.media = starter

api = falcon.API()
api.add_route('/', MainResource())