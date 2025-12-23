def parse_linha(linha):
    match = regex_ssh.search(linha)
    if not match:
        return None

    status_raw = match.group("status")

    return {
        "timestamp": match.group("data"),
        "src_ip": match.group("ip"),
        "user": match.group("usuario"),
        "event_type": "ssh_login",
        "status": "failed" if status_raw == "Failed" else "success",
        "service": "ssh"
    }

