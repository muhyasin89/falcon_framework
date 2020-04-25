import falcon, json

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

class ObjRequestClass():
    def on_get(self, req, resp):
        content = {
            'name': "Muh yasin",
            'age': 31,
            'country': "Indonesia"
        }

        resp.body = json.dumps(content)

api = falcon.API()
api.add_route('/', MainResource())
api.add_route('/test', ObjRequestClass())