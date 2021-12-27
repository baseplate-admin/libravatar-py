from typing import Dict
from hashlib import md5

import httpx
from httpx._models import Response

from ._dns import query_dns

__doc__ = """
s:
    It will automatically be squared.
        For example:
            If you input 12 in here
            It will automatically become 12x12
d:
    Lets take a look at a example:
        Email = 'someone@example.com'
        But Libravatar doesn't have a picture of 'someone@example.com'
        So if we set a fallback url it will point to there.
        If we set d = 'https://images.unsplash.com/photo-1640532050771-0274b43075bf?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=720&q=80'
        It will get the unsplash image.


    But d supports other providers too:
        404: return a 404 error (file not found) instead of an image
        mm or mp: return an image containing a simple, fixed silhouette of a person
        identicon: return an image containing a random geometric pattern
        monsterid: return an image containing a random monsterid
        wavatar: return an image containing a random wavatar
        retro: return an image containing a random retro-looking, 8-bits arcade style pixel-art
        robohash: return an image containing a random robohash
        pagan: return an image containing a random retro adventure game character using pagan
"""


async def httpx_get_avatar(
    email: str,
    params: Dict[str, int | str] = {
        "s": 0,
        "d": "",
        "f": "",
    },
) -> Response:
    """
    Parameter:
        email : str

        params:
            s: int = Picture size ( size in pixel )
            d: str = Default URL for missing images ( fallback url )
            f: str = Force default ( 'y' for forcing default image )
    """
    # Use async and http2
    client = httpx.AsyncClient(http2=True, follow_redirects=True)

    # Email needs to be hashed with MD5.
    # https://wiki.libravatar.org/api/
    email_hash = md5(email.lower().encode()).hexdigest()

    # Gets the base avatar url
    # Will get Https when available
    # Fallback to http
    avatar_url = await query_dns(email)

    # Format the address like this
    # https://seccdn.libravatar.org/avatar/00df28f68f674fb6c4e59dc00ded9df3
    # The avatar_url has something like this https://seccdn.libravatar.org/avatar/
    # Dont add unnecessary backslash
    formatted_email = f"{avatar_url}{email_hash}"

    result: Response = await client.get(
        formatted_email,
        params=params,
    )

    await client.aclose()
    return result
