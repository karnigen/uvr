#!/usr/bin/env python

import os
import sys

# assume: uvr -a --b --cc value -- script.py --d
#      -> uv run -a --b --cc value --project scriptDir --script script.py --d
# assume: uvr -a --b script.py --d
#      -> uv run -a --b --project scriptDir --script script.py --d
# problematic case: uvr -a --b -- -f script.py --d
#      -> uv run -a --b --project scriptDir --script script.py -f --d ??? not solved yet -f
def resolve_argv():
    if '--' in sys.argv:
        idx = sys.argv.index('--')
        pre_opt = sys.argv[1:idx]
        script = sys.argv[idx + 1]
        post_opt = sys.argv[idx + 2:]
    else:
        idx = 0
        for i in range(1, len(sys.argv)):
            if sys.argv[i].startswith('-'):
                continue
            else:
                idx = i-1
                break
        pre_opt = sys.argv[1:idx+1]
        script = sys.argv[idx + 1]
        post_opt = sys.argv[idx + 2:]

    return pre_opt, script, post_opt

def main():
    if len(sys.argv) < 2:
        print("Usage in shebang: #!/usr/bin/env uvr")
        print("                  #!/usr/bin/env -S uvr -opt1 --opt2")
        print("                  #!/usr/bin/env -S uvr -opt1 --opt2 value --")
        sys.exit(1)

    pre_opt, script, post_opt = resolve_argv()

    script = os.path.realpath(script)
    scriptDir = os.path.dirname(script)

    prog_args = ['uv', 'uv', 'run'] + pre_opt + ['--project', scriptDir, script] + post_opt
    os.execlp(*prog_args)

if __name__ == "__main__":
    main()
