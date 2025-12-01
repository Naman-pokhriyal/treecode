# Generated from grammer/SimplePLSQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimplePLSQLParser import SimplePLSQLParser
else:
    from SimplePLSQLParser import SimplePLSQLParser

# This class defines a complete generic visitor for a parse tree produced by SimplePLSQLParser.

class SimplePLSQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimplePLSQLParser#program.
    def visitProgram(self, ctx:SimplePLSQLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#unit.
    def visitUnit(self, ctx:SimplePLSQLParser.UnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#proc_decl.
    def visitProc_decl(self, ctx:SimplePLSQLParser.Proc_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#param_list.
    def visitParam_list(self, ctx:SimplePLSQLParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#param.
    def visitParam(self, ctx:SimplePLSQLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#proc_body.
    def visitProc_body(self, ctx:SimplePLSQLParser.Proc_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#block.
    def visitBlock(self, ctx:SimplePLSQLParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#decl_list.
    def visitDecl_list(self, ctx:SimplePLSQLParser.Decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#decl.
    def visitDecl(self, ctx:SimplePLSQLParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#stmt_list.
    def visitStmt_list(self, ctx:SimplePLSQLParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#statement.
    def visitStatement(self, ctx:SimplePLSQLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#assignment.
    def visitAssignment(self, ctx:SimplePLSQLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#target.
    def visitTarget(self, ctx:SimplePLSQLParser.TargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#if_stmt.
    def visitIf_stmt(self, ctx:SimplePLSQLParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#while_stmt.
    def visitWhile_stmt(self, ctx:SimplePLSQLParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#for_stmt.
    def visitFor_stmt(self, ctx:SimplePLSQLParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#expr_range.
    def visitExpr_range(self, ctx:SimplePLSQLParser.Expr_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#func_call.
    def visitFunc_call(self, ctx:SimplePLSQLParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#proc_call.
    def visitProc_call(self, ctx:SimplePLSQLParser.Proc_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#select_into.
    def visitSelect_into(self, ctx:SimplePLSQLParser.Select_intoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#return_stmt.
    def visitReturn_stmt(self, ctx:SimplePLSQLParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#exit_stmt.
    def visitExit_stmt(self, ctx:SimplePLSQLParser.Exit_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#empty_stmt.
    def visitEmpty_stmt(self, ctx:SimplePLSQLParser.Empty_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:SimplePLSQLParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#LogicExpr.
    def visitLogicExpr(self, ctx:SimplePLSQLParser.LogicExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#IdExprOrTarget.
    def visitIdExprOrTarget(self, ctx:SimplePLSQLParser.IdExprOrTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#CompExpr.
    def visitCompExpr(self, ctx:SimplePLSQLParser.CompExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#NotExpr.
    def visitNotExpr(self, ctx:SimplePLSQLParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#IntExpr.
    def visitIntExpr(self, ctx:SimplePLSQLParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#ParenExpr.
    def visitParenExpr(self, ctx:SimplePLSQLParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:SimplePLSQLParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#FuncCallExpr.
    def visitFuncCallExpr(self, ctx:SimplePLSQLParser.FuncCallExprContext):
        return self.visitChildren(ctx)



del SimplePLSQLParser