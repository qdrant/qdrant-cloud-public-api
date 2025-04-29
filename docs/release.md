# Qdrant Cloud Public API - Release Process

This document explains how to release a new version of the generated client libraries (Python, Go, JavaScript, etc.) from the proto repository.
> **Note:**  
> Only python is supported for now, but the process is designed to be extensible for Go and JavaScript in the future.

---
## Release Steps

### 1. Prepare changes
- Update .proto files as needed. 
- Regenerate the code for all target languages (Python, Go, JavaScript, etc.). 
- Test that the generated code works correctly if necessary.

> **Note:**  
> No need to manually change version numbers in pyproject.toml, package.json, or other files.

---

### 2. Create a new Git tag 
   - Once your changes are ready and merged into the main branch, create a Git annotated tag following semantic versioning (e.g., v1.2.0, v1.3.1, etc.).

Example:
```shell
git tag v1.3.0
git push origin v1.3.0
```

> **Important:**  
> Always use the v prefix when tagging (e.g., v1.3.0, not just 1.3.0).

---

### 3. GitHub Actions will automatically build and release
Once the tag is pushed:
- A GitHub Actions workflow will trigger automatically.
- The workflow will:
- Inject the Git tag version into the generated clients dynamically.
- Build the Python package (qdrant-cloud-public-api).
- Upload the Python package to the Google Artifact Registry.
- (Future extension: Publish Go and JavaScript packages, if needed.)

---

## How Versioning Works
- The version in pyproject.toml is automatically replaced by the Git tag version during the build.
- Example: if the pushed tag is v1.3.0, the final Python package version will be 1.3.0.
- Developers should not manually edit the version field in pyproject.toml.

Inside pyproject.toml, you will see:
```toml
# The version is replaced by git tags during the release process
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
- If you accidentally push a wrong tag, delete it:
```bash
git push --delete origin v1.3.0
git tag -d v1.3.0
```
and then create a corrected tag.

