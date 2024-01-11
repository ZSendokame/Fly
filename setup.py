from setuptools import setup, find_packages

long_description = open('./README.md')

setup(
    name='Fly',
    version='1.0.1',
    url='https://github.com/ZSendokame/Fly',
    license='MIT license',
    author='ZSendokame',
    description='Web scraping library.',
    long_description=long_description.read(),
    long_description_content_type='text/markdown',

    packages=(find_packages(include=['fly']))
)
