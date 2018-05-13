from setuptools import setup, find_packages

setup(name='hello-world',
      version='0.1',
      description='pip packaging test',
      url='https://github.com/XDeschuyteneer/pip-test',
      author='Xavier Deschuyteneer',
      author_email='xavier.deschuyteneer@gmail.com',
      license='MIT',
      py_modules=['helloworld.helloworld', 'helloworld.mylib'],
      entry_points={
        'console_scripts': [
            'hello-world=helloworld.helloworld:main',
        ],
      },
      install_requires=[
          'stomp.py',
          'websocket-client',
      ],
      dependency_links=['git+https://github.com/gschizas/websocket-client.git@patch-1#egg=wxPython'],
      zip_safe=False)