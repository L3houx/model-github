from setuptools import setup, find_packages

setup(
    name='model-github',
    version='0.1',
    description='Meltano .m5o models for data fetched using the GitHub API',
    packages=find_packages(),
    package_data={'models': ['**/*.m5o', '*.m5o']},
    install_requires=[],
)
