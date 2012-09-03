# -*- coding: utf-8 -*-
"""Recipe phantomjs"""
import glob
import sys
import os


class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        self.install_dir = os.path.join(
                                buildout['buildout']['parts-directory'], name)

    def get_binaries(self):
        binaries = glob.glob(os.path.join(self.install_dir, '*', 'bin', '*js'))
        binaries = dict([(os.path.basename(p), p) for p in binaries])
        if 'bootstrap.js' in binaries:
            del binaries['bootstrap.js']
        return binaries

    def download(self, url):
        from hexagonit.recipe.download import Recipe as Download
        options = self.options
        options['url'] = url
        dl = Download(self.buildout, self.name, options)
        dl.install()

    def install(self):
        """Installer"""
        binaries = self.get_binaries()
        if 'phantomjs' not in binaries:
            url = self.options.get('phantomjs-url', None)
            if not url:
                if sys.platform == 'linux2':
                    url = ('https://phantomjs.googlecode.com/'
                       'files/phantomjs-1.6.1-linux-x86_64-dynamic.tar.bz2')
                elif sys.platform == 'darwin':
                    url = ('https://phantomjs.googlecode.com/'
                        'files/phantomjs-1.6.1-macosx-static.zip')
                else:
                    raise RuntimeError('Please specify a phantomjs-url')
            self.download(url)
        if 'casperjs' not in binaries:
            self.download(self.options.get('casperjs-url',
                            'https://github.com/n1k0/casperjs/tarball/0.6.10'))

        binaries = self.get_binaries()
        self.options['arguments'] = repr(binaries)
        self.options['eggs'] = 'gp.recipe.phantomjs'
        self.options['entry-points'] = '\n'.join([
            '%s=gp.recipe.phantomjs.script:main' % s for s in binaries
            ])
        from zc.recipe.egg import Scripts
        rscripts = Scripts(self.buildout, self.name, self.options)
        return rscripts.install()

    update = install
