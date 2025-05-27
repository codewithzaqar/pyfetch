from setuptools import setup, find_packages

setup(
    name="pyfetch",
    version="0.0.2",
    author="codewithzaqar",
    description="A Python-based CLI system information tool inspired by Neofetch",
    packages=find_packages(),
    install_requires=["psutil>=5.9.0", "colorama>=0.4.6"],
    entry_points={
        "console_scripts": [
            "pyfetch=pyfetch.__main__:main",
        ],
    },
    python_requires=">=3.6",
    include_package_data=True,
)