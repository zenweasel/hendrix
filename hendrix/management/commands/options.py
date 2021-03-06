from django.core.management.base import BaseCommand

from hendrix import defaults

from optparse import make_option, OptionParser


HX_OPTION_LIST = BaseCommand.option_list + (
    make_option(
        '--reload',
        action='store_true',
        dest='reload',
        default=False,
        help="Flag that watchdog should restart the server when changes to the codebase occur"
    ),
    make_option(
        '-l', '--loud',
        action='store_true',
        dest='loud',
        default=False,
        help="Show warnings"
    ),
    make_option(
        '--http_port',
        type=int,
        dest='http_port',
        default=defaults.HTTP_PORT,
        help='Enter a port number for the server to serve content.'
    ),
    make_option(
        '--https_port',
        type=int,
        dest='https_port',
        default=defaults.HTTPS_PORT,
        help='Enter an ssl port number for the server to serve secure content.'
    ),
    make_option(
        '--cache_port',
        type=int,
        dest='cache_port',
        default=defaults.CACHE_PORT,
        help='Enter an cache port number to serve cached content.'
    ),
    make_option(
        '-g', '--global_cache',
        dest='global_cache',
        action='store_true',
        default=False,
        help='Make it so that there is only one cache server'
    ),
    make_option(
        '-n', '--nocache',
        dest='nocache',
        action='store_true',
        default=False,
        help='Disable page cache'
    ),
    make_option(
        '-w', '--workers',
        type=int,
        dest='workers',
        default=0,
        help='Number of processes to run'
    ),
    make_option(
        '--key',
        type=str,
        dest='key',
        default=None,
        help='Absolute path to SSL private key'
    ),
    make_option(
        '--cert',
        type=str,
        dest='cert',
        default=None,
        help='Absolute path to SSL public certificate'
    ),
    make_option(
        '--fd',
        type=str,
        dest='fd',
        default=None,
        help='DO NOT SET THIS'
    ),
    make_option(
        '-d', '--daemonize',
        dest='daemonize',
        action='store_true',
        default=False,
        help='Run in the background'
    ),
    make_option(
        '--dev',
        dest='dev',
        action='store_true',
        default=False,
        help='Runs in development mode. Meaning it uses the development wsgi handler subclass'
    ),
    make_option(
        '--wsgi',
        dest='wsgi',
        type=str,
        default=None,
        help=(
            'Overrides the use of django settings for use in testing. N.B. This'
            ' option is not for use with hx or hx.py'
        )
    )
)


def options():
    """
    A helper function that returns a dictionary of the default key-values pairs
    """
    parser = OptionParser(option_list=HX_OPTION_LIST)
    return vars(parser.parse_args([])[0])
