from setuptools import find_packages, setup

install_requires = open("requirements.txt").read().strip().split("\n")
dev_requires = open("requirements_dev.txt").read().strip().split("\n")

readme = ""
with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="prefect-collection",
    description="Prefect Collection Template contains all the boilerplate that you need to create a Prefect collection.",
    license="Apache License 2.0",
    author="Arthur Dent",
    author_email="arthur.dent@example.com",
    keywords="prefect",
    url="https://github.com/arthur_dent/prefect-collection",
    long_description=readme,
    long_description_content_type="text/markdown",
    version="0.1.0",
    packages=find_packages(exclude=("tests", "docs")),
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require={"dev": dev_requires},
    classifiers=[
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
    ],
)
