import click
import json
from terminalbrackets import make_bracket, DEFAULT_INDENT, DEFAULT_PAD_CHAR
from json import JSONDecodeError


@click.command()
@click.argument('round_files', nargs=-1, type=click.File('rb'), required=True)
@click.option('-i', '--indent', type=click.INT, help='Number of how much to indent [Default:{}]'.format(DEFAULT_INDENT))
@click.option('-p', '--pad-char', type=click.STRING,
              help='Character to use for indentation [Default:{}]'.format(DEFAULT_PAD_CHAR))
def cli(round_files, indent, pad_char):
    """CLI application for printing out competitive brackets from provided json data"""
    bracket = []
    for file in round_files:
        try:
            data = json.loads(file.read().strip().decode('utf-8'))
        except JSONDecodeError as e:
            click.echo('{} is not a valid json:\n\t{}'.format(file.name, e))
            return
        bracket.append(data)

    text = make_bracket(bracket,
                        indent=indent,
                        pad_char=pad_char)
    click.echo(text)
