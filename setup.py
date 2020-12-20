
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easy-password-generator",
    version="0.0.3",
    author="Sonia Ghongadi",
    author_email="author@example.com",
    description="A powerful but simple to use strong password generation library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/soniaghongadi/password-generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)