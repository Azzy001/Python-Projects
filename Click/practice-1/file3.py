import click

@click.group()
def cli():
    pass

@cli.command()
@click.option("-u", "--url", default=None, help="The URL to process")
def process_url(url):
    """
    This script processes a URL.

    Example:
        python script.py process-url --url https://example.com
    """
    print(f"Processing URL: {url}")

@cli.command()
@click.option("-f", "--file", default=None, help="The file to process")
def process_file(file):
    """
    This script processes a file.

    Example:
        python script.py process-file --file example.txt
    """
    print(f"Processing File: {file}")

if __name__ == '__main__':
    cli()
