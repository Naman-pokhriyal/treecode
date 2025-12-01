# SimplePLSQL Parser — Runbook

This project parses a simplified PL/SQL-like language (ANTLR4 grammar in `grammer/SimplePLSQL.g4`) and builds a JSON AST from `input/sample.sql`, writing output to `result/ast.json`.

Below are the exact commands to:

1. Activate the Python virtual environment
2. Generate/refresh ANTLR parser/lexer/visitor
3. Run the parser

Note: All commands assume you are in the project root: `d:/NAMJAM/AI/mvp`

---

## 1) Activate the virtual environment (Windows)

- Command Prompt (cmd.exe):

```
myenv\Scripts\activate
```

- PowerShell:

```
myenv\Scripts\Activate.ps1
```

- Git Bash (optional; activation is not strictly required if you call the venv executables directly):

```
source myenv/Scripts/activate
```

You can also skip activation and call the virtualenv executables explicitly using their full paths as shown below.

---

## 2) Generate ANTLR artifacts (parser, lexer, visitor)

Run this whenever you change `grammer/SimplePLSQL.g4`.

- Command Prompt (cmd.exe) or PowerShell:

```
antlr4 -Dlanguage=Python3 -visitor -o generated grammer\SimplePLSQL.g4
```

- Git Bash:

```
./myenv/Scripts/antlr4.exe -Dlanguage=Python3 -visitor -o generated grammer/SimplePLSQL.g4
```

Artifacts will be written to the `generated/` directory.

---

## 3) Run the parser

- Command Prompt (cmd.exe) or PowerShell:

```
python parser.py
```

- Git Bash:

```
./myenv/Scripts/python.exe parser.py
```

Expected output:

```
AST JSON saved to result\ast.json
```

---

## Inputs and Outputs

- Input SQL file: `input/sample.sql`
- Grammar: `grammer/SimplePLSQL.g4`
- Generated parser code: `generated/`
- AST JSON output: `result/ast.json`

If you change the grammar, re-run step (2) before step (3).

---

## Notes / Troubleshooting

- If `antlr4.exe` is not found, ensure you are using the provided virtual environment (`myenv`) and that you are running commands from the project root.
- Division operator `/` is supported. A single slash on its own line is treated as a script terminator and ignored.
- Keywords are currently case-sensitive; use uppercase (e.g., `BEGIN`, `END`, `IF`, `THEN`, `ELSE`, etc.).
