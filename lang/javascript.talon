title: /.*\.jsx?$/
title: /.*\.tsx?$/
-
type {user.javascript_types}: insert(javascript_types)
type {user.javascript_types} array: "{javascript_types}[]""
iffae:
	"if () {}"
	key(left enter up home right:4)
shells:
	"else {}"
	key(left)
shell iffae:
	"else if () {}"
	key(left enter up end left:3)
constant: "const "
constant <phrase>: "const {user.camel(phrase)} = "
letter: "let "
letter <phrase>: "let {user.camel(phrase)} = "
arrow: " => "
class name: "className="
return: "return "
semi: key(end:2 ;)
create structure <phrase>:
	"type {user.title(phrase)} = {{}};"
	key(left:2 enter)
