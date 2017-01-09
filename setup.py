from distutils.core import setup

setup(
    name='terminal-brackets',
    version='0.8',
    packages=['terminalbrackets'],
    url='http://github.com/Granitosaurus/terminalbracket',
    license='GPLv3',
    author='granitosaurus',
    author_email='bernardas.alisauskas@gmail.com',
    description='CLI application for printing out competitive brackets from provided json data',
    install_requires=[
        'click',
        'colorama',
    ],
    entry_points="""
        [console_scripts]
        terminal-brackets=terminalbrackets.cli:cli
    """,
)
