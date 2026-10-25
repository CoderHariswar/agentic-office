"""The sync scripts must read and write UTF-8 even where the locale default is not
UTF-8 (Windows uses cp1252). We simulate that by making open() default to cp1252."""
import builtins, contextlib, json, os, sys, tempfile, unittest
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
import common, jira_sync  # noqa: E402

_open = builtins.open


def windows_open(file, mode="r", *args, **kw):
    if "b" not in mode and not args and "encoding" not in kw:
        kw["encoding"] = "cp1252"
    return _open(file, mode, *args, **kw)


@contextlib.contextmanager
def windows_locale():
    with mock.patch("builtins.open", windows_open):
        yield


TASK = """---
key: ENG-1
title: Café → launch
owner: cto
---
## Goal
Ship it — fast.

## Notes / log
- 2026-10-24 · cto (Rahul): planned → ready
"""


class WindowsEncodingTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp()
        self.task = os.path.join(self.dir, "ENG-1-test.md")
        with _open(self.task, "w", encoding="utf-8") as fh:
            fh.write(TASK)

    def test_parse_task_file(self):
        with windows_locale():
            meta, sections, entries, _ = common.parse(self.task)
        self.assertEqual(meta["title"], "Café → launch")
        self.assertEqual(entries, ["2026-10-24 · cto (Rahul): planned → ready"])

    def test_roster(self):
        with windows_locale():
            names = common.roster()
        self.assertEqual(names["cto"], "Rahul Venkatesh")

    def test_env_with_bom(self):
        # Notepad saves "UTF-8" files with a byte-order mark.
        env = os.path.join(self.dir, ".env")
        with _open(env, "w", encoding="utf-8-sig") as fh:
            fh.write("AO_TEST_KEY=value\n")
        with windows_locale(), mock.patch.object(common, "ROOT", self.dir), mock.patch.dict(os.environ, {}, clear=False):
            os.environ.pop("AO_TEST_KEY", None)
            common.load_env()
            self.assertEqual(os.environ.get("AO_TEST_KEY"), "value")

    def test_pull_appends_utf8(self):
        state = {"issues": {"ENG-1": {"key": "AGENTIC-1"}}}
        comments = {"comments": [{"id": "1", "created": "2026-10-24T10:00", "author": {"displayName": "Zoë"},
                                  "body": "ok → ship"}]}
        with windows_locale(), mock.patch.object(jira_sync, "task_files", return_value=[self.task]), \
                mock.patch.object(jira_sync, "call", return_value=comments), \
                mock.patch.object(jira_sync, "plain", side_effect=lambda b: b), \
                mock.patch.object(jira_sync, "save_state", create=True), \
                contextlib.redirect_stdout(open(os.devnull, "w")):
            try:
                jira_sync.pull(state)
            except Exception:
                pass  # later bookkeeping is not under test; the appended line is
        with _open(self.task, encoding="utf-8") as fh:
            self.assertIn("Zoë (Jira comment on AGENTIC-1): ok → ship", fh.read())


if __name__ == "__main__":
    unittest.main()
