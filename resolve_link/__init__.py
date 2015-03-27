# Load in our dependencies
import re
try:
    from urlparse import urlsplit, urlunsplit
except ImportError:
    from urllib.parse import urlsplit, urlunsplit

# Define our constants
TLD_REGEXP = r'\.([a-zA-Z]*?)$'


# Define our library
def resolve_link(src_url, target_url):
    """Resolve complete/partials URLs against canonical target URL

    :param str src_url: URL/partial URL to be resolving from
    :param str target_url: Canonical URL to try to match if on the same domain
    :returns str ret_val: Completed URL formatted via `urllib.parse`
    """
    # Parse the src URL
    src_url_parts = urlsplit(src_url)

    # If there isn't a scheme (e.g. no `http://`)
    if not src_url_parts.scheme:
        # With no scheme, we have everything in path. Add on `//` and force treatment of `netloc`
        tmp_src_url = '//{src_url}'.format(src_url=src_url)
        tmp_src_url_parts = urlsplit(tmp_src_url)

        # If this new hostname has a TLD (e.g. `google.com`), then keep it as the `src_url`
        # DEV: We are trading accuracy for size (technically not all dots mean a tld)
        #   If we want to be accurate, use the Python equivalent of https://github.com/ramitos/tld.js/blob/305a285fd8f5d618417178521d8729855baadb37/src/tld.js
        if (tmp_src_url_parts.netloc and re.search(TLD_REGEXP, tmp_src_url_parts.netloc)):
          src_url = tmp_src_url
          src_url_parts = tmp_src_url_parts

    # Convert our `namedtuple` of `src_url_parts` to an ordered dict to make it editable
    # https://hg.python.org/cpython/file/2.7/Lib/urlparse.py#l121
    # https://docs.python.org/2/library/collections.html#collections.somenamedtuple._asdict
    src_url_dict = src_url_parts._asdict()

    # Fallback path (e.g. `/hello` in `www.google.com/hello`)
    if src_url_dict['path'] == '':
        src_url_dict['path'] = '/'

    # If we still have no `scheme` (e.g. no `http://`)
    if src_url_dict['scheme'] == '':
        # Parse our target URL
        target_url_parts = urlsplit(target_url)

        # If the src URL has a `netloc` (e.g. `www.google.com`)
        if src_url_dict['netloc']:
          # If the target `netloc` is the same as our original, add on the target schem (e.g. `http://`)
          if src_url_dict['netloc'] == target_url_parts.netloc:
            src_url_dict['scheme'] = target_url_parts.scheme
          # Otherwise, default to HTTP
          else:
            src_url_dict['scheme'] = 'http'
        # Otherwise, pickup the target scheme and netloc
        else:
          src_url_dict['scheme'] = target_url_parts.scheme
          src_url_dict['netloc'] = target_url_parts.netloc

    # Return the completed src URL
    # https://docs.python.org/2/library/urlparse.html#urlparse.urlsplit
    return urlunsplit((src_url_dict['scheme'], src_url_dict['netloc'], src_url_dict['path'],
                       src_url_dict['query'], src_url_dict['fragment']))
