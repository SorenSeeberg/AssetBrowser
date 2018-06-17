from server.auth import auth


class Session:

    def __init__(self, token: str, user: 'User', group: 'Group'):
        self.token = token
        self.user = user
        self.group = group

    def authenticate(self) -> bool:
        return auth.authenticate_user(self.token) and auth.authenticate_group(self.group.id)

