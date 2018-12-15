from mozilla_django_oidc.auth import OIDCAuthenticationBackend as MozillaOIDCAuthenticationBackend


class OIDCAuthenticationBackend(MozillaOIDCAuthenticationBackend):

    def filter_users_by_claims(self, claims):
        username = claims.get('preferred_username')
        if not username:
            return self.UserModel.objects.none()
        return self.UserModel.objects.filter(username__iexact=username)

    def create_user(self, claims):
        username = claims.get('preferred_username')
        if not username:
            return None
        return self.UserModel.objects.create_user(username)
