from setuptools import setup, find_packages

setup(
    name="uptime_monitor",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "flask",
        "requests",
        "pytest"
    ]
)


