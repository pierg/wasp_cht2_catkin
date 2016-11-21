import web
from generatePlan import readPlan
import os

cache = False

t_globals = dict(
  datestr=web.datestr,
)
folderpath = os.path.join(os.path.dirname(__file__),'templates/')

render = web.template.render(folderpath, cache=cache, globals=t_globals, base='index')
render._keywords['globals']['render'] = render


def list(**k):
	return render.list(readPlan())