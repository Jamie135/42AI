from setuptools import setup, find_packages

setup(
    name="my-minipack",
    version="1.0.0",
    packages=find_packages(),
    author="pbureera",
    author_email="pbureera@student.42.fr",
    description="A simple package with a progress bar and a logger.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Jamie135/42AI/tree/main/Python/Module02/ex04/my_minipack",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Students",
        "Topic :: Education",
        "Topic :: HowTo",
        "Topic :: Package",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires='>=3.6',
)
