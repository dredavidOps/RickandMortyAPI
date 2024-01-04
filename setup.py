from setuptools import setup, find_packages

setup(
    name="rnm",
    version="0.1.0",
    description="A simple CLI application",
    author="David",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
        "click" 
        "requests",
    ],
    # ...
    entry_points={
        'console_scripts': [
            'rnm = rnm.utils:main',
        ],
    },
)
