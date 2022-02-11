from setuptools import find_packages, setup

install_requires = open("requirements.txt").read().strip().split("\n")
dev_requires = open("requirements_dev.txt").read().strip().split("\n")

readme = ""
with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="{{ cookiecutter.collection_name }}",
    description="{{ cookiecutter.collection_short_description }}",
    license="Apache License 2.0",
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.email }}",
    keywords="prefect",
    url="https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.collection_name }}",
    long_description=readme,
    long_description_content_type="text/markdown",
    version="{{ cookiecutter.version }}",
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
