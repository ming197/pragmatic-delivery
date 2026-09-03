import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).parents[1]
    / "plugins"
    / "pragmatic-delivery"
    / "scripts"
    / "install_project_rules.py"
)
SPEC = importlib.util.spec_from_file_location("install_project_rules", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class InstallerTests(unittest.TestCase):
    def test_create_and_repeat_without_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "AGENTS.md"
            block = "<!-- pragmatic-delivery:start -->\nrules\n<!-- pragmatic-delivery:end -->"

            self.assertEqual(MODULE.update_file(target, block, False), "created")
            self.assertEqual(MODULE.update_file(target, block, False), "current")

    def test_preserves_content_outside_managed_block(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "AGENTS.md"
            target.write_text("before\n\n<!-- pragmatic-delivery:start -->\nold\n<!-- pragmatic-delivery:end -->\n\nafter\n")
            block = "<!-- pragmatic-delivery:start -->\nnew\n<!-- pragmatic-delivery:end -->"

            MODULE.update_file(target, block, False)

            self.assertEqual(target.read_text(), "before\n\n" + block + "\n\nafter\n")

    def test_check_does_not_write(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "CLAUDE.md"
            block = "<!-- pragmatic-delivery:start -->\nrules\n<!-- pragmatic-delivery:end -->"

            self.assertEqual(MODULE.update_file(target, block, True), "would-update")
            self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()
