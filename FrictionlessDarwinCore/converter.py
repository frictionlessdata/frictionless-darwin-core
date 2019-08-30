import click

from FrictionlessDarwinCore import DwCArchive

@click.command()
@click.argument('dwca', type=str)
@click.option('--json', type=click.File('w'))
@click.option('--md', type=click.File('w'))
def convert(dwca,json, md):
        click.echo('DwCA = %s!' % dwca)
        da=DwCArchive(dwca)
        da.infer()
        if json == None and md == None:
            da.save()
        if json != None:
            click.echo('-json = %s!' % json)
            da.to_json(json)
        if md != None:
            click.echo('-md = %s!' % md)
            da.to_markdown(md)

if __name__ == '__main__':
    convert()
