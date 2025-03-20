# Week 9-10 README

## Week 9 Files

- wk09b1_tcp_server.py
- wk09b2_tcp_client.py
- wk09b2_tcp_server.py
- wk09b3_tcp_client.py
- wk09b3_tcp_socket_client.py
- wk09b3_tcp_socket_server.py
- wk09c1_udp_client.py
- wk09c1_udp_server.py

## Week 10 Files

- wk10a_tcp_client_ssl.py
- wk10a_tcp_server_ssl.py
- wk10b_tcp_client_ssl.py
- wk10b_tcp_server_ssl.py

## Generating OpenSSL Certificate and Key (Week 10)

```bash
openssl req -new -x509 -days 365 -nodes -out server.crt -keyout server.key
```

1. openssl: This is the command-line tool for using the OpenSSL library, which provides various cryptographic functions, including the ability to create and manage SSL/TLS certificates.

2. req: This subcommand is used to create and process certificate requests in PKCS#10 format. It can also be used to create self-signed certificates.

3. -new: This option indicates that you want to create a new certificate request.

4. -x509: This option tells OpenSSL to generate a self-signed certificate instead of a certificate signing request (CSR). The -x509 option is commonly used for creating self-signed certificates.

5. -days 365: This option specifies the validity period of the certificate in days. In this case, the certificate will be valid for 365 days (1 year).

6. -nodes: This option stands for "no DES" (Data Encryption Standard). It means that the private key will not be encrypted with a passphrase. This is useful for server applications where you want the server to start without requiring user input for the passphrase.

7. -out server.crt: This option specifies the output file for the generated certificate. In this case, the certificate will be saved as server.crt.

8. -keyout server.key: This option specifies the output file for the generated private key. In this case, the private key will be saved as server.key.