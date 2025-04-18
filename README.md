

# Simple Script Execution with uvr

[`uv`](https://github.com/astral-sh/uv.git) is a fast, modern Python package installer and resolver, designed as a drop-in replacement for pip and pip-compile.

Unfortunately, [`uv`](https://github.com/astral-sh/uv.git)
prioritizes virtual environments within the current directory. This makes it cumbersome to execute scripts located elsewhere, requiring the use of the `--project` flag.

This script offers a streamlined workaround for running Python scripts via `uv`, allowing you to use `uvr [options] script.py` instead of `uv run [options] --project <script_path> script.py`."



## Installation

To install `uvr`, use the following command:

```bash
uv tool install --from git+https://github.com/karnigen/uvr uvr
```

To upgrade `uvr`, use the following command:

```bash
uv tool upgrade uvr
```



## Usage

Several ways to run your Python scripts with `uv`:

1.  **Using `uv run --project <script_path> script.py`:**

    * This command explicitly tells `uv` to run the specified Python script (`script.py`) within the context of the project located at `<script_path>`.
    * This is useful when your script relies on dependencies defined within a specific project directory.
    * Example:

        ```bash
        uvr run [options] --project /path/to/project my_script.py [script_options]
        ```

2.  **Using `uvr script.py`:**

    * This is a more direct way to execute your Python script (`script.py`) using `uvr`.
    * `uvr` automatically determines the project directory based on the script path, effectively mimicking the `--project` flag's behavior.
    * Example:

        ```bash
        uvr [options] [--] my_script.py [script_options]
        ```


3.  **Shebang Usage:**

    * Example:

        ```python
        #!/usr/bin/env -S uvr [options] [--]

        # Your Python code here...
        ```

4. **Scripts without `.py` or `.pyw` extension:**
    * Automatic `--script` option is added if not already present (`--script` or `--gui-script`) in options.
    * Otherwise, `uv` might loop indefinitely.

    * Example: For a `foo` script:

        ```python
            #!/usr/bin/env -S uvr [options] [--]

            # Your Python code here...
        ```

        This will be executed as `uv run [options] --script ...` if `[options]` do not already contain `--script` or `--gui-script`.

    * Or, to be more explicit, you can include the `--script`  flag directly in the shebang:

        ```python
        #!/usr/bin/env -S uvr --script
        ```
5.  **Debug usage:**
    * Example:
        ```bash
        uvr -v [options] [--] my_script.py [script_options]
        ```
