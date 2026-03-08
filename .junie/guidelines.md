# AI Agent Instructions for qsum

This document provides guidelines for AI agents working on the qsum project. Follow these instructions carefully to maintain code quality and project standards.

## Critical Workflow Rules

### Branch Management
- **NEVER commit directly to master branch**
- **ALWAYS create a new feature branch** for any changes
- Branch naming convention: `<type>-<brief-description>` (e.g., `feature-add-new-hasher`, `fix-collision-bug`, `test-edge-cases`)
- All changes must be merged to master via **GitHub Pull Request** with manual review

### Git Workflow
```bash
# Create a new branch
git checkout -b <branch-name>

# Make your changes and commit
git add .
git commit -m "descriptive commit message"

# Push to remote
git push -u origin <branch-name>

# Create PR via GitHub (never merge directly)
```

## Project Goals and Principles

### Core Objectives
1. **Checksumming toolkit**: Provide out-of-the-box support for common Python types
2. **Extensible framework**: Enable customized checksumming logic
3. **High quality**: Produce checksums with extraordinarily low collision rates
4. **Comprehensive testing**: Maintain 100% test coverage
5. **Broad compatibility**: Support Python 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13, and 3.14

### Design Principles

#### Checksum Structure
- **QSUM CHECKSUM = TYPE PREFIX + DATA CHECKSUM**
  - First 2 bytes: type prefix (identifies the type)
  - Remaining bytes: data checksum (digest of byte representation)

#### Relationship to Python's `__hash__`
- Respect the contract: objects that compare equal must have the same checksum
- **No salt by default** (unless explicitly requested via `depends_on`)
- **Stability**: Checksums must be consistent across Python sessions, versions, and qsum releases
- **PYTHONHASHSEED independence**: Environment variable must not affect checksums
- **Longer checksums**: Significantly longer than `__hash__` (which is 8 bytes on 64-bit, 4 on 32-bit)
- **Bytes representation**: All checksums as bytes, with toolkit for human-readable formats (hexdigests)
- **Content-based**: Base checksums on object contents, allow checksums on mutable objects

#### Type Support Requirements
- Support all common built-in types: bool, int, float, complex, str, bytes, tuple, list, dict, set, deque, etc.
- Custom containers inheriting from common types must be checksummable
- Functions checksummed by: source code + attributes + module location
- Modules checksummed by: source code hash
- Files checksummed by: all bytes in the file

## Development Best Practices

### Testing
- **100% code coverage is mandatory**
- Write tests for all new features before implementation (TDD preferred)
- Test across all supported Python versions (3.7-3.14)
- Include edge cases and collision testing
- Use pytest framework
- Run tests locally before pushing:
  ```bash
  pytest
  ```

### Code Quality
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Document all public APIs with clear docstrings
- Maintain backward compatibility unless explicitly bumping major version

### Collision Prevention
- Design checksumming logic to minimize collision rates
- Test for potential collisions between similar objects
- Ensure type prefixes prevent cross-type collisions
- Add class names as salt for custom containers

### Performance Considerations
- Optimize for common types
- Consider memory usage for large objects
- Benchmark performance-critical code paths

## Common Tasks for AI Agents

### Adding Support for a New Type
1. Create feature branch
2. Add type prefix registration
3. Implement checksumming logic
4. Ensure no collisions with existing types
5. Write comprehensive tests (100% coverage)
6. Update documentation if adding public API
7. Test across all Python versions
8. Create PR for review

### Fixing Bugs
1. Create fix branch
2. Write failing test that reproduces the bug
3. Implement fix
4. Verify test passes and coverage remains 100%
5. Check for regression across supported Python versions
6. Create PR with clear description of bug and fix

### Adding Features
1. Create feature branch
2. Design feature to align with project goals
3. Implement with backward compatibility in mind
4. Write comprehensive tests
5. Update examples in README if user-facing
6. Ensure 100% coverage maintained
7. Create PR with feature description and use cases

### Refactoring
1. Create refactor branch
2. Ensure all existing tests pass before changes
3. Make refactoring changes
4. Verify all tests still pass
5. Confirm no performance regression
6. Create PR explaining refactoring rationale

## CI/CD Integration
- GitHub Actions runs tests automatically on PR
- Codecov reports coverage (must remain 100%)
- All checks must pass before merge consideration
- Manual review required even if all automated checks pass

## Documentation Standards
- Keep README.md up to date with user-facing changes
- Use clear, concise language
- Include code examples for new features
- Maintain consistency with existing documentation style

## Package Management
- Dependencies managed via setup.py/pyproject.toml
- Keep dependencies minimal and justified
- Test with both conda and pip installations
- Ensure compatibility with conda-forge packaging

## Questions or Uncertainties?
- If design decisions are unclear, create a draft PR with questions
- Highlight trade-offs in PR description for human review
- When in doubt about backward compatibility, preserve existing behavior
- Prioritize stability and reliability over new features

## Remember
- All code changes require human review via PR
- Master branch is protected - direct commits are not allowed
- Quality over speed - maintain 100% test coverage
- Stability is paramount - checksums must remain consistent across versions
