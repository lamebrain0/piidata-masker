from setuptools import setup, find_packages

setup(
    name="pii-masking",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "regex>=2023.0.0",
    ],
    python_requires=">=3.7",
    description="A library for masking PII (Personally Identifiable Information) in text",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lamebrain0/piidata-masker",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)