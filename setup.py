from setuptools import setup

setup(name='secfilings',
      version='0.1',
      description='A simple utility to get some SEC forms for companies that file.',
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
