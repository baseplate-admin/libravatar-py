import pathlib
from setuptools import setup, find_packages


long_description = (pathlib.Path(__file__).parent.resolve() / "README.rst").read_text(
    encoding="utf-8"
)

packages = ["libravatar"]


package_data = {
    "": ["libravatar/*"],
}
extras_require = {}

install_requires = [
    "httpx[http2]",
    "dnspython",
]

setup_kwargs = setup(
    name="libravatar-py",
    version="0.0.1",
    description="A libravatar client for Python thats built on modern Technology",
    long_description=long_description,
    author="baseplate-admin",
    author_email="zarifahanf@outlook.com",
    # 'maintainer': 'baseplate-admin',
    # 'maintainer_email': None,
    keywords="python3 avatar libravatar async httpx",
    url="https://github.com/baseplate-admin/libravatar-py",
    packages=packages,
    package_data=package_data,
    include_package_data=True,
    install_requires=install_requires,
    extras_require=extras_require,
    # zip_safe=False,
    python_requires=">=3.7",
    license="GPLv3",
    platforms="any",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only ",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
