#!/usr/bin/env -S uvr -v --

# will be called as: uvr -vv  tests/foo.py


#!/usr/bin/env -S uvr -vv -- no-other-option-after--

#!/usr/bin/env -S uvr --gui-script

#!/usr/bin/env -S uvr --script

import sys

print(sys.argv)
