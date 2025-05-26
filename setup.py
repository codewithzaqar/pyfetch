from setuptools import setup, find_packages

setup(
    name="pyfetch",
    version="0.0.1",
    author="codewithzaqar",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pyfetch=pyfetch.__main__:main",
        ],
    },
)