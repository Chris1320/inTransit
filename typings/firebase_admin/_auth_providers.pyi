"""
This type stub file was generated by pyright.
"""

from firebase_admin import _auth_utils

"""Firebase auth providers management sub module."""
MAX_LIST_CONFIGS_RESULTS = ...
class ProviderConfig:
    """Parent type for all authentication provider config types."""
    def __init__(self, data) -> None:
        ...
    
    @property
    def provider_id(self):
        ...
    
    @property
    def display_name(self):
        ...
    
    @property
    def enabled(self):
        ...
    


class OIDCProviderConfig(ProviderConfig):
    """Represents the OIDC auth provider configuration.

    See https://openid.net/specs/openid-connect-core-1_0-final.html.
    """
    @property
    def issuer(self):
        ...
    
    @property
    def client_id(self):
        ...
    
    @property
    def client_secret(self):
        ...
    
    @property
    def id_token_response_type(self):
        ...
    
    @property
    def code_response_type(self):
        ...
    


class SAMLProviderConfig(ProviderConfig):
    """Represents he SAML auth provider configuration.

    See http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html.
    """
    @property
    def idp_entity_id(self):
        ...
    
    @property
    def sso_url(self):
        ...
    
    @property
    def x509_certificates(self): # -> list[Any]:
        ...
    
    @property
    def callback_url(self):
        ...
    
    @property
    def rp_entity_id(self):
        ...
    


class ListProviderConfigsPage:
    """Represents a page of AuthProviderConfig instances retrieved from a Firebase project.

    Provides methods for traversing the provider configs included in this page, as well as
    retrieving subsequent pages. The iterator returned by ``iterate_all()`` can be used to iterate
    through all provider configs in the Firebase project starting from this page.
    """
    def __init__(self, download, page_token, max_results) -> None:
        ...
    
    @property
    def provider_configs(self):
        """A list of ``AuthProviderConfig`` instances available in this page."""
        ...
    
    @property
    def next_page_token(self):
        """Page token string for the next page (empty string indicates no more pages)."""
        ...
    
    @property
    def has_next_page(self): # -> bool:
        """A boolean indicating whether more pages are available."""
        ...
    
    def get_next_page(self): # -> Self | None:
        """Retrieves the next page of provider configs, if available.

        Returns:
            ListProviderConfigsPage: Next page of provider configs, or None if this is the last
            page.
        """
        ...
    
    def iterate_all(self): # -> _ProviderConfigIterator:
        """Retrieves an iterator for provider configs.

        Returned iterator will iterate through all the provider configs in the Firebase project
        starting from this page. The iterator will never buffer more than one page of configs
        in memory at a time.

        Returns:
            iterator: An iterator of AuthProviderConfig instances.
        """
        ...
    


class _ListOIDCProviderConfigsPage(ListProviderConfigsPage):
    @property
    def provider_configs(self): # -> list[OIDCProviderConfig]:
        ...
    


class _ListSAMLProviderConfigsPage(ListProviderConfigsPage):
    @property
    def provider_configs(self): # -> list[SAMLProviderConfig]:
        ...
    


class _ProviderConfigIterator(_auth_utils.PageIterator):
    @property
    def items(self):
        ...
    


class ProviderConfigClient:
    """Client for managing Auth provider configurations."""
    PROVIDER_CONFIG_URL = ...
    def __init__(self, http_client, project_id, tenant_id=..., url_override=...) -> None:
        ...
    
    def get_oidc_provider_config(self, provider_id): # -> OIDCProviderConfig:
        ...
    
    def create_oidc_provider_config(self, provider_id, client_id, issuer, display_name=..., enabled=..., client_secret=..., id_token_response_type=..., code_response_type=...): # -> OIDCProviderConfig:
        """Creates a new OIDC provider config from the given parameters."""
        ...
    
    def update_oidc_provider_config(self, provider_id, client_id=..., issuer=..., display_name=..., enabled=..., client_secret=..., id_token_response_type=..., code_response_type=...): # -> OIDCProviderConfig:
        """Updates an existing OIDC provider config with the given parameters."""
        ...
    
    def delete_oidc_provider_config(self, provider_id): # -> None:
        ...
    
    def list_oidc_provider_configs(self, page_token=..., max_results=...): # -> _ListOIDCProviderConfigsPage:
        ...
    
    def get_saml_provider_config(self, provider_id): # -> SAMLProviderConfig:
        ...
    
    def create_saml_provider_config(self, provider_id, idp_entity_id, sso_url, x509_certificates, rp_entity_id, callback_url, display_name=..., enabled=...): # -> SAMLProviderConfig:
        """Creates a new SAML provider config from the given parameters."""
        ...
    
    def update_saml_provider_config(self, provider_id, idp_entity_id=..., sso_url=..., x509_certificates=..., rp_entity_id=..., callback_url=..., display_name=..., enabled=...): # -> SAMLProviderConfig:
        """Updates an existing SAML provider config with the given parameters."""
        ...
    
    def delete_saml_provider_config(self, provider_id): # -> None:
        ...
    
    def list_saml_provider_configs(self, page_token=..., max_results=...): # -> _ListSAMLProviderConfigsPage:
        ...
    


