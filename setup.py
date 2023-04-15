from setuptools import setup, find_packages

setup(
    name="carter-py",
    version="0.1.1",
    packages=find_packages(),
    install_requires = [
    "aiohttp==3.8.4",
    "aioresponses==0.7.4",
    "asynctest==0.13.0",
    "python-dotenv==1.0.0",
    "Requests==2.28.2",
    "responses==0.23.1",
    "setuptools==65.5.0"
    ],
    author="LazyLyrics",
    author_email="lazylyrics@icloud.com",
    description="A wrapper for the Carter API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LazyLyrics/carterpy",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
