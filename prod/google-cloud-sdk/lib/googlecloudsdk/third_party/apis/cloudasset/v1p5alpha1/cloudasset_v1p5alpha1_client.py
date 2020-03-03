"""Generated client library for cloudasset version v1p5alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudasset.v1p5alpha1 import cloudasset_v1p5alpha1_messages as messages


class CloudassetV1p5alpha1(base_api.BaseApiClient):
  """Generated client library for service cloudasset version v1p5alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://cloudasset.googleapis.com/'
  MTLS_BASE_URL = u''

  _PACKAGE = u'cloudasset'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1p5alpha1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'CloudassetV1p5alpha1'
  _URL_VERSION = u'v1p5alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new cloudasset handle."""
    url = url or self.BASE_URL
    super(CloudassetV1p5alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.assets = self.AssetsService(self)

  class AssetsService(base_api.BaseApiService):
    """Service class for the assets resource."""

    _NAME = u'assets'

    def __init__(self, client):
      super(CloudassetV1p5alpha1.AssetsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists assets with time and resource types and returns paged results in.
response.

      Args:
        request: (CloudassetAssetsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListAssetsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1p5alpha1/{v1p5alpha1Id}/{v1p5alpha1Id1}/assets',
        http_method=u'GET',
        method_id=u'cloudasset.assets.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'assetTypes', u'contentType', u'pageSize', u'pageToken', u'readTime'],
        relative_path=u'v1p5alpha1/{+parent}/assets',
        request_field='',
        request_type_name=u'CloudassetAssetsListRequest',
        response_type_name=u'ListAssetsResponse',
        supports_download=False,
    )