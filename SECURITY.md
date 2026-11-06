# Security policy

## Credentials

Never commit API keys, access tokens, passwords, private dotenv files or other credentials.
The Skill uses only these variable names as optional configuration references:

- `SLET_OPENALEX_API_KEY`
- `SLET_NCBI_API_KEY`
- `SLET_CROSSREF_MAILTO`

Real values must remain outside the repository and the Skill directory. Do not paste credentials
into public issues, pull requests, examples or logs.

## Reporting a suspected exposure

Do not publish a credential or exploit details in a public issue. Contact the repository maintainer
through GitHub's private reporting/contact mechanism where available. If a credential may have been
exposed, revoke or rotate it at the issuing provider before investigating repository history.
