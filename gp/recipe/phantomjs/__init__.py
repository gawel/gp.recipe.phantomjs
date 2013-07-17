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
        if sys.platform.startswith('win'):
            binaries.extend(glob.glob(os.path.join(self.install_dir, '*', '*.exe')))
        rv = {}
        for p in binaries:
            bname = os.path.basename(p)
            if bname.lower().endswith('.js'):
                continue
            if bname.lower().endswith('.exe'):
                bname = bname[:-4]
            rv[bname] = p
        return rv

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
                version = self.options.get('phantomjs-version', '1.9.1')
                default_base = 'https://phantomjs.googlecode.com/files'
                url_base = self.options.get('phantomjs-url-base', default_base)
                if sys.platform.startswith('linux'):
                    arch = 'x86_64' in os.uname() and 'x86_64' or 'i686'
                    url = (
                        '%s/phantomjs-%s-linux-%s.tar.bz2'
                    ) % (url_base, version, arch)
                elif sys.platform == 'darwin':
                    url = (
                        '%s/phantomjs-%s-macosx.zip'
                    ) % (url_base, version)
                elif sys.platform.startswith('win'):
                    url = (
                        '%s/phantomjs-%s-windows.zip'
                    ) % (url_base, version)
                else:
                    raise RuntimeError('Please specify a phantomjs-url')
            self.download(url)
        if 'casperjs' not in binaries:
            url = self.options.get(
                    'casperjs-url',
                    'https://github.com/n1k0/casperjs/tarball/1.0.0-RC4')
            if url:
                self.download(url)

        binaries = self.get_binaries()
        for f in binaries.values():
            os.chmod(f, 0o777)

        self.options['arguments'] = repr(binaries)
        self.options['eggs'] = 'gp.recipe.phantomjs'
        self.options['entry-points'] = '\n'.join([
            '%s=gp.recipe.phantomjs.script:main' % s for s in binaries
        ])
        from zc.recipe.egg import Scripts
        rscripts = Scripts(self.buildout, self.name, self.options)
        return rscripts.install()

    update = install
