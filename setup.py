import setuptools

setuptools.setup(
  name="{{proj}}", # replace quoted text with name of package unders src
  version="0.0.0",
  description="python project run in docker",
  packages=setuptools.find_packages("src"),
  package_dir={"": "src"},
)
