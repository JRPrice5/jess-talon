code.language: csharp
-
tag(): user.code_imperative
tag(): user.code_object_oriented

tag(): user.code_comment_line
tag(): user.code_comment_block_c_like
tag(): user.code_data_bool
tag(): user.code_data_null
tag(): user.code_functions
tag(): user.code_functions_common
tag(): user.code_libraries
tag(): user.code_operators_array
tag(): user.code_operators_assignment
tag(): user.code_operators_bitwise
tag(): user.code_operators_lambda
tag(): user.code_operators_math
tag(): user.code_operators_pointer

settings():
    user.code_private_function_formatter = "PRIVATE_CAMEL_CASE"
    user.code_protected_function_formatter = "PUBLIC_CAMEL_CASE"
    user.code_public_function_formatter = "PUBLIC_CAMEL_CASE"
    user.code_private_variable_formatter = "PRIVATE_CAMEL_CASE"
    user.code_protected_variable_formatter = "PUBLIC_CAMEL_CASE"
    user.code_public_variable_formatter = "PUBLIC_CAMEL_CASE"

# Typed declarations (matching TypeScript patterns)
snip class <user.text>: user.code_class(text)
snip interface <user.text>: user.code_interface(text)
snip enum <user.text>: user.code_enum(text)
snip struct <user.text>: user.code_struct(text)
snip record <user.text>: user.code_record(text)
snip namespace <user.text>: user.code_namespace(text)

# Typed variable declarations
snip constant <user.text>: user.code_constant(text)
snip variable <user.text>: user.code_variable(text)

# Typed members
snip property <user.text>: user.code_property(text)
snip field <user.text>: user.code_field(text)
snip item <user.text>: user.code_item(text)

# Typed function declarations
snip async funky <user.text>: user.code_async_function(text)
snip lambda <user.text>: user.code_lambda(text)
snip action <user.text>: user.code_action_lambda(text)
snip funk <user.text>: user.code_func_lambda(text)

# Control flow
snip try catch: user.insert_snippet_by_name("tryCatchStatement")
snip for each <user.text>: user.code_foreach(text)
snip using: user.insert_snippet_by_name("usingStatement")

# Type annotations
snip type [<user.code_type>]: user.code_insert_type_annotation(code_type or "")
