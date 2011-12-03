from setuptools import setup


setup(
    name = "edge",
    version = "0.3.2",
    url = "http://pypi.python.org/pypi/edge",
    license = "BSD",
    description = "Python bindings for Directed Edge's API",
    author = "Directed Edge",
    py_modules = ["directed_edge"],
    install_requires = ["httplib2"]
)
