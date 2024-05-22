from flask import Blueprint, request

from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    user_id = args.get("id")
    name = args.get("name")
    age = args.get("age")
    occupation = args.get("occupation")

    result = []

    for i in args.keys():
        for user in USERS:
            if (i == "id") and (user_id is not None) and (user_id == user.get("id")):
                result.append(user)

            if (i == "name") and (name is not None) and (name in user.get("name")):
                result.append(user)

            if (i == "age") and (age is not None) and (age == str(user.get("age"))):
                result.append(user)

            if (i == "occupation") and (occupation is not None) and (occupation in user.get("occupation")):
                result.append(user)

    if not result:
        return USERS
    else:
        return result
