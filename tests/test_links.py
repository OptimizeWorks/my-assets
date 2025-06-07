from pathlib import Path
from html.parser import HTMLParser


class LinkScriptParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []

    def handle_starttag(self, tag, attrs):
        if tag not in {"link", "script"}:
            return
        attr_name = "href" if tag == "link" else "src"
        for name, value in attrs:
            if name == attr_name and value:
                self.refs.append(value)


def extract_local_paths(html_path: Path):
    parser = LinkScriptParser()
    parser.feed(html_path.read_text(encoding="utf-8"))
    local_paths = []
    for ref in parser.refs:
        if ref.startswith(("http://", "https://", "//", "data:", "mailto:", "tel:")):
            continue
        ref = ref.split("?")[0].split("#")[0]
        local_paths.append((html_path.parent / ref).resolve())
    return local_paths


def test_referenced_files_exist():
    repo_root = Path(__file__).resolve().parents[1]
    html_files = [repo_root / "index.html", repo_root / "style-guide.html"]

    missing = []
    for html in html_files:
        for path in extract_local_paths(html):
            if not path.exists():
                missing.append(str(path.relative_to(repo_root)))
    assert not missing, f"Missing referenced files: {missing}"
