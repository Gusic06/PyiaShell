from setuptools import setup, find_packages
setup (
    name="pythonia",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "rich",
        "pyvim"
    ],
    entry_points = """
    [console_scripts]
    pyia = PyiaShell:pyia
    """
)