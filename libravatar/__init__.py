import asyncio

from typing import Dict

from httpx._models import Response
from ._query import httpx_get_avatar


def libravatar_url(email: str, params: Dict[str, int | str] = {}) -> str:
    """
    Parameter:
        email : str

        params:
            s: int = Picture size ( size in pixel )
            d: str = Default URL for missing images ( fallback url )
            f: str = Force default ( 'y' for forcing default image )
    Returns:
        url:str
    """
    return asyncio.run(httpx_get_avatar(email, params)).url


def libravatar_img_tag(
    email: str, _alt: str = "Avatar for {}", params: Dict[str, int | str] = {}
) -> str:
    """
    Parameter:
        email : str

        params:
            s: int = Picture size ( size in pixel )
            d: str = Default URL for missing images ( fallback url )
            f: str = Force default ( 'y' for forcing default image )
    Returns:
        <img src={url} alt="Avatar for {email}' />
    """
    url = asyncio.run(httpx_get_avatar(email, params)).url
    alt = _alt.format(email)

    result = f"<img src={url} alt='{alt}' />"
    return result


def libravatar_raw_image(email: str, params: Dict[str, int | str] = {}) -> bytes:
    """
    Parameter:
        email : str

        params:
            s: int = Picture size ( size in pixel )
            d: str = Default URL for missing images ( fallback url )
            f: str = Force default ( 'y' for forcing default image )
    Returns:
        Raw binary data of the image
    """

    return asyncio.run(httpx_get_avatar(email, params)).read()


async def libravatar_raw_query(*args, **kwargs) -> Response:
    """
    Function:
        Provides raw access to lower level API
    params:
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
    return await httpx_get_avatar(*args, **kwargs)
