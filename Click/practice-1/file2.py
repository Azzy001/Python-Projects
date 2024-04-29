import click

@click.command()
@click.option("-u", "--url", default=None, help="The URL to process")
def process_url(url):
    """
    This script processes a URL.

    Example:
        python script.py --url https://example.com
    """
    print(f"Processing URL: {url}")

if __name__ == '__main__':
    process_url()
