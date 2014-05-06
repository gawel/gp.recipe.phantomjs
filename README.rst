Buildout recipe to install phantomjs/casperjs

Supported options
=================

The recipe supports the following options:

.. Note to recipe author!
   ----------------------
   For each option the recipe uses you should include a description
   about the purpose of the option, the format and semantics of the
   values it accepts, whether it is mandatory or optional and what the
   default value is if it is omitted.

phantomjs-url
    Url to download phantomjs

phantomjs-url-base
    If phantomjs-url is not specified, this recipe downloads phantomjs from
    phantomjs-url-base. Defaults to https://bitbucket.org/ariya/phantomjs/downloads/.
    Set this if you want to use your own mirror for phantomjs.

phantomjs-url-template
    If phantomjs-url and phantomjs-url-template are
    not specified, you can set a template which will populate various
    variables. The variables should be wrapped in {}, and the
    following values are supported:

    * arch: the architecture. x86_64 or i686
    * phantom_platform: the platform, following the format dictated by the standard phantomjs url (e.g. linux, macosx)
    * phantom_extension: the extension, as specified by the format dictated by the standard phantomjs url (e.g. tar.bz2, zip)
    * platform: the platform, as specified by sys.platform (e.g. linux, darwin)
    * version: the version of phantomjs

phantomjs-version
    Try to retreive phantomjs url from version

casperjs-url
    Url to download casperjs


Example usage
=============

We'll start by creating a buildout that uses the recipe::

    >>> write('buildout.cfg',
    ... """
    ... [buildout]
    ... parts = casperjs
    ...
    ... [casperjs]
    ... recipe = gp.recipe.phantomjs
    ... """)

    >>> system('buildout')

    >>> ls('bin')
    -  buildout
    -  casperjs
    -  phantomjs
