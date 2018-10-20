import requests

# Raised whenever there is an error.

class GithubError(Exception):
    def __init__(self, status=200, msg=''):
        self.status = status
        self.msg = msg

# Possible urls.

URLS = {
    'repo_commits': 'https://api.github.com/repos/{user}/{repo}/commits',
    'user_account': 'https://api.github.com/users/{user}',
    'user_repos': 'https://api.github.com/users/{user}/repos',
}

# Client functions.

def get_repo_commits(user, repo, params={}):
    r = requests.get(URLS['repo_commits'].format(user=user, repo=repo), params=params)
    if r.status_code == 404:
        raise GithubError(status=404, msg='User Not Found!')
    return r.json ()

def get_user_info(user, params={}):
    r = requests.get(URLS['user_account'].format(user=user), params=params)
    if r.status_code == 404:
        raise GithubError(status=404, msg='User Not Found!')
    return r.json()

def get_user_repos(user, params={}):
    r = requests.get(URLS['user_repos'].format(user=user), params=params)
    if r.status_code == 404:
        raise GithubError(status=404, msg='User Not Found!')
    return r.json()

