from setuptools import setup

setup(
    name="Roman's CLI",
    version='0.1',
    py_modules=['cli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
            [console_scripts]
            mycli=cli:cli
        ''',
)