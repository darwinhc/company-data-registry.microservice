from dataclasses import dataclass


@dataclass
class UserInfo:
    """UserInfo model for the database.

    Attributes
    ----------
    user_id : str
        The unique identifier for the user.
    user_name : str
        The name of the user.
    user_email : str
        The email address of the user.
    """
    user_id: str
    user_name: str
    user_email: str

