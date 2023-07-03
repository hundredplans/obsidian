```
BEGIN {
  print "PID:", PROCINFO["pid"]
  print "PPID:", PROCINFO["ppid"]
  print "UID:", PROCINFO["uid"]
  print "GID:", PROCINFO["gid"]
  print "EGID:", PROCINFO["egid"]
  print "EUID:", PROCINFO["euid"]
  print "Command Line:", PROCINFO["cmdline"]
  print "Program Name:", PROCINFO["name"]
  print "Awk Version:", PROCINFO["version"]
}

```