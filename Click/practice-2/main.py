import click

@click.command()
@click.option("--name", prompt="Enter your name: ", help="Then name of the user")
def hello(name):
    click.echo(f"Hello {name}!")



if __name__ == "__main__":
    hello()