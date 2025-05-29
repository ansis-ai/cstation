from setuptools import find_packages, setup

setup(
    name="cstation",
    py_modules=["cstation"],
    packages=find_packages(exclude=["etc", "etc.*"]),
    package_dir={"": "."},
)
