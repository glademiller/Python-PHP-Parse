import re

def parse_php_assignments(php):
	reg = r'\$(?P<variable>\w+)\s*=\s*"?\'?(?P<value>[^"\';]+)"?\'?;'
	rg = re.compile(reg,re.IGNORECASE|re.DOTALL)
	return rg.findall(php)


