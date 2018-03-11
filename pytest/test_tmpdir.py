
import pytest
import pandas as pd

@pytest.fixture
def dataset():
    # this is some test data we need
    df = pd.DataFrame({'a': [1, 2], 
                       'b': [2, 3]})
    return df

@pytest.fixture
def datafile(tmpdir, dataset):
    df = dataset
    path = tmpdir.join('df.csv')
    df.to_csv(path, index=None)
    return path

def test_with_tmpdir_fixture(datafile, dataset):
    pd.testing.assert_frame_equal(pd.read_csv(datafile), dataset)
    assert 0