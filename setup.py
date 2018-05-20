from setuptools import setup
with open('README.md') as f:
    long_description = f.read()

setup(name='secfilings',
      version='0.4',
      description='A simple utility to get some SEC forms for companies that file.',
      long_description=long_description,
      long_description_content_type='text/markdown',  
      url='http://github.com/sman1/secfilings',
      author='NGT Apps',
      author_email='developer@ngtapps.com',
      license='MIT',
      install_requires=[
          'requests',
	  'bs4',
	  'lxml',
      ],
      packages=['secfilings'],
      zip_safe=False)
