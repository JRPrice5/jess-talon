from talon import Context, Module, actions, settings

mod = Module()

# Declare new actions
@mod.action_class
class Actions:
    def code_class(text: str):
        """Inserts class declaration"""

    def code_interface(text: str):
        """Inserts interface declaration"""

    def code_enum(text: str):
        """Inserts enum declaration"""

    def code_constant(text: str):
        """Inserts const declaration"""

    def code_variable(text: str):
        """Inserts let/var declaration"""

    def code_property(text: str):
        """Inserts property declaration"""

    def code_item(text: str):
        """Inserts object item (key: value)"""

    def code_async_function(text: str):
        """Inserts async function declaration"""

    def code_arrow_function(text: str):
        """Inserts arrow function declaration"""


ctx = Context()
ctx.matches = r"""
code.language: typescript
code.language: typescriptreact
mode: command
"""

ctx.lists["user.code_type"] = {
    "boolean": "boolean",
    "integer": "int",
    "string": "string",
    "null": "null",
    "undefined": "undefined",
    "number": "number",
    "any": "any",
}


@ctx.action_class("user")
class UserActions:
    def code_default_function(text: str):
        """Inserts typed function declaration"""
        formatted_name = actions.user.formatted_text(
            text, settings.get("user.code_private_function_formatter")
        )
        actions.user.insert_snippet_by_name(
            "functionDeclaration", {"1": formatted_name}
        )

    def code_private_function(text: str):
        """Inserts typed private method declaration"""
        formatted_name = actions.user.formatted_text(
            text, settings.get("user.code_private_function_formatter")
        )
        actions.user.insert_snippet_by_name(
            "privateMethodDeclaration", {"1": formatted_name}
        )

    def code_protected_function(text: str):
        """Inserts typed protected method declaration"""
        formatted_name = actions.user.formatted_text(
            text, settings.get("user.code_protected_function_formatter")
        )
        actions.user.insert_snippet_by_name(
            "protectedMethodDeclaration", {"1": formatted_name}
        )

    def code_public_function(text: str):
        """Inserts typed public method declaration"""
        formatted_name = actions.user.formatted_text(
            text, settings.get("user.code_public_function_formatter")
        )
        actions.user.insert_snippet_by_name(
            "publicMethodDeclaration", {"1": formatted_name}
        )

    def code_async_function(text: str):
        """Inserts typed async function declaration"""
        formatted_name = actions.user.formatted_text(
            text, settings.get("user.code_private_function_formatter")
        )
        actions.user.insert_snippet_by_name(
            "asyncFunctionDeclaration", {"1": formatted_name}
        )

    def code_arrow_function(text: str):
        """Inserts typed arrow function declaration"""
        formatted_name = actions.user.formatted_text(
            text, settings.get("user.code_private_function_formatter")
        )
        actions.user.insert_snippet_by_name(
            "typedArrowFunction", {"1": formatted_name}
        )

    def code_class(text: str):
        """Inserts class declaration"""
        formatted_name = actions.user.formatted_text(text, "PUBLIC_CAMEL_CASE")
        actions.user.insert_snippet_by_name(
            "classDeclaration", {"1": formatted_name}
        )

    def code_interface(text: str):
        """Inserts interface declaration"""
        formatted_name = actions.user.formatted_text(text, "PUBLIC_CAMEL_CASE")
        actions.user.insert_snippet_by_name(
            "interfaceDeclaration", {"1": formatted_name}
        )

    def code_enum(text: str):
        """Inserts enum declaration"""
        formatted_name = actions.user.formatted_text(text, "PUBLIC_CAMEL_CASE")
        actions.user.insert_snippet_by_name(
            "enumDeclaration", {"1": formatted_name}
        )

    def code_constant(text: str):
        """Inserts typed const declaration"""
        formatted_name = actions.user.formatted_text(
            text, settings.get("user.code_private_variable_formatter")
        )
        actions.user.insert_snippet_by_name(
            "typedConstAssignment", {"1": formatted_name}
        )

    def code_variable(text: str):
        """Inserts typed let declaration"""
        formatted_name = actions.user.formatted_text(
            text, settings.get("user.code_private_variable_formatter")
        )
        actions.user.insert_snippet_by_name(
            "typedLetAssignment", {"1": formatted_name}
        )

    def code_property(text: str):
        """Inserts typed property declaration"""
        formatted_name = actions.user.formatted_text(
            text, settings.get("user.code_private_variable_formatter")
        )
        actions.user.insert_snippet_by_name(
            "property", {"1": formatted_name}
        )

    def code_item(text: str):
        """Inserts object item (key: value)"""
        formatted_name = actions.user.formatted_text(
            text, settings.get("user.code_private_variable_formatter")
        )
        actions.user.insert_snippet_by_name(
            "item", {"1": formatted_name}
        )

    def code_insert_type_annotation(type: str):
        actions.insert(f": {type}")

    def code_insert_return_type(type: str):
        actions.insert(f": {type}")
