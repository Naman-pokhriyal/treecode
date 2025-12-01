-- sample_full.sql
-- Uses: PROCEDURE, FUNCTION, DECLARE, BEGIN/END, IF, WHILE, FOR, SELECT INTO, calls, dotted access

PROCEDURE inc_by(n IN INTEGER) IS
BEGIN
  x := x + n;
END inc_by;

FUNCTION sum_to(n IN INTEGER) RETURN INTEGER IS
BEGIN
  total := 0;
  FOR i IN 1..n LOOP
    total := total + i;
  END LOOP;
  RETURN total;
END sum_to;

DECLARE
  x := 10;
  y := 3;
  rec := 0;
  val := 0;
  total := 0;
  s := 0;
BEGIN
  -- call a procedure
  inc_by(5);

  -- IF with comparison and boolean ops
  IF x > 5 AND y < 10 THEN
    x := x + 1;
  ELSE
    x := 0;
  END IF;

  -- WHILE loop
  i := 0;
  WHILE i < 3 LOOP
    i := i + 1;
    -- dotted access example (record.field)
    rec := rec + obj.field;
  END LOOP;

  -- FOR loop + SELECT INTO (simplified single-row select)
  total := 0;
  FOR j IN 1..5 LOOP
    SELECT a INTO val FROM mytable WHERE id = j;
    total := total + val;
  END LOOP;

  -- call function and assign
  s := sum_to(5);

  -- demonstrate NULL and EXIT
  IF total > 0 OR s = 15 THEN
    NULL;
  ELSE
    EXIT;
  END IF;

  -- dotted assignment
  obj.field := total;
END;
