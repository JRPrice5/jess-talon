from talon import Context, Module, actions, settings

from ...core.described_functions import create_described_insert_between
from ..tags.operators import Operators

mod = Module()

# Declare new actions for C# (matching TypeScript patterns)
@mod.action_class
class Actions:
    def code_class(text: str):
        """Inserts class declaration"""

    def code_interface(text: str):
        """Inserts interface declaration"""

    def code_enum(text: str):
        """Inserts enum declaration"""

    def code_struct(text: str):
        """Inserts struct declaration"""

    def code_record(text: str):
        """Inserts record declaration"""

    def code_namespace(text: str):
        """Inserts namespace declaration"""

    def code_constant(text: str):
        """Inserts const declaration"""

    def code_variable(text: str):
        """Inserts variable declaration"""

    def code_property(text: str):
        """Inserts property declaration"""

    def code_field(text: str):
        """Inserts field declaration"""

    def code_item(text: str):
        """Inserts item (key = value)"""

    def code_async_function(text: str):
        """Inserts async method declaration"""

    def code_lambda(text: str):
        """Inserts lambda expression"""

    def code_action_lambda(text: str):
        """Inserts Action lambda"""

    def code_func_lambda(text: str):
        """Inserts Func lambda"""

    def code_foreach(text: str):
        """Inserts foreach loop"""


ctx = Context()
ctx.matches = r"""
code.language: csharp
mode: command
"""

ctx.lists["user.code_type"] = {
    "boolean": "bool",
    "bool": "bool",
    "integer": "int",
    "int": "int",
    "string": "string",
    "null": "null",
    "void": "void",
    "double": "double",
    "float": "float",
    "decimal": "decimal",
    "long": "long",
    "short": "short",
    "byte": "byte",
    "char": "char",
    "object": "object",
    "dynamic": "dynamic",
    "var": "var",
}

operators = Operators(
    # code_operators_array
    SUBSCRIPT=create_described_insert_between("[", "]"),
    # code_operators_assignment
    ASSIGNMENT=" = ",
    ASSIGNMENT_ADDITION=" += ",
    ASSIGNMENT_SUBTRACTION=" -= ",
    ASSIGNMENT_DIVISION=" /= ",
    ASSIGNMENT_MULTIPLICATION=" *= ",
    ASSIGNMENT_MODULO=" %= ",
    ASSIGNMENT_BITWISE_AND=" &= ",
    ASSIGNMENT_BITWISE_EXCLUSIVE_OR=" ^= ",
    ASSIGNMENT_BITWISE_LEFT_SHIFT=" <<= ",
    ASSIGNMENT_BITWISE_OR=" |= ",
    ASSIGNMENT_BITWISE_RIGHT_SHIFT=" >>= ",
    ASSIGNMENT_INCREMENT="++",
    # code_operators_bitwise
    BITWISE_NOT="~",
    BITWISE_AND=" & ",
    BITWISE_EXCLUSIVE_OR=" ^ ",
    BITWISE_LEFT_SHIFT=" << ",
    BITWISE_OR=" | ",
    BITWISE_RIGHT_SHIFT=" >> ",
    # code_operators_lambda
    LAMBDA="=>",
    # code_operators_pointer
    MATH_ADD=" + ",
    MATH_SUBTRACT=" - ",
    MATH_MULTIPLY=" * ",
    MATH_DIVIDE=" / ",
    MATH_MODULO=" % ",
    MATH_EQUAL=" == ",
    MATH_NOT_EQUAL=" != ",
    MATH_OR=" || ",
    MATH_AND=" && ",
    MATH_NOT="!",
    MATH_GREATER_THAN_OR_EQUAL=" >= ",
    MATH_GREATER_THAN=" > ",
    MATH_LESS_THAN_OR_EQUAL=" <= ",
    MATH_LESS_THAN=" < ",
    # code_operators_pointer
    POINTER_ADDRESS_OF="&",
    POINTER_INDIRECTION="*",
    POINTER_STRUCTURE_DEREFERENCE="->",
)


@ctx.action_class("user")
class UserActions:
    def code_get_operators() -> Operators:
        return operators

    def code_self():
        actions.auto_insert("this")

    def code_operator_object_accessor():
        actions.auto_insert(".")

    def code_insert_null():
        actions.auto_insert("null")

    def code_insert_is_null():
        actions.auto_insert(" == null ")

    def code_insert_is_not_null():
        actions.auto_insert(" != null")

    def code_insert_true():
        actions.auto_insert("true")

    def code_insert_false():
        actions.auto_insert("false")

    def code_insert_function(text: str, selection: str):
        text += f"({selection or ''})"
        actions.user.paste(text)
        actions.edit.left()

    def code_private_function(text: str):
        """Inserts private function declaration"""
        result = "private void {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    def code_private_static_function(text: str):
        """Inserts private static function"""
        result = "private static void {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    def code_protected_function(text: str):
        result = "private void {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_protected_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    def code_protected_static_function(text: str):
        result = "protected static void {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_protected_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    def code_public_function(text: str):
        result = "public void {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    def code_public_static_function(text: str):
        result = "public static void {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)
