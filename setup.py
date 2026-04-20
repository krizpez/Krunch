from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="krunch",
    version="0.1.0",
    author="krizpez",
    author_email="",
    description="Android Virtual Machine USB Bootloader Application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/krizpez/Krunch",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Click>=8.1.0",
        "PyYAML>=6.0",
        "psutil>=5.9.0",
        "libusb1>=3.1.0",
        "paramiko>=3.3.0",
    ],
    entry_points={
        "console_scripts": [
            "krunch=krunch.cli:main",
        ],
    },
)