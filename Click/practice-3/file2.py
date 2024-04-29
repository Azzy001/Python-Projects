import click


@click.group()
def cli():
    pass

@cli.command()
@click.option("--name", prompt="Your name", help="Name of the user")
def name(name):
    print(f"Your name is {name}.")


@cli.command()
@click.option("--age", prompt="Your age", help="Age of the user")
def age(age):
    print(f"You are {age} years old.")


if __name__ == "__main__":
    cli()