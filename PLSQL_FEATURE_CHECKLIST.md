# PL/SQL Grammar Coverage Checklist

## Legend

- ✓ = Supported in current grammar/AST
- ✗ = Missing / Not implemented yet
- Partial = Some support but incomplete

---

## 1️⃣ Declarations & Types

- ✓ Variable declarations with initialization
- ✓ Procedure / Function declarations with IN parameters
- ✓ Function return / RETURN
- ✓ CONSTANT declarations
- ✓ %TYPE and %ROWTYPE attributes
- ✓ Typed declarations with precision (e.g., NUMBER(p,s), VARCHAR2(n))
- ✓ NOT NULL, DEFAULT modifiers
- ✓ Record types (TYPE ... IS RECORD)
- ✓ User-defined object types (CREATE TYPE)
- ✓ Collections (associative arrays, nested tables, varrays)
- ✓ Cursor variable / REF CURSOR declarations
- ✓ PRAGMA attributes

## 2️⃣ Expressions & Operators

- ✓ Numeric / literal expressions
- ✓ Variable references
- ✓ Dot field access (obj.field)
- ✓ Binary ops: + - > < = AND OR
- ✗ Additional ops: NOT, IN, LIKE, BETWEEN, IS NULL
- ✗ Built-in and function calls as expressions

## 3️⃣ Control Flow

- ✓ IF / THEN / ELSE
- ✓ WHILE loop
- ✓ Numeric FOR loop
- ✓ NULL statement
- Partial: Labels & GOTO
- ✗ Unconditional LOOP…END LOOP
- ✗ EXIT WHEN
- ✗ CONTINUE
- ✗ CASE statement (simple & searched)

## 4️⃣ Exception Handling

- ✗ EXCEPTION block
- ✗ WHEN handlers
- ✗ OTHERS
- ✗ RAISE / RAISE_APPLICATION_ERROR

## 5️⃣ SQL & Database Operations

- ✓ SELECT INTO (simple form)
- ✗ INSERT / UPDATE / DELETE / MERGE
- ✗ EXECUTE IMMEDIATE
- ✗ Bulk operations: BULK COLLECT, FORALL
- ✗ Explicit cursors (OPEN, FETCH, CLOSE)
- ✗ Advanced SQL queries (joins, GROUP BY, HAVING, aggregates)
- ✗ Transaction statements (COMMIT, ROLLBACK, SAVEPOINT)

## 6️⃣ Cursor Logic

- ✗ Cursor declarations
- ✗ REF CURSOR
- ✗ Cursor FOR loops

## 7️⃣ Packaging & Triggers

- ✗ PACKAGE and PACKAGE BODY
- ✗ TRIGGER support
- ✗ :NEW and :OLD pseudorecords

## 8️⃣ Advanced PL/SQL Features

- ✗ PRAGMA (autonomous transaction, etc.)
- ✗ Overloading
- ✗ OUT / IN OUT parameters
- ✓ Function usage rules implemented properly (procedures disallow return)

## 9️⃣ Misc

- ✓ Line metadata tracking (start_line, end_line)
- ✗ DBMS_OUTPUT calls (as part of AST)
