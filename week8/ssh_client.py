#!/usr/bin/env python3
import argparse
import paramiko
import sys

def run_remote_command(host, user, key_file, command, port=22, timeout=10):
    """
    Connects to the remote host via SSH using the given private key,
    runs the specified command, and returns (exit_status, stdout, stderr).
    """
    # Create SSH client
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Load private key
        pkey = paramiko.RSAKey.from_private_key_file(key_file)
    except Exception as e:
        print(f"ERROR loading key {key_file}: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        client.connect(
            hostname=host,
            port=port,
            username=user,
            pkey=pkey,
            timeout=timeout
        )
    except Exception as e:
        print(f"ERROR connecting to {host}: {e}", file=sys.stderr)
        sys.exit(1)

    # Run the command
    stdin, stdout, stderr = client.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()
    out = stdout.read().decode()
    err = stderr.read().decode()

    client.close()
    return exit_status, out, err

def main():
    parser = argparse.ArgumentParser(
        description="Run a command on a remote host via SSH using a private key"
    )
    parser.add_argument("--host",         required=True, help="Remote host (IP or hostname)")
    parser.add_argument("--user",         required=True, help="SSH username")
    parser.add_argument("--identityfile", required=True, help="Path to private key file")
    parser.add_argument("--command",      required=True, help="Command to execute remotely")
    parser.add_argument("--port",         type=int, default=22, help="SSH port (default: 22)")
    parser.add_argument("--timeout",      type=int, default=10, help="Connection timeout in seconds")

    args = parser.parse_args()

    status, out, err = run_remote_command(
        host=args.host,
        user=args.user,
        key_file=args.identityfile,
        command=args.command,
        port=args.port,
        timeout=args.timeout
    )

    print(f"\n--- SSH COMMAND OUTPUT (exit code {status}) ---")
    if out:
        print(out.rstrip())
    if err:
        print(f"\n--- SSH COMMAND STDERR ---\n{err.rstrip()}", file=sys.stderr)

    sys.exit(status)

if __name__ == "__main__":
    main()
