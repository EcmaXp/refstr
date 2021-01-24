from setuptools import setup

with open('README.md', encoding='utf-8') as fp:
    long_description = fp.read()

setup(
    name="refstr",
    version="1.0",
    description="Referenceable String",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/EcmaXp/refstr",
    author="EcmaXp",
    author_email="ecmaxp+refstr@ecmaxp.pe.kr",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
    ],
    keywords="typing, reference, string",
    py_modules=["refstr"],
    python_requires='>=2.7, >=3',
)
