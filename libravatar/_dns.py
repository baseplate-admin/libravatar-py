import re
from dns.resolver import NXDOMAIN, resolve


async def query_dns(email: str) -> str:
    """
    Adapted from:
        https://wiki.libravatar.org/api/

    Function:
        This module checks if the service is fedarated or not.
        With automatic DNS redirection.

    Parameters:
        email: str

    Returns:
        baseurl: str
    """

    domain = email.split("@")[-1]

    try:
        answers = resolve("_avatars._tcp." + domain, "SRV")
        hostname = re.sub(
            "\.$", "", str(answers[0].target)
        )  # query returns "example.com." and while http requests are fine with this, https most certainly do not consider "example.com." and "example.com" to be the same.
        port = str(answers[0].port)
        if port == "443":
            baseurl = "https://" + hostname + "/avatar/"
        else:
            baseurl = "http://" + hostname + ":" + port + "/avatar/"
    except NXDOMAIN:
        baseurl = "https://seccdn.libravatar.org/avatar/"

    return baseurl
