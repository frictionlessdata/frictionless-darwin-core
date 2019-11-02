import click

from FrictionlessDarwinCore import DwCArchive

@click.command()
@click.argument('dwca', type=str, required=True)
@click.argument('outpath', type=click.Path(writable=True),required=True)
@click.option('-f','--format', help='Output format', type=click.Choice(['json', 'md', 'csv']))
def cli(dwca, outpath, format):
        da = DwCArchive(dwca)
        if da.valid:
            da.infer()
            if da.valid:
                if format is None:
                    da.save(outpath)
                if format == 'json':
                    da.to_json(outpath)
                if format == 'md':
                    da.to_markdown(outpath)
                if format == 'csv':
                    da.to_csv(outpath)

if __name__ == '__main__':
    cli()
