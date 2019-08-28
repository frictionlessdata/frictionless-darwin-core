import click
from FrictionlessDarwinCore import DwCArchive

@click.command()
@click.argument('dwca', type=str)
@click.option('--o', type=click.File('wb'))
def convert(dwca):
        click.echo('DwCA = %s!' % dwca)
        da=DwCArchive(dwca)
        da.infer()

if __name__ == '__main__':
    convert()
