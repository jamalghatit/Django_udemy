# Precisa melhorar a segurança da sua aplicação Django? Vamos lá!

- Criar ambiente virtual, instalar o django e criar projeto segurança.
- Configurar o settings.py como nos projetos anteriores.

Segurança contra:

- Cross Site Scripting (XSS) - faz sanitização

- Cross Site Request Forgery (CSRF) - {% csrf_token %}

- SQL Injection

- Suporta HTTPS e TLS;

- Armazenamento seguro de senhas - Algoritmo PBKDF2 com SHA256 recomendado pelo NIST

- Recursos extras no settings.py

```python

# Recursos extras de segurança no django
SECURE_HSTS_SECONDS = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

# SECURE_SSL_REDIRECT = True
```

https://docs.djangoproject.com/en/3.2/ref/middleware/#module-django.middleware.security