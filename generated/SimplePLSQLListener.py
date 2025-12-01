# Generated from grammer/SimplePLSQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimplePLSQLParser import SimplePLSQLParser
else:
    from SimplePLSQLParser import SimplePLSQLParser

# This class defines a complete listener for a parse tree produced by SimplePLSQLParser.
class SimplePLSQLListener(ParseTreeListener):

    # Enter a parse tree produced by SimplePLSQLParser#program.
    def enterProgram(self, ctx:SimplePLSQLParser.ProgramContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#program.
    def exitProgram(self, ctx:SimplePLSQLParser.ProgramContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#unit.
    def enterUnit(self, ctx:SimplePLSQLParser.UnitContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#unit.
    def exitUnit(self, ctx:SimplePLSQLParser.UnitContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#proc_decl.
    def enterProc_decl(self, ctx:SimplePLSQLParser.Proc_declContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#proc_decl.
    def exitProc_decl(self, ctx:SimplePLSQLParser.Proc_declContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#param_list.
    def enterParam_list(self, ctx:SimplePLSQLParser.Param_listContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#param_list.
    def exitParam_list(self, ctx:SimplePLSQLParser.Param_listContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#param.
    def enterParam(self, ctx:SimplePLSQLParser.ParamContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#param.
    def exitParam(self, ctx:SimplePLSQLParser.ParamContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#proc_body.
    def enterProc_body(self, ctx:SimplePLSQLParser.Proc_bodyContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#proc_body.
    def exitProc_body(self, ctx:SimplePLSQLParser.Proc_bodyContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#block.
    def enterBlock(self, ctx:SimplePLSQLParser.BlockContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#block.
    def exitBlock(self, ctx:SimplePLSQLParser.BlockContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#decl_list.
    def enterDecl_list(self, ctx:SimplePLSQLParser.Decl_listContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#decl_list.
    def exitDecl_list(self, ctx:SimplePLSQLParser.Decl_listContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#decl.
    def enterDecl(self, ctx:SimplePLSQLParser.DeclContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#decl.
    def exitDecl(self, ctx:SimplePLSQLParser.DeclContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#stmt_list.
    def enterStmt_list(self, ctx:SimplePLSQLParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#stmt_list.
    def exitStmt_list(self, ctx:SimplePLSQLParser.Stmt_listContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#statement.
    def enterStatement(self, ctx:SimplePLSQLParser.StatementContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#statement.
    def exitStatement(self, ctx:SimplePLSQLParser.StatementContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#assignment.
    def enterAssignment(self, ctx:SimplePLSQLParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#assignment.
    def exitAssignment(self, ctx:SimplePLSQLParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#target.
    def enterTarget(self, ctx:SimplePLSQLParser.TargetContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#target.
    def exitTarget(self, ctx:SimplePLSQLParser.TargetContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#if_stmt.
    def enterIf_stmt(self, ctx:SimplePLSQLParser.If_stmtContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#if_stmt.
    def exitIf_stmt(self, ctx:SimplePLSQLParser.If_stmtContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#while_stmt.
    def enterWhile_stmt(self, ctx:SimplePLSQLParser.While_stmtContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#while_stmt.
    def exitWhile_stmt(self, ctx:SimplePLSQLParser.While_stmtContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#for_stmt.
    def enterFor_stmt(self, ctx:SimplePLSQLParser.For_stmtContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#for_stmt.
    def exitFor_stmt(self, ctx:SimplePLSQLParser.For_stmtContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#expr_range.
    def enterExpr_range(self, ctx:SimplePLSQLParser.Expr_rangeContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#expr_range.
    def exitExpr_range(self, ctx:SimplePLSQLParser.Expr_rangeContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#func_call.
    def enterFunc_call(self, ctx:SimplePLSQLParser.Func_callContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#func_call.
    def exitFunc_call(self, ctx:SimplePLSQLParser.Func_callContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#proc_call.
    def enterProc_call(self, ctx:SimplePLSQLParser.Proc_callContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#proc_call.
    def exitProc_call(self, ctx:SimplePLSQLParser.Proc_callContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#select_into.
    def enterSelect_into(self, ctx:SimplePLSQLParser.Select_intoContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#select_into.
    def exitSelect_into(self, ctx:SimplePLSQLParser.Select_intoContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#return_stmt.
    def enterReturn_stmt(self, ctx:SimplePLSQLParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#return_stmt.
    def exitReturn_stmt(self, ctx:SimplePLSQLParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#exit_stmt.
    def enterExit_stmt(self, ctx:SimplePLSQLParser.Exit_stmtContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#exit_stmt.
    def exitExit_stmt(self, ctx:SimplePLSQLParser.Exit_stmtContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#empty_stmt.
    def enterEmpty_stmt(self, ctx:SimplePLSQLParser.Empty_stmtContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#empty_stmt.
    def exitEmpty_stmt(self, ctx:SimplePLSQLParser.Empty_stmtContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:SimplePLSQLParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:SimplePLSQLParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#LogicExpr.
    def enterLogicExpr(self, ctx:SimplePLSQLParser.LogicExprContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#LogicExpr.
    def exitLogicExpr(self, ctx:SimplePLSQLParser.LogicExprContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#IdExprOrTarget.
    def enterIdExprOrTarget(self, ctx:SimplePLSQLParser.IdExprOrTargetContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#IdExprOrTarget.
    def exitIdExprOrTarget(self, ctx:SimplePLSQLParser.IdExprOrTargetContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#CompExpr.
    def enterCompExpr(self, ctx:SimplePLSQLParser.CompExprContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#CompExpr.
    def exitCompExpr(self, ctx:SimplePLSQLParser.CompExprContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#NotExpr.
    def enterNotExpr(self, ctx:SimplePLSQLParser.NotExprContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#NotExpr.
    def exitNotExpr(self, ctx:SimplePLSQLParser.NotExprContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#IntExpr.
    def enterIntExpr(self, ctx:SimplePLSQLParser.IntExprContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#IntExpr.
    def exitIntExpr(self, ctx:SimplePLSQLParser.IntExprContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#ParenExpr.
    def enterParenExpr(self, ctx:SimplePLSQLParser.ParenExprContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#ParenExpr.
    def exitParenExpr(self, ctx:SimplePLSQLParser.ParenExprContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:SimplePLSQLParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:SimplePLSQLParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by SimplePLSQLParser#FuncCallExpr.
    def enterFuncCallExpr(self, ctx:SimplePLSQLParser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by SimplePLSQLParser#FuncCallExpr.
    def exitFuncCallExpr(self, ctx:SimplePLSQLParser.FuncCallExprContext):
        pass



del SimplePLSQLParser