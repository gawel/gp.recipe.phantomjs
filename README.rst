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
    phantomjs-url-base. Defaults to https://phantomjs.googlecode.com/files/
    Set this if you want to use your own mirror for phantomjs.

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

