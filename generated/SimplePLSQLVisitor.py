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


    # Visit a parse tree produced by SimplePLSQLParser#constant_modifier.
    def visitConstant_modifier(self, ctx:SimplePLSQLParser.Constant_modifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#not_null.
    def visitNot_null(self, ctx:SimplePLSQLParser.Not_nullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#init.
    def visitInit(self, ctx:SimplePLSQLParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#type_decl.
    def visitType_decl(self, ctx:SimplePLSQLParser.Type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#record_type_body.
    def visitRecord_type_body(self, ctx:SimplePLSQLParser.Record_type_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#record_fields.
    def visitRecord_fields(self, ctx:SimplePLSQLParser.Record_fieldsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#field.
    def visitField(self, ctx:SimplePLSQLParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#collection_type_body.
    def visitCollection_type_body(self, ctx:SimplePLSQLParser.Collection_type_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#ref_cursor_body.
    def visitRef_cursor_body(self, ctx:SimplePLSQLParser.Ref_cursor_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#cursor_decl.
    def visitCursor_decl(self, ctx:SimplePLSQLParser.Cursor_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#cursor_params.
    def visitCursor_params(self, ctx:SimplePLSQLParser.Cursor_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#cursor_select.
    def visitCursor_select(self, ctx:SimplePLSQLParser.Cursor_selectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#select_list.
    def visitSelect_list(self, ctx:SimplePLSQLParser.Select_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#pragma_stmt.
    def visitPragma_stmt(self, ctx:SimplePLSQLParser.Pragma_stmtContext):
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


    # Visit a parse tree produced by SimplePLSQLParser#type_spec.
    def visitType_spec(self, ctx:SimplePLSQLParser.Type_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#simple_type.
    def visitSimple_type(self, ctx:SimplePLSQLParser.Simple_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#numeric_type.
    def visitNumeric_type(self, ctx:SimplePLSQLParser.Numeric_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#char_type.
    def visitChar_type(self, ctx:SimplePLSQLParser.Char_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#pct_attr.
    def visitPct_attr(self, ctx:SimplePLSQLParser.Pct_attrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimplePLSQLParser#qualified_name.
    def visitQualified_name(self, ctx:SimplePLSQLParser.Qualified_nameContext):
        return self.visitChildren(ctx)



del SimplePLSQLParser