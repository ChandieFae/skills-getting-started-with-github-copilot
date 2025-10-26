import subprocess
import time
import os
import signal

import httpx


def wait_for_server(url: str, timeout: float = 10.0):
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            r = httpx.get(url, timeout=1.0)
            return r
        except Exception:
            time.sleep(0.2)
    raise RuntimeError(f"Server did not become available at {url} within {timeout}s")


def test_ui_serves_index(tmp_path):
    """Start uvicorn in a subprocess and verify the static index.html is served.

    This is a simple integration-style test. It starts a dev server on port 8000,
    polls until the server responds, verifies the page contains the expected
    title, then cleans up the subprocess.
    """

    port = os.environ.get("TEST_SERVER_PORT", "8000")
    url = f"http://127.0.0.1:{port}/static/index.html"

    # Start uvicorn as a subprocess
    proc = subprocess.Popen([
        "uvicorn",
        "src.app:app",
        "--port",
        str(port),
        "--log-level",
        "info",
    ])

    try:
        resp = wait_for_server(url, timeout=12.0)
        assert resp.status_code == 200
        text = resp.text
        assert "Mergington High School Activities" in text
    finally:
        # Terminate the server process
        proc.send_signal(signal.SIGINT)
        try:
            proc.wait(timeout=5)
        except Exception:
            proc.kill()
            proc.wait()
