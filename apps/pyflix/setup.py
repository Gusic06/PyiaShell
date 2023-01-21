from setuptools import setup, find_packages

setup (
    name="pyflix.py",
    version="1.0.1",
    packages=find_packages(),
    install_requires = [
        "colorama",
        "playsound"
    ],
    entry_points = """
    [console_scripts]
    pyflix=pyflix:pyflix
    """
)