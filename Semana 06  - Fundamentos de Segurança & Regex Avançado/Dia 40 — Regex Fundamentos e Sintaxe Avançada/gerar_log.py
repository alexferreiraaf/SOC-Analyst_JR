with open("auth_sample_large.log", "w") as f:
    for i in range(1_000_000):
        f.write(f"Oct 8 12:{i%60:02d}:{i%60:02d} sshd[{1000+i}]: Failed login for user{i%50} from Source Network Address: 192.168.{i%255}.{i%255}\n")
