#!/usr/bin/env python
from setuptools import setup, find_packages
import os

# Read the version from version.py without importing the package
version_file = os.path.join(os.path.dirname(__file__), 'src', 'enzywizard_embedding', 'version.py')
with open(version_file) as f:
    exec(f.read())  # defines __version__ variable

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="enzywizard-embedding",
    version=__version__,                     # dynamically read from version.py
    author="bioinfbrad",
    description=(
        "Generate protein sequence embeddings from a cleaned FASTA "
        "using the ESM-2 protein language model."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bioinfbrad/enzywizard-embedding",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
    install_requires=[
        "torch>=2.6.0",
        "fair-esm>=2.0.0",               # ESM-2 model
        "biopython>=1.86",
        "biotite>=0.39.0",
        "numpy>=1.23.5",
        "scipy>=1.15.2",
        "packaging>=26.1",
        "pyparsing>=3.3.2",
        "requests>=2.33.1",
        "tqdm>=4.67.3",
        "typing-extensions>=4.15.0",
    ],
    entry_points={
        "console_scripts": [
            "enzywizard-embedding = enzywizard_embedding.cli:main",
        ],
    },
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
)
