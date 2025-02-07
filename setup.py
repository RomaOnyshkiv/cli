from setuptools import setup

setup(
    name="CLI",
    version='0.1.1',
    py_modules=['cli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
            [console_scripts]
            mycli=cli:cli
        ''',
)