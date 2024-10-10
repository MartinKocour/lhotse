from typing import Optional, Sequence, Union

import click

from lhotse.bin.modes import download, prepare
from lhotse.recipes.ears import download_ears, prepare_ears
from lhotse.utils import Pathlike


@prepare.command(context_settings=dict(show_default=True))
@click.argument("corpus_dir", type=click.Path(exists=True, dir_okay=True))
@click.argument("output_dir", type=click.Path())
@click.option(
    "-j",
    "--num-jobs",
    type=int,
    default=1,
    help="How many threads to use (can give good speed-ups with slow disks).",
)
def ears(
    corpus_dir: Pathlike,
    output_dir: Optional[Pathlike] = None,
    num_jobs: int = 1,
):
    """EARS data preparation."""
    prepare_ears(
        corpus_dir=corpus_dir,
        output_dir=output_dir,
        num_jobs=num_jobs,
    )


@download.command(context_settings=dict(show_default=True))
@click.argument("target_dir", type=click.Path())
def ears(
    target_dir: Pathlike,
):
    """EARS data download."""
    download_ears(
        target_dir=target_dir,
    )
