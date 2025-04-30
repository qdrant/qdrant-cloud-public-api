# Qdrant Cloud Public API - Release Process

This document explains how to release a new version of the generated libraries (Python, JavaScript, etc.) from the proto repository.
> **Note:**  
> Only python is supported for now, but the process is designed to be extensible for JavaScript or other languages in the future.

---
## Release Steps

### 1. Create a new branch for the release
   - Once your changes are merged into the main branch, create a Git branch for the release. Branch must be named `releases/X.Y.Z`.

Example:
```shell
git checkout -b releases/1.3.0
git push origin releases/1.3.0
```

> **Important:**  
> Please do not use `v` prefix in the branch name. For example, use `releases/1.3.0` instead of `releases/v1.3.0`.

---

### 2. GitHub Actions will automatically build and upload the package
Once the branch is pushed:
- A GitHub Actions workflow will trigger automatically.
- The workflow will:
  - Inject the version into the generated client(s) dynamically.
  - Build the Python package (qdrant-cloud-public-api).
  - Upload the Python package to the Google Artifact Registry.
  - (Future extension: Publish JavaScript packages, if needed.)

---

## How Versioning Works
- The version in pyproject.toml is automatically replaced by the version from Git branch name during the build.
- Example: if the pushed branch is releases/1.3.0, the final Python package version will be 1.3.0.
- Developers should not manually edit the version field in pyproject.toml.

Inside pyproject.toml, you will see:
```toml
# The version is replaced by the version from Git branch name during the release process
version = "0.0.0"
```
This is normal.

---

## Best Practices
- Follow semantic versioning (MAJOR.MINOR.PATCH) when tagging:
  - MAJOR: breaking changes
  - MINOR: new features, backward-compatible
  - PATCH: bug fixes, minor corrections
- Always test generated clients before tagging a release.
- If you accidentally push a wrong branch, delete it:
```bash
git branch -D releases/1.3.0
git push origin --delete releases/1.3.0
```
and then create a corrected branch.

