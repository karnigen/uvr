

# Simple Script Execution with uvr

Unfortunately, `uv` prioritizes virtual environments within the current directory. This makes it cumbersome to execute scripts located elsewhere, requiring the use of the `--project` flag.

This script offers a streamlined workaround for running Python scripts via `uv`, allowing you to use `uvr script.py` instead of `uv run --project <script_path> script.py`."



## Installation

To install `uvr`, use the following command:

```bash
uv tool install --from git+https://github.com/karnigen/uvr uvr
```


## Usage

Several ways to run your Python scripts with `uv`:

1.  **Using `uv run --project <script_path> script.py`:**

    * This command explicitly tells `uv` to run the specified Python script (`script.py`) within the context of the project located at `<script_path>`.
    * This is useful when your script relies on dependencies defined within a specific project directory.
    * Example:

        ```bash
        uvr run --project /path/to/your/project my_script.py
        ```

2.  **Using `uvr script.py`:**

    * This is a more direct way to execute your Python script (`script.py`) using `uvr`.
    * `uvr` will attempt to resolve any dependencies required by the script.
    * Example:

        ```bash
        uvr my_script.py
        ```


3.  **Shebang Usage:**

    * Example:

        ```python
        #!/usr/bin/env uvr

        # Your Python code here...
        ```
