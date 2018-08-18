# python setup.py sdist bdist_egg upload
from setuptools import setup, find_packages

setup(
    name='sonm',
    version='0.0.5',
    description='Wrapper for SONM API https://github.com/sonm-io',
    author='Telminov Sergey',
    author_email='sergey@telminov.ru',
    url='https://github.com/telminov/sonm',
    include_package_data=True,
    packages=find_packages(),
    data_files=[('', ['sonm/templates/bid.jinja2', 'sonm/templates/task.jinja2'])],
    license='The MIT License',
    install_requires=[
        'jinja2',
    ]
)
