from setuptools import setup, find_packages


with open('README.md', mode='r') as f:
    long_description = f.read()

setup(name='h2libpy',
      version='1.0',
      description='Python interface for the h2lib library',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/marekhummel/h2libpy',
      author='Marek Hummel',
      author_email='marek.hummel3@gmail.com',
      license='LGPL-3.0',
      packages=find_packages(exclude=['examples']),
      package_data={'h2libpy': ['libh2.so']},
      include_package_data=True,
      python_requires='>=3.8',)
