from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='revoker',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Tool for revoking packages in conda channels",
    author="Anaconda, Inc.",
    author_email='conda@anaconda.com',
    url='https://github.com/conda/revoker',
    packages=['revoker'],
    entry_points={
        'console_scripts': [
            'revoker=revoker.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='revoker',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)
