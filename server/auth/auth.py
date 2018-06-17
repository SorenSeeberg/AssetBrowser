
def authenticate_user(user_token: str) -> bool:

    if user_token:
        return True
    else:
        return False


def authenticate_group(group_token: str) -> bool:

    if group_token:
        return True
    else:
        return False

