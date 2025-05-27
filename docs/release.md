# Qdrant Cloud Public API - Release Process

This document explains how to release a new version of the generated libraries (Python, JavaScript, etc.) from the proto repository.
> **Note:**  
> Only python and typescript is supported for now, but the process is designed to be extensible for other languages in the future.

---
## Release Steps

### 1. Create a new branch for the release
   - Once your changes are merged into the main branch, create a Git branch for the release. Branch must be named `releases/vX.Y.Z`.

Example:
```shell
git checkout -b releases/v1.3.0
git push origin releases/v1.3.0
```

> **Important:**  
> Always use the `v` prefix when creating a release branch.

---

### 2. GitHub Actions will automatically build and upload the package
Once the branch is pushed:
- A GitHub Actions workflow will trigger automatically.
- The workflow will:
  - Inject the version into the generated client(s) dynamically.
  - Build the Python and Typescript package (qdrant-cloud-public-api).
  - Upload the Python and Typescript package to the Google Artifact Registry.

---

## How Versioning Works
- The version in pyproject.toml and package.json is automatically replaced by the version from Git branch name during the build.
- Example: if the pushed branch is releases/v1.3.0, the final Python/Typescript package version will be 1.3.0.
- Developers should not manually edit the version field in pyproject.toml or package.json.

Inside pyproject.toml, you will see:
```toml
# The version is replaced by the version from Git branch name during the release process
version = "0.0.0"
```
This is normal.
Same for package.json:
```json
{
  "name": "@qdrant/qdrant-cloud-public-api",
  "version": "0.0.0",
  ...
}
```

---

## Best Practices
- Follow semantic versioning (MAJOR.MINOR.PATCH) when tagging:
  - MAJOR: breaking changes
  - MINOR: new features, backward-compatible
  - PATCH: bug fixes, minor corrections
- Always test generated clients before tagging a release.
- If you accidentally push a wrong branch, delete it:
```bash
git branch -D releases/v1.3.0
git push origin --delete releases/v1.3.0
```
and then create a corrected branch.

