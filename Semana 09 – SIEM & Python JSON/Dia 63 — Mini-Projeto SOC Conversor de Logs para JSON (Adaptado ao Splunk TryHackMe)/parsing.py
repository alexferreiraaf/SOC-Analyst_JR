defparse_linha(linha):
if"sshd"notin linha:
returnNone

# regex simplificado para THM
match = re.search(
r"(?P<data>\w+\s+\d+\s+\d+:\d+:\d+).*Failed password for (?P<usuario>\w+) from (?P<ip>\d+\.\d+\.\d+\.\d+)",
        linha
    )

ifnotmatch:
returnNone

return {
"timestamp":match.group("data"),
"usuario":match.group("usuario"),
"ip":match.group("ip"),
"evento":"ssh_failed"
    }

