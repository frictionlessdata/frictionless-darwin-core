import click

from FrictionlessDarwinCore import DwCArchive

@click.command()
@click.argument('dwca', type=str)
@click.option('--json', type=click.Path())
@click.option('--md', type=click.Path())
def cli(dwca,json, md):
        da=DwCArchive(dwca)
        da.infer()
        if json == None and md == None:
            click.echo('DwCA = %s' % dwca)
            da.save()
        if json != None:
            click.echo('-json = %s' % json)
            da.to_json(json)
        if md != None:
            click.echo('-md = %s' % md)
            da.to_markdown(md)

if __name__ == '__main__':
    cli()
