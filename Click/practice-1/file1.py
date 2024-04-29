import click

@click.group(help="Your script description goes here.")
def cli():
    print("Hello")

# ----------------------------

@cli.command()
@click.option("-a", "--texta", default=None, help="Help for option a")
def command_a(texta):
    """A description."""
    print("Working for Command A with texta:", texta)

# ----------------------------

@cli.command()
@click.option("-b", "--textb", default=None, help="Help for option b")
def command_b(textb):
    """B description."""
    print("Working for Command B with textb:", textb)

if __name__ == '__main__':
    cli()
