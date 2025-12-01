# nodes.py
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

class ASTNode:
    def to_dict(self) -> Dict[str, Any]:
        result = {"type": self.__class__.__name__}
        for k, v in self.__dict__.items():
            if isinstance(v, ASTNode):
                result[k] = v.to_dict()
            elif isinstance(v, list):
                result[k] = [x.to_dict() if isinstance(x, ASTNode) else x for x in v]
            else:
                result[k] = v
        return result

# Top-level
@dataclass
class Program(ASTNode):
    units: List[ASTNode] = field(default_factory=list)

# Block / declarations / statements
@dataclass
class Block(ASTNode):
    declarations: List["Decl"] = field(default_factory=list)
    statements: List[ASTNode] = field(default_factory=list)

@dataclass
class Decl(ASTNode):
    name: str
    typ: Optional[str] = None
    init: Optional["Expr"] = None

# Statements
@dataclass
class Assignment(ASTNode):
    target: str
    expr: "Expr"
    start_line: Optional[int] = None
    end_line: Optional[int] = None

@dataclass
class IfStmt(ASTNode):
    cond: "Expr"
    then_body: List[ASTNode] = field(default_factory=list)
    else_body: Optional[List[ASTNode]] = None

@dataclass
class WhileStmt(ASTNode):
    cond: "Expr"
    body: List[ASTNode] = field(default_factory=list)

@dataclass
class ReturnStmt(ASTNode):
    expr: Optional["Expr"] = None

@dataclass
class ExitStmt(ASTNode):
    pass

@dataclass
class NullStmt(ASTNode):
    pass

# Expressions
@dataclass
class Expr(ASTNode):
    pass

@dataclass
class BinOp(Expr):
    op: str
    left: Expr
    right: Expr

@dataclass
class IntLiteral(Expr):
    value: int

@dataclass
class VarRef(Expr):
    name: str

@dataclass
class Param(ASTNode):
    name: str
    mode: Optional[str] = None   # 'IN' | 'OUT' | 'IN OUT' | None
    typ: Optional[str] = None

@dataclass
class ProcDecl(ASTNode):
    name: str
    params: List[Param] = field(default_factory=list)
    block: Any = None            # Block node
    is_function: bool = False

@dataclass
class ProcCall(ASTNode):
    name: str
    args: List[Any] = field(default_factory=list)  # list of Expr nodes

@dataclass
class ForStmt(ASTNode):
    var: str
    start_expr: Any
    end_expr: Any
    body: List[Any] = field(default_factory=list)

@dataclass
class SelectInto(ASTNode):
    target: Any       # target node (VarRef or DotRef)
    expr: Any         # select expression (Expr)
    from_table: str
    where_expr: Optional[Any] = None

@dataclass
class DotRef(Expr):
    base: str
    field: str
