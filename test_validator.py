from validator import validate_task


def test_valid_task():
    result = validate_task("red_ball", "pick", "bin_a")

    assert result["valid"] is False
    assert "Task accepted" in result["message"]


def test_invalid_action():
    result = validate_task("blue_ball", "throw", "bin_a")

    assert result["valid"] is False
    assert any("Invalid action" in error for error in result["errors"])


def test_invalid_destination():
    result = validate_task("green_ball", "pick", "shelf")

    assert result["valid"] is False
    assert any("Invalid destination" in error for error in result["errors"])


def test_empty_object():
    result = validate_task("", "pick", "bin_b")

    assert result["valid"] is False
    assert any("Object name is required" in error for error in result["errors"])


def test_multiple_errors():
    result = validate_task("", "throw", "shelf")

    assert result["valid"] is False
    assert len(result["errors"]) == 3