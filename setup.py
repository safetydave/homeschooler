from setuptools import setup, find_packages

setup(name='homeschooler',
      version='0.1',
      description='Solution to Homeschool Shokunin Challenge',
      url='https://github.com/safetydave/homeschooler',
      author='David Colls',
      author_email='david dot colls at gmail com',
      license='MIT',
      python_requires='>=3.6.0',
      packages=find_packages("src"),
      package_dir={"": "src"},
      install_requires=['numpy'],
      zip_safe=False)
