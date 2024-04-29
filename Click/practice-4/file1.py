import click

version = "0.0.1"

@click.version_option(version, message=f"Version: {version}")
@click.command()
def main():
    print("This is the main command.")


if __name__ == "__main__":
    main()