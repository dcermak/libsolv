import sys
import re
from pathlib import Path
from skbuild import setup

def get_version():
    version_file = Path(__file__).parent / "VERSION.cmake"
    content = version_file.read_text()

    major = re.search(r'SET\(LIBSOLV_MAJOR "(\d+)"\)', content)
    minor = re.search(r'SET\(LIBSOLV_MINOR "(\d+)"\)', content)
    patch = re.search(r'SET\(LIBSOLV_PATCH "(\d+)"\)', content)

    if not all([major, minor, patch]):
        raise ValueError("Could not parse version from VERSION.cmake")

    return f"{major.group(1)}.{minor.group(1)}.{patch.group(1)}"

setup(
    name="libsolv",
    version=get_version(),
    description="Python bindings for libsolv, a package dependency solver",
    long_description=Path("README").read_text(),
    long_description_content_type="text/plain",
    author="Michael Schroeder",
    author_email="mls@suse.de",
    url="https://github.com/openSUSE/libsolv",
    license="BSD-3-Clause",
    packages=['solv'],
    package_dir={'solv': 'bindings/python3'},
    python_requires=">=3.6",
    cmake_args=[
        "-DENABLE_PYTHON3=ON",
        "-DENABLE_STATIC=ON",
        "-DDISABLE_SHARED=ON",
        "-DCMAKE_POSITION_INDEPENDENT_CODE=ON",
        f"-DPYTHON3_EXECUTABLE={sys.executable}",
        "-DPYTHON3_INSTALL_DIR=bindings/python3",
        "-DCMAKE_INSTALL_COMPONENT=python3",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: C",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Software Distribution",
    ],
)
