from setuptools import setup

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")
    
setup(name='daftlistings',
      version='0.9',
      description='A web scraper for Daft.ie',
      long_description=long_descr,
      url='https://github.com/AnthonyBloomer/daftlistings',
      author='Anthony Bloomer',
      keywords=['daft', 'web scraping'],
      author_email='ant0@protonmail.ch',
      license='MIT',
      packages=['daftlistings'],
      install_requires=[
          'beautifulsoup4',
      ],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          "Topic :: Software Development :: Libraries",
          'Programming Language :: Python :: 2.7'
      ],
      zip_safe=False)
