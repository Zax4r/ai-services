import pytest

from app.file_processer import FileProcesser


@pytest.fixture(scope='session')
def file_processer():
    return FileProcesser()


def test_succeed_file_processer(file_processer: FileProcesser):
    for text in file_processer.process_dir('files'):
        assert text is not None


def test_fail_file_processer(file_processer: FileProcesser):
    with pytest.raises(FileNotFoundError):
        for text in file_processer.process_dir('random_dir_not_existing'):
            pass
