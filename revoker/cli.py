from glob import glob
import click


@click.command()
@click.argument("pattern")
def cli(pattern):
    if not pattern.endswith("*") and not pattern.endswith(".tar.bz2"):
        pattern += ".tar.bz2"
    for fn in glob(pattern, recursive=True):
        open(fn + ".REVOKED", 'a').close()
        print("Revoked {}".format(fn))
