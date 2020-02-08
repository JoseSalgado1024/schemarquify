import os
from setuptools import find_packages, setup

# readme_file = os.path.join(os.path.dirname(__file__), 'README.md')
# with open(readme_file) as readme:
#     README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

README = """
Forms
===


"""

setup(
    name="py3-tokko-forms-flavor",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    license="MIT License",
    description="Tokko Forms flavor.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="El Jose Salgado",
    author_email="jsalgado@tokko.com",
    install_requires=[
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)