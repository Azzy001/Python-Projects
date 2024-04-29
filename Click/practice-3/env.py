import click

@click.command()
@click.option("--e", prompt="input env", help="environment: depl, stag, prod")
def env(e):
    click.echo(f"You've selected {e} environment")


if __name__ == "__main__":
    env()