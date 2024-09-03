from setuptools import setup, find_packages
import os


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="enigma",  
    version="0.1.0",
    author="Mateus Porto, Vitor Raia",
    author_email="vitortr@al.insper.edu.br",
    description="Um pacote minimalista em Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mateus1711-ctrl/enigma-.git",  
    packages=find_packages(),  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    entry_points={
        'console_scripts': [
            'enigma=enigma.enigma:main', 
        ],
    },
    install_requires=[  
        line.strip() for line in open("requirements.txt").readlines()
    ],
    include_package_data=True, 
    package_data={
        "enigma": ["img/*.png", "img/*.jpg", "img/*.webp"],  
    },
)
