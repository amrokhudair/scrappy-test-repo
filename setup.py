from setuptools import setup, find_packages
import os


version = '0.9.5'

base_dir = os.path.dirname(__file__)


setup(
      name='ikcon-protobuf',
      version=version,
      description='Ikcon Protobuf',
      long_description=open(os.path.join(base_dir, "README.md")).read(),
      url='https://github.com/sitmena/ikcon-protobuf',
      classifiers=[
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      keywords='Ikcon Protobuf',
      author='Abdelhadi Abu-Shamleh',
      author_email='a.abushamleh@sit-mena.com',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      dependency_links=[],
      install_requires=[
          'setuptools',
          'protobuf>=3.11.2'
      ]
)
