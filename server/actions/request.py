from server.actions import actions


class Request:

    def __init__(self, session: 'Session', action_name: str, args):
        self.__session__ = session
        self.action_name = action_name
        self.args = args

    def request(self):

        if self.__session__.authenticate():
            result = self.__execute_action__()

        else:
            result = "No Authentication"

        return result

    def __execute_action__(self):

        if self.action_name == 'previews':
            actions.previews(self.__session__)
        return f'executing {self.action_name}'
