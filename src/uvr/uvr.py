#!/usr/bin/env python

import os
import sys

# assume: uvr -a --b --cc value -- script.py --d
#      -> uv run -a --b --cc value --project scriptDir script.py --d
# assume: uvr -a --b script.py --d
#      -> uv run -a --b --project scriptDir script.py --d
# assume: uvr -a --b script --d
#      -> uv run -a --b --script --project scriptDir script --d
# problematic case: uvr -a --b -- -f script.py --d   # error -f after --
def resolve_argv():
    pre_opt = []
    script = None
    post_opt = []

    if '--' in sys.argv:
        idx = sys.argv.index('--')
        pre_opt = sys.argv[1:idx]

    else:
        idx = 0
        for i in range(1, len(sys.argv)):
            if sys.argv[i].startswith('-'):
                idx = i
            else:
                break
        pre_opt = sys.argv[1:idx + 1]

    if idx + 1 >= len(sys.argv) or sys.argv[idx + 1].startswith('-'):
        return pre_opt, script, post_opt

    script = sys.argv[idx + 1]
    post_opt = sys.argv[idx + 2:]

    if not (script.endswith('.py') or script.endswith('.pyw')):
        # add --script option if not --[gui-]script already present; otherwise uv loops forever
        if '--script' not in pre_opt and '--gui-script' not in pre_opt:
            pre_opt.append('--script')

    return pre_opt, script, post_opt


def main():  # pragma: no cover
    if len(sys.argv) < 2:
        print("Shebang usage:      #!/usr/bin/env -S uvr [options] [--]")
        print("Command line usage: uvr [options] [--] script.py [script options]")
        print("Debug usage:        uvr -v [options] [--] script.py [script options]")

        sys.exit(1)

    pre_opt, script, post_opt = resolve_argv()

    if '-v' in pre_opt:
        print(f"DEBUG uvr {sys.argv=}", file=sys.stderr)
        print(f"DEBUG uvr {pre_opt=} {script=} {post_opt=}", file=sys.stderr)

    if script is None:
        print("No script provided")
        sys.exit(1)

    if not os.path.isfile(script):
        prog_args = ['uv', 'uv', 'run'] + pre_opt + [script] + post_opt  # fall back to uv run
    else:
        script = os.path.realpath(script)
        scriptDir = os.path.dirname(script)
        prog_args = ['uv', 'uv', 'run'] + pre_opt + ['--project', scriptDir, script] + post_opt

    if '-v' in pre_opt:
        print(f"DEBUG uv {prog_args=}", file=sys.stderr)

    os.execlp(*prog_args)

if __name__ == "__main__":  # pragma: no cover
    main()
