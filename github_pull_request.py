import sublime, sublime_plugin, webbrowser
from github import *

class GithubPullRequestCommand(GithubWindowCommand):
  @with_repo
  def run(self, repo):
    self.repo = repo
    branches = self.repo.get_remote_branches()
    if not branches:
        branches = ''
    self.branch_done(branches)

  def branch_done(self, result):
    self.results = result
    self.window.show_quick_panel(self.results, self.panel_done, sublime.MONOSPACE_FONT)

  def panel_done(self, picked):
    picked_branch = self.results[picked]
    webbrowser.open_new_tab(self.repo.pull_request_url(picked_branch))
