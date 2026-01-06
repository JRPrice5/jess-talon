code.language: typescript
code.language: typescriptreact
-

snip type union [<user.code_type>]: " | {code_type or ''}"
snip type intersect [<user.code_type>]: " & {code_type or ''}"

snip state type: user.insert_between("type ", " = ")

snip as const: " as const"

# Typed function declarations
snip async funky <user.text>: user.code_async_function(text)
snip arrow funky <user.text>: user.code_arrow_function(text)

# Typed declarations
snip class <user.text>: user.code_class(text)
snip interface <user.text>: user.code_interface(text)
snip enum <user.text>: user.code_enum(text)

# Typed variable declarations
snip constant <user.text>: user.code_constant(text)
snip variable <user.text>: user.code_variable(text)

# Typed members
snip property <user.text>: user.code_property(text)
snip item <user.text>: user.code_item(text)

snip try catch: user.insert_snippet_by_name("tryCatchStatement")
