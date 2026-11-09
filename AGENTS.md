# Development guide

These instructions apply to the entire `py-timenet` repository.

## Project layout

Python library published as `timenet`, a thin wrapper around Timenet's public
API. Public entry point: `from timenet import TimenetClient`.

| Path | Responsibility |
| --- | --- |
| `timenet/client.py` | Authentication, HTTP transport, JSON serialization and error handling. |
| `timenet/endpoints/` | `CheckAPI`, `ConfigAPI`, `CustomersAPI`, `GroupsAPI`, `ProjectsAPI` and `WorkersAPI`; delegate to the client. |
| `timenet/__init__.py` | Exports `TimenetClient` and resolves `__version__`. |
| `tests/test_client.py` | HTTP contract tests using `FakeSession` and `FakeResponse`. |
| `tests/test_endpoints.py` | Route, method, parameter and payload tests using `FakeClient`. |
| `setup.py` | Package metadata, supported Python versions and runtime dependencies. |
| `requirements-ci.txt` / `requirements-py27.txt` | Pinned dependencies for CI and Python 2.7, respectively. |
| `.github/workflows/tests.yml` | Python 3.11 tests on pull requests and pushes to `main`. |
| `README.md` | Installation, usage and payload validation policy. |

## Environment setup

Run commands from the repository root. To reproduce the CI environment:

```bash
python3.11 -m venv venv
. venv/bin/activate
python -m pip install -r requirements-ci.txt
python -m unittest discover -v
```

Both requirements files include `-e .` for an editable install. `venv/` is ignored
by Git.

Python 2.7 compatibility is checked locally, outside CI. In an isolated Python
2.7 environment:

```bash
python2.7 -m pip install -r requirements-py27.txt
python2.7 -m unittest discover -v
```

## Compatibility and style

- Keep library code and tests compatible with Python 2.7 and 3, as declared in
  `setup.py`. Avoid f-strings, type annotations, `async` and Python 3-only APIs.
- Follow existing patterns: UTF-8 encoding,
  `from __future__ import unicode_literals, absolute_import`, classes inheriting
  from `object` and `.format()` for string interpolation.
- Use four spaces, `snake_case` for methods and variables, `PascalCase` for
  classes and `id_` for resource identifiers.
- Keep project documentation and docstrings in Catalan, using `:param` and
  `:return:` where appropriate. Keep agent instructions in English. Match the
  surrounding file's style.
- The project uses `unittest` and has no linter or formatter configuration.
  Keep changes focused and justify new dependencies.

## API contracts

- Centralize transport in
  `TimenetClient.request(method, endpoint, data=None, params=None)`. Endpoints
  pass relative paths, query filters through `params` and payloads through `data`.
- Timenet validates fields, dates, identifiers and enum values, as documented
  in the README. Forward payloads unchanged, including additional fields;
  leave business validation to the server.
- Preserve the `token` header, `json.dumps` serialization passed through
  `session.request(..., data=...)`, injectable `session`, configurable timeout
  and URL slash normalization.
- Supported HTTP methods are `GET`, `POST`, `PUT` and `DELETE`. Preserve decoded
  JSON responses and centralized handling of HTTP errors, invalid JSON and
  `requests` exceptions through error dictionaries.
- Endpoint families are client attributes: `check`, `config`, `customers`,
  `groups`, `projects` and `workers`. Import and instantiate new endpoint
  families in `TimenetClient.__init__`.
- Preserve public signatures, routes and response formats unless the task
  explicitly requires changing them.

## Testing and delivery

Run individual test modules with:

```bash
python -m unittest tests.test_client -v
python -m unittest tests.test_endpoints -v
```

- Add regression tests for behavior changes, covering the affected contract:
  HTTP method, route, parameters, JSON body or error response.
- Reuse existing test doubles. Keep tests independent of credentials and live
  Timenet requests.
- Run `python -m unittest discover -v` after code changes. Report unavailable
  Python 2.7 validation and any failures caused by the environment.
- Update the README when public usage or documented behavior changes. For a
  version bump, review both `setup.py` and the `__version__` fallback in
  `timenet/__init__.py`.
- Review `git diff --check` and the final diff. Summarize changes and checks;
  preserve any pre-existing user changes.
