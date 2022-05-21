from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='sony_bravia_api',
    version='1.01',
    license='MIT',
    author='Alec J. Davidson',
    author_email='alecjdavidson@outlook.com',
    description='Sony Bravia API for controlling Sony Bravia Smart TV',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlecJDavidson/sony_bravia_api.git",
    project_urls={
        "Bug Tracker": "https://github.com/AlecJDavidson/sony_bravia_api.git/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        'requests',
    ],
)
