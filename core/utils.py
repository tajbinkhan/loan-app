from django.template import loader

def add_context_to_string(template_str, context) -> str:
	engines = loader._engine_list()
	for engine in engines:
		try:
			template = engine.from_string(template_str)
			return template.render(context)
		except AttributeError:
			continue
	else:
		raise ValueError("Could not find a template engine that can render the string.")