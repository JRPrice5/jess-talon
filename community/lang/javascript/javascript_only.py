from talon import Context, actions, settings

ctx = Context()
ctx.matches = r"""
code.language: javascript
code.language: javascriptreact
"""


@ctx.action_class("user")
class UserActions:
    def code_class(text: str):
        """Inserts class declaration"""
        formatted_name = actions.user.formatted_text(text, "PUBLIC_CAMEL_CASE")
        actions.user.insert_snippet_by_name(
            "classDeclaration", {"1": formatted_name}
        )

    def code_constant(text: str):
        """Inserts const declaration (untyped)"""
        formatted_name = actions.user.formatted_text(
            text, settings.get("user.code_private_variable_formatter")
        )
        actions.user.insert_snippet_by_name(
            "constantAssignment", {"1": formatted_name}
        )

    def code_variable(text: str):
        """Inserts let declaration (untyped)"""
        formatted_name = actions.user.formatted_text(
            text, settings.get("user.code_private_variable_formatter")
        )
        actions.user.insert_snippet_by_name(
            "variableAssignment", {"1": formatted_name}
        )

    def code_property(text: str):
        """Inserts property declaration"""
        formatted_name = actions.user.formatted_text(
            text, settings.get("user.code_private_variable_formatter")
        )
        actions.user.insert_snippet_by_name(
            "item", {"1": formatted_name}
        )

    def code_item(text: str):
        """Inserts object item (key: value)"""
        formatted_name = actions.user.formatted_text(
            text, settings.get("user.code_private_variable_formatter")
        )
        actions.user.insert_snippet_by_name(
            "item", {"1": formatted_name}
        )
