from tempfile import TemporaryDirectory
from pathlib import Path

from starspace.test.util import make_matrix
from starspace.classes import Matrix
from starspace.constants import MATRIX_NAME


def test_read_write() -> None:
    matrix = make_matrix()

    with TemporaryDirectory() as dirpath:
        zarr_directory = Path(dirpath) / "archive.zarr"
        matrix.save_zarr(url=zarr_directory)

        the_matrix_reloaded = Matrix.load_zarr(url=f"{zarr_directory}.{MATRIX_NAME}.zarr")

        # assert the matrix isn't mutated upon reading
        assert the_matrix_reloaded.identical(matrix)
