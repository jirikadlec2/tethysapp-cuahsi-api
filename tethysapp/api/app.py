from tethys_sdk.base import TethysAppBase, url_map_maker


class Api(TethysAppBase):
    """
    Tethys app class for api.
    """

    name = 'api'
    index = 'api:home'
    icon = 'api/images/api_logo1.png'
    package = 'api'
    root_url = 'api'
    color = '#9b59b6'
        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='api',
                           controller='api.controllers.home'),
                    UrlMap(name='list_apps_help',
                            url='list_apps_help',
                            controller='api.controllers.list_apps_help'),
                    UrlMap(name='list_apps',
                            url='list_apps',
                            controller='api.controllers.list_apps'),
        )
        return url_maps