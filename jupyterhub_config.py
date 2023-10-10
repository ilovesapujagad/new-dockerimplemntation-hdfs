# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

# Configuration file for JupyterHub
import os

c = get_config()  # noqa: F821

c.JupyterHub.load_roles = [  # noqa: F821
    {
        "name": "test-admin",
        "scopes": ["admin:users", "admin:servers", "access:servers"],
        "services": ["test"],
    }
]

c.JupyterHub.services = [  # noqa: F821
    {
        "name": "test",
        "api_token": "test-token-123",
    }
]
# We rely on environment variables to configure JupyterHub so that we
# avoid having to rebuild the JupyterHub container every time we change a
# configuration parameter.

# Spawn single-user servers as Docker containers
c.JupyterHub.spawner_class = 'sudospawner.SudoSpawner'


# User containers will access hub by container name on the Docker network
c.JupyterHub.hub_ip = "jupyter"
c.JupyterHub.hub_port = 8080

# Persist hub data on volume mounted inside container
c.JupyterHub.cookie_secret_file = "/data/jupyterhub_cookie_secret"
c.JupyterHub.db_url = "sqlite:////data/jupyterhub.sqlite"

# Authenticate users with Native Authenticator
c.JupyterHub.authenticator_class = "nativeauthenticator.NativeAuthenticator"

# Allow anyone to sign-up without approval
c.NativeAuthenticator.open_signup = True

# Allowed admins
admin = os.environ.get("JUPYTERHUB_ADMIN")
if admin:
    c.Authenticator.admin_users = [admin]

