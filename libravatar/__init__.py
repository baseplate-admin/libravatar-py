import asyncio
from typing import Dict

from httpx._models import Response
from ._query import httpx_get_avatar


def libravatar_url(email: str, params: Dict[str, int | str]) -> str:
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


def libravatar_img_tag(email: str, params: Dict[str, int | str]) -> str:
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
    result = f"<img src={url} alt='Avatar for {email}' />"
    return result


def libravatar_raw_image(email: str, params: Dict[str, int | str]) -> bytes:
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
    Parameter:
        any
    Returns:
        any
    """
    return httpx_get_avatar(*args, **kwargs)
