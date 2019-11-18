from getresponse_api_wrapper.resources import BaseResource


class Multimedia(BaseResource):

    def get_images(self, fields, results, page):
        params = {
            "fields": fields,
            "perPage": results,
            "page": page
        }
        response = self.request.get("/multimedia", params=params)
        return response
