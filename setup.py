import setuptools
import re

# versioning ------------
VERSIONFILE="filterimage/__init__.py"
getversion = re.search( r"^__version__ = ['\"]([^'\"]*)['\"]", open(VERSIONFILE, "rt").read(), re.M)
if getversion:
    new_version = getversion.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

# Setup ------------
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     python_requires='>=3',
     name='filterimage',
     version=new_version,
     author="Darnell Love, Jamar Bailey III, Miles Adedjouma",
     author_email="darnell.love@bison.howard.edu",
     description="Python package for my filterimage.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/darnell-love27/Image_Filters",
     packages=setuptools.find_packages(), # Searches throughout all dirs for files to include
     include_package_data=True, # Must be true to include files depicted in MANIFEST.in
     license_files=["LICENSE"],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
