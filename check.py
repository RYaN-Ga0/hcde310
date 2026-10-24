"""Checks fetch.py without calling the real API.  Run:  python3 check.py

It runs your fetch.py three times, pretending to be the museum's API each time:
  1. a search for "cat" that answers with sample_response.json (the same 5 artworks every time)
  2. a search with no results
  3. an error from the server (status 500)
You choose your own wording and print format; this only checks that the right things show up and nothing crashes.
It runs a copy of your code in a temporary folder, so it never touches your own results file.
Passing here doesn't prove the live call works: run fetch.py for real too.
"""
import subprocess, sys, pathlib, json, os, tempfile, shutil

here = pathlib.Path(__file__).parent
sys.stdout.reconfigure(encoding="utf-8")  # so ✓ ✗ print on Windows
env = {**os.environ, "PYTHONUTF8": "1"}
sample = json.loads((here / "sample_response.json").read_text(encoding="utf-8"))
works = sample["data"]

# Runs inside a fresh Python: swaps in a fake `requests` and a fake `input()`, then runs fetch.py.
RUNNER = r'''
import sys, json, types, runpy, builtins
status, body_path, term, report_path = int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]
body = json.load(open(body_path, encoding="utf-8"))
report = {"calls": []}

class FakeResponse:
    def __init__(self):
        self.status_code = status
        self.ok = status == 200
        self.reason = {200: "OK", 500: "Internal Server Error"}.get(status, "")
        self.text = json.dumps(body)
    def json(self):
        return body

def get(url, params=None, **kwargs):
    report["calls"].append({"url": url, "params": params or {}})
    return FakeResponse()

fake = types.ModuleType("requests")
fake.get = get
sys.modules["requests"] = fake
builtins.input = lambda prompt="": term

try:
    g = runpy.run_path("fetch.py", run_name="__main__")
    if callable(g.get("count_by_artist")):
        sample = json.load(open("sample_response.json", encoding="utf-8"))
        try:
            report["count_by_artist"] = g["count_by_artist"](sample["data"])
        except Exception as e:
            report["count_by_artist_error"] = f"{type(e).__name__}: {e}"
finally:
    json.dump(report, open(report_path, "w", encoding="utf-8"), default=str)
'''


def run(status, body, term):
    """Runs a copy of fetch.py once with a fake API. Returns (stdout, stderr, crashed, report, text files it wrote)."""
    with tempfile.TemporaryDirectory() as tmp:
        work = os.path.join(tmp, "work")
        os.mkdir(work)
        for name in ("fetch.py", "sample_response.json"):
            shutil.copy(here / name, work)
        body_path, report_path = os.path.join(tmp, "body.json"), os.path.join(tmp, "report.json")
        json.dump(body, open(body_path, "w", encoding="utf-8"))
        try:
            p = subprocess.run([sys.executable, "-c", RUNNER, str(status), body_path, term, report_path], cwd=work,
                               capture_output=True, text=True, encoding="utf-8", env=env, timeout=10)
        except subprocess.TimeoutExpired:
            return "", "took too long (an infinite loop?)", True, {}, {}
        report = json.load(open(report_path, encoding="utf-8")) if os.path.exists(report_path) else {}
        files = {f: open(os.path.join(work, f), encoding="utf-8", errors="replace").read()
                 for f in os.listdir(work) if f.endswith(".txt")}
        return p.stdout, p.stderr.strip(), p.returncode != 0, report, files


def last_line(err):
    return err.splitlines()[-1] if err else "no message"


all_ok = True
def result(ok, msg, detail=""):
    global all_ok
    all_ok = all_ok and ok
    print(("✓ " if ok else "✗ ") + msg + (("\n" + detail) if detail and not ok else ""))


# 1. Search for "cat": the 5 sample artworks
out, err, crashed, report, files = run(200, sample, "cat")
if crashed:
    result(False, 'Search "cat" crashed:', err)
else:
    calls = report.get("calls", [])
    params = calls[0]["params"] if calls else {}
    if not calls:
        result(False, "fetch.py never calls requests.get")
    else:
        result(calls[0]["url"].rstrip("/") == "https://api.artic.edu/api/v1/artworks/search",
               "calls the search URL", f"   yours: {calls[0]['url']!r}")
        result(params.get("q") == "cat", "sends the search term as q",
               f"   the user typed 'cat', but your params are {params}")
        result("artist_title" in str(params.get("fields", "")), "asks for artist_title in fields",
               f"   your fields: {params.get('fields')!r}")
    missing = [w["title"] for w in works if w["title"] not in out]
    result(not missing, "prints all 5 titles", "   missing: " + "; ".join(missing))
    artists = [w["artist_title"] for w in works if w.get("artist_title")]
    missing = [a for a in artists if a not in out]
    result(not missing, "prints the artists",
           "   missing: " + ", ".join(missing) + "\n   Hint: are you looking up the API's field names, or HW2's?")
    # A known artist shouldn't show up as "Unknown" on its title's line (the HW2 key "artist" isn't in the API's data).
    lines = out.splitlines()
    wrong = [l.strip() for w in works if w.get("artist_title")
             for l in lines if w["title"] in l and "unknown" in l.lower()]
    result(not wrong, "known artists aren't printed as Unknown",
           "   " + "\n   ".join(wrong) + "\n   Hint: which key are you looking up for the artist? Check the field names in sample_response.json.")
    nones = [line for line in out.splitlines() if "None" in line]
    result(not nones, "never prints None (null fields get a default)",
           "   " + "\n   ".join(nones) + "\n   Hint: .get(key, default) only uses the default when the key is missing, not when it's null.")

# 2. No results
out, err, crashed, _, _ = run(200, {**sample, "data": [], "pagination": {**sample["pagination"], "total": 0}}, "12345678901234")
result(not crashed and out.strip() != "", "no results: prints a message, no crash",
       f"   it crashed: {last_line(err)}" if crashed else "   it printed nothing")

# 3. Server error
out, err, crashed, _, _ = run(500, {"status": 500, "error": "Internal Server Error"}, "cat")
result(not crashed and out.strip() != "", "server error (500): prints a message, no crash",
       f"   it crashed: {last_line(err)}\n   Hint: what runs when the status isn't 200?" if crashed else "   it printed nothing")
if not crashed and out.strip():
    result("500" in out and "Internal Server Error" in out, "server error: the message includes the code and the reason",
           "   your message: " + out.strip().splitlines()[-1] + "\n   Hint: response.status_code and response.reason")

# Part 3: count_by_artist
if "count_by_artist" not in report and "count_by_artist_error" not in report:
    result(False, "count_by_artist (Part 3)", "   no function named count_by_artist in fetch.py yet (or fetch.py crashed above)")
else:
    want = {}
    for w in works:
        a = w.get("artist_title") or "Unknown"
        want[a] = want.get(a, 0) + 1
    if "count_by_artist_error" in report:
        result(False, "count_by_artist crashed on the sample data:", "   " + report["count_by_artist_error"])
    else:
        got = report["count_by_artist"]
        result(got == want, "count_by_artist gives the right counts for the sample",
               f"   expected: {want}\n   yours:    {got}")

# Part 4: save_results writes a .txt file with the results
if "def save_results" not in (here / "fetch.py").read_text(encoding="utf-8"):
    result(False, "save_results (Part 4)", "   no function named save_results in fetch.py yet")
elif not files:
    result(False, "save_results writes a .txt file when you search", "   no .txt file appeared after searching for 'cat'")
else:
    text = "\n".join(files.values())
    missing = [w["title"] for w in works if w["title"] not in text]
    result(not missing, "save_results writes all 5 titles to a .txt file", "   missing: " + "; ".join(missing))

print()
print("All checks pass. Now run fetch.py for real, too." if all_ok else "Not there yet. Fix the first ✗ and run again.")
sys.exit(0 if all_ok else 1)
