import click
import logging


logger = logging.getLogger(__name__)
tasks = {
    "test": None
}


def main(task):
    try:
        tasks[task]()
    except:
        logger.error(f"Task {task} failed")


@click.command()
@click.option(
    "--task",
    type=click.Choice(tasks.keys()),
    required=True,
    help="Name of the task to execute",
)
def main_cli(task):
    main(task)