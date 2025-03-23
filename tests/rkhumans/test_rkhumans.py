import rkhumans

def test_count_of_children() -> None:
    abraham = rkhumans.Abraham()
    assert abraham.get_n_children() == 8
