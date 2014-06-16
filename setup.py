# coding=utf-8
"""
Реализация API сайта cinemate.cc на языке python.
"""
import os
import sys
import codecs
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from pip.req import parse_requirements


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)


basedir = os.path.dirname(__file__)


def get_version():
    with open(os.path.join(basedir, 'cinemate/version.py')) as f:
        variables = {}
        exec(f.read(), variables)
        return variables['VERSION']


def get_requirements(filename):
    requirements_path = os.path.join(basedir, filename)
    requirements = parse_requirements(requirements_path)
    return [str(r.req) for r in requirements]


setup(
    name='cinemate',
    version=get_version(),
    url='https://github.com/Pentusha/cinemate/',
    license='BSD',
    author='Ivan Larin',
    author_email='pentusha@gmail.com',
    description='cinemate.cc api',
    long_description=codecs.open('README.rst', encoding="utf-8").read(),
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    tests_require=get_requirements('requirements_tests.txt'),
    cmdclass={'test': Tox},
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[
        # As from https://pypi.python.org/pypi?:action=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: Russian',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
)
