from github import Github
from github.Repository import Repository
# Replace YOUR_TAG_NAME with the actual tag name

g = Github("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")

repo_name = "python-package-manager"
repo = g.get_repo(repo_name)

tag_name = "v1.0.1"

# Replace YOUR_RELEASE_NAME with the actual release name (optional)
release_name = "my-first-release"

# Replace YOUR_RELEASE_NOTES_FILE_PATH with the actual file path of your release notes
with open("src/release_notes.md", "r") as f:
    release_notes = f.read()

# Create the release
repo.create_git_release(tag_name, release_name, release_notes, draft=False, prerelease=False)