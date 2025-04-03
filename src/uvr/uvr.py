#!/usr/bin/env python

import os
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage in shebang: #!/usr/bin/env uvr")
        sys.exit(1)

    script = sys.argv[1]
    script = os.path.realpath(script)
    scriptDir = os.path.dirname(script)

    os.execlp('uv', 'uv', 'run', '--project', scriptDir, '--script', script, *sys.argv[2:])

if __name__ == "__main__":
    main()
