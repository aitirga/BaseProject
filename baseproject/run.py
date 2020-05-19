import click
import logging
from baseproject.config import cfg
from baseproject.model.task1.run import main as main_task1

logger = logging.getLogger(__name__)
tasks = {
    "task1": main_task1
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
def main_cli(task, environment="./env"):
    main(task)

