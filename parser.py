import os
import sys, json
from antlr4 import FileStream, CommonTokenStream
from generated.SimplePLSQLLexer import SimplePLSQLLexer
from generated.SimplePLSQLParser import SimplePLSQLParser
from src.ast.ast_builder import AstBuilder


def main():
    input_file = "./input/sample.sql"
    output_file = os.path.join("result", "ast.json")

    # Ensure result folder exists
    os.makedirs("result", exist_ok=True)

    # Parse
    input_stream = FileStream(input_file)
    lexer = SimplePLSQLLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = SimplePLSQLParser(tokens)
    tree = parser.program()

    # Build AST
    builder = AstBuilder()
    ast = builder.visit(tree)

    # Save JSON output
    with open(output_file, "w") as f:
        json.dump(ast.to_dict(), f, indent=2)

    print(f"AST JSON saved to {output_file}")

if __name__ == "__main__":
    main()
