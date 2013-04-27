import sublime, sublime_plugin, webbrowser
from github import *

class GithubPullRequestCommand(GithubWindowCommand):
  @with_repo
  def run(self, repo):
    webbrowser.open_new_tab(repo.pull_request_url('master'))
