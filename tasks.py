import json
import re
import tempfile
from pathlib import Path

import yaml
from invoke.tasks import task


def read_metadata_file(path):
    """Read metadata from YAML, JSON, or Markdown file."""
    path = Path(path)
    content = path.read_text(encoding="utf-8")

    if path.suffix in [".yaml", ".yml"]:
        metadata = yaml.safe_load(content)

    elif path.suffix == ".json":
        metadata = json.loads(content)

    elif path.suffix == ".md":
        # Extract YAML front matter from markdown
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if match:
            yaml_block = match.group(1)
            metadata = yaml.safe_load(yaml_block)
        else:
            metadata = {}
    else:
        raise ValueError(f"Unsupported file type: {path.suffix}")

    return metadata, path.parent


def merge_additional_metadata(metadata, base_path):
    """If metadata-dict exists, load and merge additional files."""
    key = "metadata-files"
    if key in metadata:
        extra = metadata[key]
        if isinstance(extra, str):
            extra = [extra]

        for file in extra:
            file_path = Path(file)
            if not file_path.is_absolute():
                file_path = base_path / file_path
            new_data, _ = read_metadata_file(file_path)
            metadata.update(new_data)

    return metadata


def _metadata(config_path):
    """Return metadata dictionary from config and any merged metadata-dict."""
    metadata, base_path = read_metadata_file(config_path)
    metadata = merge_additional_metadata(metadata, base_path)
    return metadata, base_path


@task
def readmeta(c, config):
    """Read metadata from config and any additional metadata files."""
    metadata, _ = _metadata(config)
    print(metadata)


def resolve_files(files: str | list[str], base_path: Path, ext: str) -> list[str]:
    resolved = []

    if isinstance(files, str):
        files = [files]

    for f in files:
        fpath = Path(f)
        if not fpath.is_absolute():
            fpath = base_path / fpath

        if fpath.is_dir():
            matched = sorted(str(p) for p in fpath.rglob(f"*{ext}") if p.is_file())
            resolved.extend(matched)
        else:
            resolved.append(str(fpath))

    return resolved


@task
def build_ast(c, config):
    """Build Pandoc AST JSON from files specified in metadata."""
    metadata, base_path = _metadata(config)

    file_type = metadata.get("file-type", "markdown")
    file_ext = metadata.get("file-extension", ".md")
    files = metadata.get("files", [])

    resolved_files = resolve_files(files, base_path, file_ext)
    print(json.dumps(resolved_files, indent=4))

    if metadata.get("build-dir"):
        output_dir = base_path / metadata["build-dir"]
    else:
        output_dir = Path(tempfile.mkdtemp())

    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "combined.json"
    print(output_path.resolve())

    # Build the Pandoc command
    input_files_str = " ".join(f'"{f}"' for f in resolved_files)
    cmd = f'pandoc -f {file_type} -t json {input_files_str} -o "{output_path}"'

    print(f"Running: {cmd}")
    result = c.run(cmd, hide=False, warn=False)

    print(f"AST written to: {output_path}")
