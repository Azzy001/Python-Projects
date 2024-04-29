import click

@click.command() # function for cmd comand
@click.option("--name", prompt="Your name: ", help="The name of the user")
def greetings(name):
    click.echo(f"Good afternoon {name}.")


if __name__ == "__main__":
    greetings()