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
            buildout['buildout']['parts-directory'], name
        )

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
                version = self.options.get('phantomjs-version', '1.7.0')
                if sys.platform == 'linux2':
                    url = (
                        'https://phantomjs.googlecode.com/'
                        'files/phantomjs-%s-linux-i686.tar.bz2'
                    ) % version
                elif sys.platform == 'darwin':
                    url = (
                        'https://phantomjs.googlecode.com/'
                        'files/phantomjs-%s-macosx.zip'
                    ) % version
                else:
                    raise RuntimeError('Please specify a phantomjs-url')
            self.download(url)
        if 'casperjs' not in binaries:
            self.download(
                self.options.get(
                    'casperjs-url',
                    'https://github.com/n1k0/casperjs/tarball/1.0.0-RC4'
                )
            )

        binaries = self.get_binaries()
        for f in binaries.values():
            os.chmod(f, 0777)

        self.options['arguments'] = repr(binaries)
        self.options['eggs'] = 'gp.recipe.phantomjs'
        self.options['entry-points'] = '\n'.join([
            '%s=gp.recipe.phantomjs.script:main' % s for s in binaries
        ])
        from zc.recipe.egg import Scripts
        rscripts = Scripts(self.buildout, self.name, self.options)
        return rscripts.install()

    update = install
