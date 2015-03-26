from setuptools import setup, find_packages


setup(
    name='resolve_link',
    version='1.0.0',
    description='Resolve complete/partial URLs against a canonical target URL',
    long_description=open('README.rst').read(),
    keywords=[
        'resolve',
        'link',
        'url',
        'target',
        'canonical'
    ],
    author='Todd Wolfson',
    author_email='todd@twolfson.com',
    url='https://github.com/underdogio/python-resolve-link',
    download_url='https://github.com/underdogio/python-resolve-link/archive/master.zip',
    packages=find_packages(),
    license='MIT',
    install_requires=open('requirements.txt').readlines(),
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
