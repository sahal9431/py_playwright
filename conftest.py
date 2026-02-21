import pytest
import os
from pathlib import Path
from datetime import datetime


@pytest.fixture
def browser_instance(playwright, request):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page   # <-- test runs here
    # teardown starts here
    if request.node.rep_call.failed:
        screenshots_dir = Path.cwd() / "screenshots"
        screenshots_dir.mkdir(exist_ok=True)

        name = request.node.nodeid.replace("::", "_").replace("/", "_")
        ts = datetime.now().strftime("%Y%m%d-%H%M%S")

        path = screenshots_dir / f"{name}-{ts}.png"
        page.screenshot(path=str(path), full_page=True)
        print(f"\nScreenshot saved: {path}")

    page.close()
    context.close()
    browser.close()
#     yield page
#     # After test finishes: capture screenshot if test failed (pytest sets rep_call on node)
#     try:
#         node = getattr(pytest, "_current_test_node", None)
#     except Exception:
#         node = None
#     # fallback: try to access request.node via inspect (not available here)
#     # Use attribute set by pytest_runtest_makereport on the request.node
#     try:
#         # request.node is set for fixtures if passed in; many tests use pytest-bdd step functions
#         # The test that calls this fixture will have set attribute on its node; we can try to find it
#         import inspect
#         frame = inspect.currentframe()
#         # climb until a frame with 'request' in locals
#         req = None
#         f = frame
#         while f is not None:
#             if 'request' in f.f_locals:
#                 req = f.f_locals.get('request')
#                 break
#             f = f.f_back
#         if req is not None:
#             rep = getattr(req.node, 'rep_call', None)
#         else:
#             rep = None
#     except Exception:
#         rep = None

#     screenshots_dir = Path(pytest.Config if False else Path.cwd()) / "screenshots"
#     screenshots_dir.mkdir(parents=True, exist_ok=True)
#     if rep and getattr(rep, 'failed', False):
#         try:
#             nodeid = rep.nodeid if hasattr(rep, 'nodeid') else getattr(req.node, 'nodeid', 'test')
#         except Exception:
#             nodeid = getattr(req.node, 'nodeid', 'test') if 'req' in locals() and req else 'test'
#         safe_name = "".join(c if c.isalnum() or c in ('-', '_', '.') else '_' for c in nodeid)
#         ts = datetime.now().strftime("%Y%m%d-%H%M%S")
#         dest = screenshots_dir / f"{safe_name}-{ts}.png"
#         try:
#             page.screenshot(path=str(dest), full_page=True)
#             print(f"Saved failure screenshot: {dest}")
#         except Exception as e:
#             print(f"Failed to capture screenshot for {nodeid}: {e}")

#     try:
#         page.close()
#     except Exception:
#         pass
#     try:
#         context.close()
#     except Exception:
#         pass
#     try:
#         browser.close()
#     except Exception:
#         pass
# import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # Run all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()
#     # attach report to the item for later access from fixtures/finalizers
#     try:
#         setattr(item, "rep_" + rep.when, rep)
#     except Exception:
#         pass
#     # Capture screenshots for any failed phase (setup/call/teardown)
#     if rep.failed:
#         # Try to locate any Playwright Page instance among fixtures
#         page = None
#         for val in getattr(item, 'funcargs', {}).values():
#             try:
#                 # Page objects have a screenshot method
#                 if hasattr(val, 'screenshot'):
#                     page = val
#                     break
#             except Exception:
#                 continue

#         if page:
#             try:
#                 root = Path(item.config.rootpath)
#             except Exception:
#                 root = Path.cwd()
#             screenshots_dir = root / "screenshots"
#             screenshots_dir.mkdir(parents=True, exist_ok=True)
#             nodeid = item.nodeid.replace("::", "_")
#             safe_name = "".join(c if c.isalnum() or c in ('-', '_', '.') else '_' for c in nodeid)
#             ts = datetime.now().strftime("%Y%m%d-%H%M%S")
#             # write debug info to help diagnose why screenshots may not be created
#             debug_file = screenshots_dir / f"debug-{safe_name}-{ts}.txt"
#             try:
#                 with open(debug_file, "w", encoding="utf-8") as fh:
#                     fh.write(f"funcargs keys: {list(item.funcargs.keys())}\n")
#                     fh.write(f"page repr: {repr(page)}\n")
#             except Exception:
#                 pass

#             dest = screenshots_dir / f"{safe_name}-{ts}.png"
#             try:
#                 page.screenshot(path=str(dest), full_page=True)
#                 # write a tiny marker file confirming success
#                 try:
#                     with open(screenshots_dir / f"ok-{safe_name}-{ts}.txt", "w", encoding="utf-8") as fh:
#                         fh.write(str(dest))
#                 except Exception:
#                     pass
#                 print(f"Saved failure screenshot: {dest}")
#             except Exception as e:
#                 print(f"Failed to capture screenshot for {item.nodeid}: {e}")