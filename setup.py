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
    url="https://github.com/xumaple/create-web-app",
    scripts=['create-web-app']
)
