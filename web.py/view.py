import web
from generatePlan import readPlan

cache = False

t_globals = dict(
  datestr=web.datestr,
)
render = web.template.render('templates/', cache=cache, 
    globals=t_globals)
render._keywords['globals']['render'] = render


def list(**k):
	return render.list(readPlan())