
import pytest
import sys

from uvr import *

def test_resolve_argv():
    # Test case 1: No arguments
    sys.argv = ['uvr']
    pre_opt, script, post_opt = resolve_argv()
    assert pre_opt == []
    assert script is None
    assert post_opt == []

    # Test case 2: Only pre-options
    sys.argv = ['uvr', '-v', '--']
    pre_opt, script, post_opt = resolve_argv()
    assert pre_opt == ['-v']
    assert script is None
    assert post_opt == []

    # Test case 3: Pre-options and script
    sys.argv = ['uvr', '-v', 'script.py', 'arg1', 'arg2']
    pre_opt, script, post_opt = resolve_argv()
    assert pre_opt == ['-v', ]
    assert script == 'script.py'
    assert post_opt == ['arg1', 'arg2']

    # Test case 4: Only script
    sys.argv = ['uvr', 'script.py']
    pre_opt, script, post_opt = resolve_argv()
    assert pre_opt == []
    assert script == 'script.py'
    assert post_opt == []

    # Test case 5: Script with pre-options and post-options
    sys.argv = ['uvr', '-v', '--script',  'script.py', '--option1', '--option2']
    pre_opt, script, post_opt = resolve_argv()
    assert pre_opt == ['-v', '--script']
    assert script == 'script.py'
    assert post_opt == ['--option1', '--option2']

    # Test case 6: Script with pre-options and post-options
    sys.argv = ['uvr', '--', 'script.py', '--option1', '--option2']
    pre_opt, script, post_opt = resolve_argv()
    assert pre_opt == []
    assert script == 'script.py'
    assert post_opt == ['--option1', '--option2']
