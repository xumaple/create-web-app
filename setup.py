try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="create-web-app",
    description="Create a Web App!",
    version="1.0",
    author="Maple Xu",
    author_email="maplexu2010@gmail.com",
    url="https://gitlab.eecs.umich.edu/akamil/canvas-tools",
    license="FIXME",
    packages=["create-web-app"],

    # Python command line utilities will be installed in a PATH-accessible bin/
    entry_points={
        'console_scripts': [
            'create-web-app = src.create-web-app:main',
        ]
    },
)
