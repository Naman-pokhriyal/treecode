# src/ast/ast_builder.py
from generated.SimplePLSQLVisitor import SimplePLSQLVisitor
from generated.SimplePLSQLParser import SimplePLSQLParser

from src.ast.nodes import (
    Program,
    Block,
    Decl,
    Assignment,
    IfStmt,
    WhileStmt,
    ReturnStmt,
    ExitStmt,
    NullStmt,
    BinOp,
    IntLiteral,
    VarRef,
    DotRef,
    SelectInto,
    ForStmt,
    ProcCall,
    ProcDecl,
    Param
)


class AstBuilder(SimplePLSQLVisitor):
    """Visitor converting SimplePLSQL parse tree -> AST nodes."""

    # --- small helpers -------------------------------------------------
    def _id_texts(self, ctx):
        """
        Return list of ID texts for a context that may expose ID() as
        either a single TerminalNode or a list of TerminalNodes.
        """
        if ctx is None:
            return []
        try:
            ids = ctx.ID()
        except Exception:
            return []
        if ids is None:
            return []
        # If a single TerminalNode is returned
        try:
            # If it's a list-like container, iterate
            if isinstance(ids, (list, tuple)):
                return [t.getText() for t in ids]
            # single TerminalNode
            return [ids.getText()]
        except Exception:
            # defensive fallback
            try:
                return [ids.getText()]
            except Exception:
                return []

    def _safe_visit(self, node):
        """Visit node if not None, return None otherwise."""
        if node is None:
            return None
        return self.visit(node)

    def _target_to_str(self, targ_node):
        """Convert VarRef or DotRef into string 'a' or 'a.b'."""
        if isinstance(targ_node, VarRef):
            return targ_node.name
        if isinstance(targ_node, DotRef):
            return f"{targ_node.base}.{targ_node.field}"
        # if it's already a string
        if isinstance(targ_node, str):
            return targ_node
        # fallback: try attributes
        try:
            base = getattr(targ_node, "base", None)
            field = getattr(targ_node, "field", None)
            if base is not None and field is not None:
                return f"{base}.{field}"
        except Exception:
            pass
        return str(targ_node)

    # --- Visitors ----------------------------------------------------
    def visitProgram(self, ctx):
        prog = Program()
        # prefer ctx.unit() if available
        try:
            units = ctx.unit()
            # ctx.unit() often returns a list of UnitContext
        except Exception:
            units = [c for c in ctx.getChildren() if hasattr(c, "getText")]
        if units:
            for u in units:
                node = self._safe_visit(u)
                if node is not None:
                    prog.units.append(node)
        return prog

    def visitUnit(self, ctx):
        if ctx is None:
            return None
        if ctx.proc_decl() is not None:
            return self._safe_visit(ctx.proc_decl())
        if ctx.block() is not None:
            return self._safe_visit(ctx.block())
        if ctx.statement() is not None:
            return self._safe_visit(ctx.statement())
        return None

    def visitBlock(self, ctx):
        if ctx is None:
            return Block()
        try:
            if hasattr(ctx, "proc_body") and ctx.proc_body() is not None:
                return self._safe_visit(ctx.proc_body())
        except Exception:
            pass
        block = Block()
        # declarations
        try:
            if ctx.DECLARE() is not None and ctx.decl_list() is not None:
                decl_list_ctx = ctx.decl_list()
                # decl_list: decl (decl)*
                decls = getattr(decl_list_ctx, "decl", None)
                if callable(decls):
                    dctxs = decls()
                else:
                    dctxs = decls or []
                for dctx in dctxs:
                    dnode = self._safe_visit(dctx)
                    if dnode is not None:
                        block.declarations.append(dnode)
        except Exception:
            # ignore declaration-processing errors and continue
            pass

        # statements inside BEGIN ... END
        try:
            stmt_list_ctx = ctx.stmt_list()
            stmts = getattr(stmt_list_ctx, "statement", None)
            if callable(stmts):
                sctxs = stmts()
            else:
                sctxs = stmts or []
            for sctx in sctxs:
                snode = self._safe_visit(sctx)
                if snode is not None:
                    block.statements.append(snode)
        except Exception:
            pass

        return block

    def visitProc_body(self, ctx):
        # Same structure as block: (DECLARE decl_list)? BEGIN stmt_list END
        block = Block()
        if ctx is None:
            return block
        # declarations
        try:
            if ctx.decl_list() is not None:
                decl_list_ctx = ctx.decl_list()
                decls = getattr(decl_list_ctx, "decl", None)
                dctxs = decls() if callable(decls) else (decls or [])
                for dctx in dctxs:
                    dnode = self._safe_visit(dctx)
                    if dnode is not None:
                        block.declarations.append(dnode)
        except Exception:
            pass

        # statements inside BEGIN ... END
        try:
            stmt_list_ctx = ctx.stmt_list()
            stmts = getattr(stmt_list_ctx, "statement", None)
            sctxs = stmts() if callable(stmts) else (stmts or [])
            for sctx in sctxs:
                snode = self._safe_visit(sctx)
                if snode is not None:
                    block.statements.append(snode)
        except Exception:
            pass

        return block

    def visitDecl(self, ctx):
        # decl : ID (':' ID)? (ASSIGN expr)? SEMI
        ids = self._id_texts(ctx)
        name = ids[0] if ids else "unknown"
        typ = None
        # attempt to read type token if present (some grammars expose as ctx.ID(1))
        if len(ids) > 1:
            typ = ids[1]
        init = None
        try:
            init = self._safe_visit(ctx.expr())
        except Exception:
            init = None
        return Decl(name=name, typ=typ, init=init)

    def visitStatement(self, ctx):
        if ctx is None:
            return None
        if ctx.assignment() is not None:
            return self._safe_visit(ctx.assignment())
        if ctx.if_stmt() is not None:
            return self._safe_visit(ctx.if_stmt())
        if ctx.while_stmt() is not None:
            return self._safe_visit(ctx.while_stmt())
        if ctx.for_stmt() is not None:
            return self._safe_visit(ctx.for_stmt())
        if ctx.proc_call() is not None:
            return self._safe_visit(ctx.proc_call())
        if ctx.select_into() is not None:
            return self._safe_visit(ctx.select_into())
        if ctx.return_stmt() is not None:
            return self._safe_visit(ctx.return_stmt())
        if ctx.exit_stmt() is not None:
            return self._safe_visit(ctx.exit_stmt())
        if ctx.empty_stmt() is not None:
            return self._safe_visit(ctx.empty_stmt())
        return None

    def visitAssignment(self, ctx):
        # assignment : target ASSIGN expr
        if ctx is None:
            return None
        tctx = ctx.target()
        if tctx is None:
            return None

        # build target node
        try:
            targ_node = self.visitTarget(tctx)
        except Exception:
            ids = self._id_texts(tctx)
            if len(ids) == 1:
                targ_node = VarRef(name=ids[0])
            else:
                base = ids[0] if ids else "unknown"
                field = ".".join(ids[1:]) if len(ids) > 1 else ""
                targ_node = DotRef(base=base, field=field)

        expr_node = self._safe_visit(ctx.expr())
        # normalize target to string (Assignment expects a string target)
        target_name = self._target_to_str(targ_node)
        return Assignment(target=target_name, expr=expr_node,
                          start_line=getattr(ctx.start, "line", None),
                          end_line=getattr(ctx.stop, "line", None))

    def visitIf_stmt(self, ctx):
        if ctx is None:
            return None
        cond = self._safe_visit(ctx.expr())
        then_body = []
        else_body = None
        try:
            then_ctx = ctx.stmt_list(0)
            if then_ctx is not None:
                stmts = getattr(then_ctx, "statement", None)
                sctxs = stmts() if callable(stmts) else (stmts or [])
                for sctx in sctxs:
                    node = self._safe_visit(sctx)
                    if node is not None:
                        then_body.append(node)
        except Exception:
            pass

        if ctx.ELSE() is not None:
            else_body = []
            try:
                else_ctx = ctx.stmt_list(1)
                if else_ctx is not None:
                    stmts = getattr(else_ctx, "statement", None)
                    sctxs = stmts() if callable(stmts) else (stmts or [])
                    for sctx in sctxs:
                        node = self._safe_visit(sctx)
                        if node is not None:
                            else_body.append(node)
            except Exception:
                pass

        return IfStmt(cond=cond, then_body=then_body, else_body=else_body)

    def visitWhile_stmt(self, ctx):
        if ctx is None:
            return None
        cond = self._safe_visit(ctx.expr())
        body = []
        try:
            stmt_list_ctx = ctx.stmt_list()
            stmts = getattr(stmt_list_ctx, "statement", None)
            sctxs = stmts() if callable(stmts) else (stmts or [])
            for sctx in sctxs:
                node = self._safe_visit(sctx)
                if node is not None:
                    body.append(node)
        except Exception:
            pass
        return WhileStmt(cond=cond, body=body)

    def visitReturn_stmt(self, ctx):
        expr_node = None
        if ctx is None:
            return ReturnStmt(expr=None)
        try:
            expr_node = self._safe_visit(ctx.expr())
        except Exception:
            expr_node = None
        return ReturnStmt(expr=expr_node)

    def visitExit_stmt(self, ctx):
        return ExitStmt()

    def visitEmpty_stmt(self, ctx):
        return NullStmt()

    # Expressions
    def visitCompExpr(self, ctx):
        if ctx is None:
            return None
        left = self._safe_visit(ctx.expr(0))
        right = self._safe_visit(ctx.expr(1))
        op = getattr(ctx, "op", None)
        op_text = op.text if op is not None else ctx.getChild(1).getText()
        return BinOp(op=op_text, left=left, right=right)

    def visitAddSubExpr(self, ctx):
        left = self._safe_visit(ctx.expr(0))
        right = self._safe_visit(ctx.expr(1))
        op = getattr(ctx, "op", None)
        op_text = op.text if op is not None else ctx.getChild(1).getText()
        return BinOp(op=op_text, left=left, right=right)

    def visitMulDivExpr(self, ctx):
        left = self._safe_visit(ctx.expr(0))
        right = self._safe_visit(ctx.expr(1))
        op = getattr(ctx, "op", None)
        op_text = op.text if op is not None else ctx.getChild(1).getText()
        return BinOp(op=op_text, left=left, right=right)

    def visitLogicExpr(self, ctx):
        left = self._safe_visit(ctx.expr(0))
        right = self._safe_visit(ctx.expr(1))
        op = getattr(ctx, "op", None)
        op_text = op.text if op is not None else ctx.getChild(1).getText()
        return BinOp(op=op_text.upper(), left=left, right=right)

    def visitNotExpr(self, ctx):
        inner = self._safe_visit(ctx.expr())
        # Represent NOT as unary with op='NOT' and left=inner, right=None (or special node)
        return BinOp(op="NOT", left=inner, right=None)

    def visitIntExpr(self, ctx):
        try:
            value = int(ctx.INT().getText())
        except Exception:
            value = 0
        return IntLiteral(value=value)

    def visitIdExpr(self, ctx):
        ids = self._id_texts(ctx)
        if not ids:
            return VarRef(name="unknown")
        # If dotted target returned here, join into dotted string and use VarRef name
        if len(ids) == 1:
            return VarRef(name=ids[0])
        return VarRef(name=".".join(ids))

    def visitParenExpr(self, ctx):
        return self._safe_visit(ctx.expr())

    def visitExpr(self, ctx):
        # Fallback when a specific labeled alt isn't matched.
        if ctx is None:
            return None
        n = ctx.getChildCount()
        if n == 1:
            child = ctx.getChild(0)
            # If the child is a terminal INT, produce IntLiteral
            try:
                sym = child.getSymbol()
                if sym.type == SimplePLSQLParser.INT:
                    return IntLiteral(int(child.getText()))
            except Exception:
                pass
            # Delegate to the child rule if possible (e.g., IdExprOrTarget, func_call, paren)
            node = self._safe_visit(child)
            if node is not None:
                return node
            # Otherwise treat as identifier text
            return VarRef(child.getText())
        if n == 3:
            # binary or paren
            if ctx.expr(0) is not None and ctx.expr(1) is not None:
                left = self._safe_visit(ctx.expr(0))
                right = self._safe_visit(ctx.expr(1))
                op = ctx.getChild(1).getText()
                return BinOp(op=op, left=left, right=right)
            return self._safe_visit(ctx.expr(0))
        return None

    # Additional constructs: proc_decl, params, calls, for, select, target
    def visitProc_decl(self, ctx):
        if ctx is None:
            return None
        ids = self._id_texts(ctx)
        # name is first ID
        name = ids[0] if ids else "anon_proc"
        # return type (if present) may be second ID; safe approach:
        ret_type = ids[1] if len(ids) > 1 else None
        kind_tok = None
        try:
            kind_tok = ctx.getChild(0).getText().upper()
        except Exception:
            kind_tok = None
        is_func = (kind_tok == "FUNCTION")
        params = []
        if ctx.param_list() is not None:
            plist = getattr(ctx.param_list(), "param", None)
            pctxs = plist() if callable(plist) else (plist or [])
            for pctx in pctxs:
                pnode = self._safe_visit(pctx)
                if pnode is not None:
                    params.append(pnode)
        blk = None
        try:
            if hasattr(ctx, "proc_body") and ctx.proc_body() is not None:
                blk = self._safe_visit(ctx.proc_body())
            elif hasattr(ctx, "block") and ctx.block() is not None:
                blk = self._safe_visit(ctx.block())
        except Exception:
            blk = None
        return ProcDecl(name=name, params=params, block=blk, is_function=is_func)

    def visitParam(self, ctx):
        if ctx is None:
            return None
        ids = self._id_texts(ctx)
        name = ids[0] if ids else "p"
        mode = None
        try:
            if ctx.IN() is not None:
                mode = "IN"
            if ctx.OUT() is not None:
                mode = "OUT" if mode is None else "IN OUT"
        except Exception:
            pass
        typ = ids[1] if len(ids) > 1 else None
        return Param(name=name, mode=mode, typ=typ)

    def visitProc_call(self, ctx):
        if ctx is None:
            return None
        try:
            fc = ctx.func_call()
            if fc is not None:
                return self._safe_visit(fc)
        except Exception:
            pass
        name_ids = self._id_texts(ctx)
        name = name_ids[0] if name_ids else "call"
        args = []
        try:
            exprs = getattr(ctx, "expr", None)
            ectxs = exprs() if callable(exprs) else (exprs or [])
            for e in ectxs:
                args.append(self._safe_visit(e))
        except Exception:
            pass
        return ProcCall(name=name, args=args)

    def visitFunc_call(self, ctx):
        if ctx is None:
            return None
        name_ids = self._id_texts(ctx)
        name = name_ids[0] if name_ids else "call"
        args = []
        try:
            exprs = getattr(ctx, "expr", None)
            ectxs = exprs() if callable(exprs) else (exprs or [])
            for e in ectxs:
                args.append(self._safe_visit(e))
        except Exception:
            pass
        return ProcCall(name=name, args=args)

    def visitFuncCallExpr(self, ctx):
        if ctx is None:
            return None
        try:
            return self._safe_visit(ctx.func_call())
        except Exception:
            return None

    def visitIdExprOrTarget(self, ctx):
        if ctx is None:
            return None
        try:
            # Drill into target() so we can get proper VarRef/DotRef
            return self._safe_visit(ctx.target())
        except Exception:
            pass
        # Fallback: try to read IDs directly
        ids = self._id_texts(ctx)
        if not ids:
            return VarRef(name="unknown")
        if len(ids) == 1:
            return VarRef(name=ids[0])
        return DotRef(base=ids[0], field=".".join(ids[1:]))

    def visitFor_stmt(self, ctx):
        if ctx is None:
            return None
        ids = self._id_texts(ctx)
        var = ids[0] if ids else "i"
        er = ctx.expr_range()
        start_expr = self._safe_visit(er.expr(0)) if er is not None else None
        end_expr = self._safe_visit(er.expr(1)) if er is not None else None
        body = []
        try:
            stmt_list_ctx = ctx.stmt_list()
            stmts = getattr(stmt_list_ctx, "statement", None)
            sctxs = stmts() if callable(stmts) else (stmts or [])
            for sctx in sctxs:
                node = self._safe_visit(sctx)
                if node is not None:
                    body.append(node)
        except Exception:
            pass
        return ForStmt(var=var, start_expr=start_expr, end_expr=end_expr, body=body)

    def visitSelect_into(self, ctx):
        if ctx is None:
            return None
        exprs = getattr(ctx, "expr", None)
        expr_list = exprs() if callable(exprs) else (exprs or [])
        sel_expr = self._safe_visit(expr_list[0]) if len(expr_list) > 0 else None
        targ = self._safe_visit(ctx.target())

        # Find table name as the ID immediately following FROM
        from_table = None
        try:
            children = list(ctx.getChildren())
            for i, ch in enumerate(children):
                try:
                    if ch.getText().upper() == "FROM" and i + 1 < len(children):
                        from_table = children[i + 1].getText()
                        break
                except Exception:
                    continue
        except Exception:
            from_table = None

        where_expr = None
        try:
            if ctx.WHERE() is not None and len(expr_list) >= 2:
                where_expr = self._safe_visit(expr_list[1])
        except Exception:
            where_expr = None
        return SelectInto(target=targ, expr=sel_expr, from_table=from_table, where_expr=where_expr)

    def visitTarget(self, ctx):
        ids = self._id_texts(ctx)
        if len(ids) <= 1:
            return VarRef(name=ids[0] if ids else "unknown")
        base = ids[0]
        field = ".".join(ids[1:])
        return DotRef(base=base, field=field)

    # Terminal node fallback: map ID and INT tokens to AST nodes when encountered directly
    def visitTerminal(self, node):
        try:
            t = node.getSymbol().type
            text = node.getText()
            if t == SimplePLSQLParser.ID:
                return VarRef(name=text)
            if t == SimplePLSQLParser.INT:
                return IntLiteral(value=int(text))
        except Exception:
            pass
        return None

    # fallback to continue traversal
    def visitChildren(self, node):
        return super().visitChildren(node)
