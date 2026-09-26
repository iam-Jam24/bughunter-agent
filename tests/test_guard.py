from guard.guard import check

ORIGINAL = {
    "cart.py": "def cart_total(items, discount_percent=0):\n    return 0\n",
    "test_cart.py": "def test_total():\n    assert True\n",
}


def test_no_new_test_is_stopped():
    verdict, reasons, _ = check(ORIGINAL, dict(ORIGINAL))
    assert verdict == "STOP"
    assert "No new test was added to prove the bug" in reasons


def test_fix_with_new_test_is_ok():
    fixed = {
        "cart.py": "def cart_total(items, discount_percent=0):\n    return 1\n",
        "test_cart.py": ORIGINAL["test_cart.py"] + "\n\ndef test_discount():\n    assert True\n",
    }
    verdict, reasons, changed = check(ORIGINAL, fixed)
    assert verdict == "OK"
    assert reasons == []
    assert changed == ["cart.py"]


def test_removing_an_existing_test_is_stopped():
    fixed = {
        "cart.py": ORIGINAL["cart.py"],
        "test_cart.py": "def test_discount():\n    pass\n",
    }
    verdict, reasons, _ = check(ORIGINAL, fixed)
    assert verdict == "STOP"
    assert any("Existing tests removed" in r for r in reasons)
    assert any("Fewer assertions" in r for r in reasons)


def test_deleting_a_test_file_is_stopped():
    fixed = {"cart.py": ORIGINAL["cart.py"], "test_new.py": "def test_x():\n    assert True\n"}
    verdict, reasons, _ = check(ORIGINAL, fixed)
    assert verdict == "STOP"
    assert "Existing test file deleted: test_cart.py" in reasons


def test_too_many_changed_files_is_stopped():
    original = {f"m{i}.py": "x = 0\n" for i in range(3)} | {"test_m.py": "def test_a():\n    assert True\n"}
    fixed = {f"m{i}.py": "x = 1\n" for i in range(3)} | {
        "test_m.py": original["test_m.py"] + "\n\ndef test_b():\n    assert True\n"
    }
    verdict, reasons, _ = check(original, fixed)
    assert verdict == "STOP"
    assert any("source files" in r for r in reasons)
