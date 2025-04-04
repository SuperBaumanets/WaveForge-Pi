import pytest
from src.manager.toml_gui_manager import TomlManager

@pytest.fixture
def temp_toml_file(tmp_path):
    test_file = tmp_path / "test.toml"
    yield test_file
    if test_file.exists():
        test_file.unlink()

def test_initialization(temp_toml_file):
    tm = TomlManager(temp_toml_file)
    assert tm.data == {}
    assert tm.get_table_names() == []

def test_add_and_read_table(temp_toml_file):
    tm = TomlManager(temp_toml_file)
    
    tm.add_table("Locator_1", {
        "signal": "signal_1",
        "frequency_range": "range_1"
    })
    
    table = tm.read_all_fields("Locator_1")
    assert table == {
        "signal": "signal_1",
        "frequency_range": "range_1"
    }
    
    assert tm.get_table_names() == ["Locator_1"]

def test_duplicate_table(temp_toml_file):
    tm = TomlManager(temp_toml_file)
    tm.add_table("Locator_1", {})

    with pytest.raises(ValueError):
        tm.add_table("Locator_1", {})

def test_update_fields(temp_toml_file):
    tm = TomlManager(temp_toml_file)
    tm.add_table("Locator_1", {"signal": "old_signal"})
    
    tm.write_fields("Locator_1", {
        "signal": "new_signal",
        "new_field": "value"
    })
    
    assert tm.read_field("Locator_1", "signal") == "new_signal"
    assert tm.read_field("Locator_1", "new_field") == "value"

def test_delete_table(temp_toml_file):
    tm = TomlManager(temp_toml_file)
    tm.add_table("Locator_1", {})
    
    tm.delete_table("Locator_1")
    assert tm.get_table_names() == []
    
    tm.delete_table("NonExistent")

def test_read_nonexistent_table(temp_toml_file):
    tm = TomlManager(temp_toml_file)
    
    assert tm.read_all_fields("NonExistent") is None
    assert tm.read_field("NonExistent", "field") is None

def test_persistence(temp_toml_file):
    with TomlManager(temp_toml_file) as tm:
        tm.add_table("Locator_1", {"signal": "persistent"})
    
    tm2 = TomlManager(temp_toml_file)
    assert tm2.read_field("Locator_1", "signal") == "persistent"