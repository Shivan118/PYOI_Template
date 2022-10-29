import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "<YOUR REPO NAME>"
AUTHOR_USER_NAME = "< YOUR USER NAME>"
SRC_REPO = "<YOUR REPO NAME>"
AUTHOR_EMAIL = "<YOUR EMAIL ID>"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)