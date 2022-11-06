from setuptools import setup, find_packages

setup(
    name="metacrax",
    version="0.0.1",
    packages=find_packages(),
    author="amanraj-bose",
    author_email="amanraj90770124@gmail.com",
    install_requires=["scikit-learn", "joblib", "pyfiglet", "numpy", "pandas", "seaborn", "matplotlib", "python-nmap"],
    description="It is allow you to hack the metasploitable 2 and it is only made up for beginners.",
    url="https://github.com/amanraj-bose/metacrax",
    entry_points = {"console_scripts": ['metacrax = tool:USER']},
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
    ],
)


