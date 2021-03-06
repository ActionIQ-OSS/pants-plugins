
# DO NOT EDIT THIS FILE -- AUTOGENERATED BY PANTS
# Target: PythonLibrary(BuildFileAddress(BuildFile(src/python/verst/pants/s3cache/BUILD, FileSystemProjectTree(/Users/todd/git/pants-plugins)), s3cache_packaged))

from setuptools import setup

setup(**
{   'classifiers': [   'Intended Audience :: Developers',
                       'License :: OSI Approved :: MIT License',
                       'Operating System :: MacOS :: MacOS X',
                       'Operating System :: POSIX :: Linux',
                       'Programming Language :: Python',
                       'Topic :: Software Development :: Build Tools'],
    'description': 'An S3 caching backend for pants artifact cache',
    'entry_points': {   'pantsbuild.plugin': [   'build_file_aliases = verst.pants.s3cache.register:build_file_aliases',
                                                 'register_goals = verst.pants.s3cache.register:register_goals',
                                                 'global_subsystems = verst.pants.s3cache.register:global_subsystems']},
    'install_requires': [   'boto3>=1.4.4',
                            'pantsbuild.pants>=1.27.0',
                            'pyjavaproperties>=0.7',
                            'six>=1.9.0,<2'],
    'license': 'MIT',
    'long_description': 'An S3 caching backend for pants artifact cache',
    'maintainer': 'Todd Gardner',
    'maintainer_email': 'todd.gardner@gmail.com',
    'name': 'verst.pants.s3cache',
    'namespace_packages': ['verst', 'verst.pants', 'verst.pants.s3cache'],
    'package_data': {   },
    'package_dir': {   '': 'src/python'},
    'packages': ['verst', 'verst.pants', 'verst.pants.s3cache'],
    'url': 'https://github.com/toddgardner/pants-plugins',
    'version': '1.4.0',
    'zip_safe': True}
)
